import json
import yaml
from urllib.parse import quote
from pathlib import Path

icons = {}
with open(
    Path(__file__).parent.parent / "assets"/"simple-icons.json", "r", encoding="utf8"
) as f:
    simple_icons = json.load(f)["icons"]
    for icon in simple_icons:
        name = icon["title"].lower()
        icons[name] = icon["hex"]


def get_badge_color(title):
    if title in icons:
        return icons[title]
    else:
        return ""


def generate_badge_url(badges_list: list, theme, theme_color, style):
    base_url = "https://img.shields.io/badge/"
    output_list = []
    for badge in badges_list:
        print(badge)
        title = badge.get("title", badge["icon"])
        description = badge.get("description", "")
        color = get_badge_color(badge["icon"])
        if color == "" and badge["icon"] != "":
            color = badge["color"]
        description = description + "-" if description != "" else ""
        logo_color = (
            "&labelColor=eff0ff&logoColor=" + color
            if badge.get("description", "") == "" or theme == "unify"
            else "&logoColor=white"
        )
        color_str = (
            theme_color if theme == "unify" else color
        )
        try:
            uri = quote(
                title.replace("-", "_")
                + "-"
                + description
                + color_str
                + "?style="
                + style
                + "&logo="
                + badge["icon"]
                + logo_color,
                safe="?&=",
            )

            output_list.append("![%s](%s)" % (title, base_url + uri))
        except IndexError:
            print("Icon not found: ", badge["icon"])
    return output_list
