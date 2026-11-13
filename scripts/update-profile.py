"""Generate public GitHub profile cards using the authenticated GitHub CLI."""

import html
import base64
from collections import Counter
import json
import re
from pathlib import Path
import subprocess
from datetime import datetime, timezone
from urllib.parse import urlencode

USER = "zixin947"
LANGUAGE_REPOS = ("dsh-compact", "codex-atelier")
FEATURED_REPOS = ("Ebony-Vinyl/EACbot", "zixin947/codex-atelier")
ROOT = Path(__file__).resolve().parents[1]
COLORS = ("#38bdf8", "#34d399", "#c4b5fd", "#fbbf24", "#fb7185")


def api(endpoint):
    result = subprocess.run(
        ["gh", "api", endpoint], check=True, capture_output=True, text=True, encoding="utf-8"
    )
    return json.loads(result.stdout)


def text(x, y, value, size=14, color="#cbd5e1", weight=400):
    return (
        f'<text x="{x}" y="{y}" font-size="{size}" fill="{color}" '
        f'font-weight="{weight}">{html.escape(str(value))}</text>'
    )


def card(title, description, content, date):
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="480" height="248" '
        'viewBox="0 0 480 248" role="img" aria-labelledby="title desc">'
        f'<title id="title">{html.escape(title)}</title>'
        f'<desc id="desc">{html.escape(description)}</desc>'
        '<rect x="0.5" y="0.5" width="479" height="247" rx="16" '
        'fill="#0f172a" stroke="#334155"/>'
        '<g font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Arial,sans-serif">'
        + text(24, 37, title, 19, "#f8fafc", 700)
        + '<rect x="24" y="51" width="36" height="3" rx="1.5" fill="#38bdf8"/>'
        + content
        + text(24, 228, f"PUBLIC DATA · {date} UTC", 10, "#94a3b8")
        + "</g></svg>\n"
    )


def main():
    profile = api(f"users/{USER}")
    query = f"is:pr is:merged is:public author:{USER} -user:{USER}"
    merged = api("search/issues?" + urlencode({"q": query, "per_page": 1}))
    if merged.get("incomplete_results"):
        raise RuntimeError("GitHub returned incomplete search results; keeping old cards")
    languages = {}
    for repo in LANGUAGE_REPOS:
        for name, count in api(f"repos/{USER}/{repo}/languages").items():
            languages[name] = languages.get(name, 0) + count
    if not languages or sum(languages.values()) <= 0:
        raise RuntimeError("No language data returned; keeping old cards")

    # Validate all responses before writing either card.
    stats = (
        ("PUBLIC REPOSITORIES", int(profile["public_repos"])),
        ("MERGED UPSTREAM PRs", int(merged["total_count"])),
        ("GITHUB FOLLOWERS", int(profile["followers"])),
    )
    date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    content = ""
    for index, (label, value) in enumerate(stats):
        y = 91 + index * 48
        content += text(24, y, label, 12, "#94a3b8")
        content += text(395, y + 2, value, 24, "#38bdf8", 700)
    stats_svg = card(
        "GitHub at a glance",
        "; ".join(f"{label}: {value}" for label, value in stats),
        content,
        date,
    )
    dashboard_data = fetch_dashboard(query)
    dashboards = {
        f"github-stats-{theme}.svg": dashboard(profile, dashboard_data, date, theme)
        for theme in ("light", "dark")
    }

    entries = sorted(languages.items(), key=lambda item: (-item[1], item[0]))
    total = sum(languages.values())
    top = entries[:4]
    if len(entries) > 4:
        top.append(("Other", sum(value for _, value in entries[4:])))
    content = text(24, 77, "dsh-compact + codex-atelier · code bytes", 11, "#94a3b8")
    x = 24.0
    for index, (_, value) in enumerate(top):
        width = 432 * value / total
        content += (
            f'<rect x="{x:.3f}" y="93" width="{width:.3f}" height="12" '
            f'fill="{COLORS[index]}"/>'
        )
        x += width
    for index, (name, value) in enumerate(top):
        column, row = index % 2, index // 2
        x, y = 24 + column * 224, 135 + row * 27
        content += f'<circle cx="{x + 4}" cy="{y - 4}" r="4" fill="{COLORS[index]}"/>'
        content += text(x + 16, y, f"{name} {100 * value / total:.1f}%", 12)
    language_svg = card(
        "Languages in my projects",
        "Code bytes across " + ", ".join(LANGUAGE_REPOS) + "; not a proficiency score",
        content,
        date,
    )
    assets = ROOT / "assets"
    assets.mkdir(exist_ok=True)
    for name, svg in (
        ("github-stats.svg", stats_svg),
        ("github-languages.svg", language_svg),
        *dashboards.items(),
    ):
        temporary = assets / (name + ".tmp")
        temporary.write_text(svg, encoding="utf-8")
        temporary.replace(assets / name)
    readme = ROOT / "README.md"
    version = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
    markdown = readme.read_text(encoding="utf-8")
    markdown = re.sub(
        r"(assets/github-stats-(?:light|dark)\.svg)(?:\?v=[\w-]+)?",
        lambda match: f"{match[1]}?v={version}",
        markdown,
    )
    readme.write_text(markdown, encoding="utf-8", newline="\n")
    print(f"Generated public profile cards: {stats[1][1]} merged upstream PRs")


