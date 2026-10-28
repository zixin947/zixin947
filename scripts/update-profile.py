"""Generate public GitHub profile cards using the authenticated GitHub CLI."""

import html
import json
from pathlib import Path
import subprocess
from datetime import datetime, timezone
from urllib.parse import urlencode

USER = "zixin947"
LANGUAGE_REPOS = ("dsh-compact", "codex-atelier")
ROOT = Path(__file__).resolve().parents[1]
COLORS = ("#38bdf8", "#34d399", "#c4b5fd", "#fbbf24", "#fb7185")


def api(endpoint):
    result = subprocess.run(
        ["gh", "api", endpoint], check=True, capture_output=True, text=True
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
    ):
        temporary = assets / (name + ".tmp")
        temporary.write_text(svg, encoding="utf-8")
        temporary.replace(assets / name)
    print(f"Generated public profile cards: {stats[1][1]} merged upstream PRs")


if __name__ == "__main__":
    main()