def fetch_dashboard(query):
    counts = Counter()
    page = 1
    items = []
    while True:
        response = api("search/issues?" + urlencode({"q": query, "per_page": 100, "page": page}))
        if response.get("incomplete_results") or response["total_count"] > 1000:
            raise RuntimeError("Incomplete upstream PR search; keeping existing cards")
        items.extend(response["items"])
        if len(items) >= response["total_count"]:
            break
        if not response["items"]:
            raise RuntimeError("Missing upstream PR search page")
        page += 1
    for item in items:
        counts[item["repository_url"].split("/repos/", 1)[1]] += 1
    query_text = """query($login:String!){user(login:$login){
      contributionsCollection{contributionCalendar{totalContributions}
      totalCommitContributions totalIssueContributions totalRepositoriesWithContributedCommits}
    }}"""
    result = subprocess.run(
        ["gh", "api", "graphql", "-f", f"query={query_text}", "-f", f"login={USER}"],
        check=True, capture_output=True, text=True, encoding="utf-8",
    )
    collection = json.loads(result.stdout)["data"]["user"]["contributionsCollection"]
    stars = {}
    for repo in dict.fromkeys((*counts, *FEATURED_REPOS)):
        repository = api(f"repos/{repo}")
        stars[repository["full_name"]] = int(repository["stargazers_count"])
    return counts, collection, stars


def dashboard(profile, data, date, theme):
    counts, collection, stars = data
    dark = theme == "dark"
    background, border, foreground, muted, accent = (
        ("#0f172a", "#334155", "#f8fafc", "#94a3b8", "#38bdf8") if dark else
        ("#f8fafc", "#dbe4ef", "#0f172a", "#64748b", "#0369a1")
    )
    total = sum(counts.values())
    thresholds = ((100, "S"), (50, "A"), (20, "B"), (5, "C"), (1, "D"), (0, "E"))
    rank = next(label for floor, label in thresholds if total >= floor)
    rows = (
        ("Merged upstream PRs", total),
        ("Contributions (last year)", collection["contributionCalendar"]["totalContributions"]),
        ("Commits (last year)", collection["totalCommitContributions"]),
        ("Repositories committed to (year)", collection["totalRepositoriesWithContributedCommits"]),
        ("Issues opened (last year)", collection["totalIssueContributions"]),
        ("Public repositories", profile["public_repos"]),
        ("Followers", profile["followers"]),
    )
    body = text(58, 44, "GITHUB STATS", 16, accent, 700)
    for index, (label, value) in enumerate(rows):
        y = 82 + index * 27
        body += text(42, y, label, 12, muted)
        body += f'<text x="350" y="{y}" text-anchor="end" font-size="14" font-weight="700" fill="{foreground}">{value}</text>'
    image = base64.b64encode((ROOT / "assets/deepseek-chan.png").read_bytes()).decode("ascii")
    body += f'<image x="140" y="264" width="110" height="110" href="data:image/png;base64,{image}"/>'
    body += f'<path d="M380 65V370" stroke="{border}"/>'
    body += text(438, 44, f"{total} merged PRs in {len(counts)} upstream repos", 13, muted)
    body += f'<circle cx="625" cy="115" r="47" fill="none" stroke="{accent}" stroke-width="10"/>'
    body += f'<text x="625" y="130" text-anchor="middle" font-size="42" fill="{foreground}" font-weight="700">{rank}</text>'
    body += text(525, 188, f"Custom rank · {total} merged PRs", 12, muted)
    body += text(405, 208, "REPOSITORY STARS", 10, muted, 700)
    ranked = sorted(
        ((repo, count) for repo, count in stars.items() if repo not in FEATURED_REPOS),
        key=lambda item: (-item[1], item[0]),
    )
    top = ranked[:4] + [(repo, stars[repo]) for repo in FEATURED_REPOS]
    peak = max(max((count for _, count in top), default=0), 1)
    for index, (repo, count) in enumerate(top):
        y = 230 + index * 25
        body += text(405, y, repo, 11, foreground)
        width = 120 * count / peak
        body += f'<rect x="680" y="{y - 8}" width="{width:.1f}" height="8" rx="4" fill="{COLORS[index % len(COLORS)]}"/>'
        body += text(808, y, count, 11, muted)
    if not top:
        body += text(445, 250, "No merged upstream pull requests yet", 13, muted)
    body += text(405, 383, "Rank by upstream PRs: E 0 / D 1 / C 5 / B 20 / A 50 / S 100", 10, muted)
    body += text(32, 408, f"PUBLIC DATA · {date} UTC · Top 4 upstream repos + EACbot / Codex Atelier", 10, muted)
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" width="880" height="430" viewBox="0 0 880 430" role="img" aria-labelledby="title">'
        '<title id="title">Zixin GitHub statistics and contributed upstream repository stars</title>'
        f'<rect x="0.5" y="0.5" width="879" height="429" rx="16" fill="{background}" stroke="{border}"/>'
        '<g font-family="Segoe UI,Arial,sans-serif">' + body + '</g></svg>\n'
    )


if __name__ == "__main__":
    main()
