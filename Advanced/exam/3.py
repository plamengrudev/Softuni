import re

def sort_games(*args, **kwargs):
    title_to_platform = {title: platform for platform, title in args}

    console_games = []
    pc_games = []

    for release_id, game_title in kwargs.items():
        platform = title_to_platform[game_title]

        if platform == "console":
            console_games.append((release_id, game_title))
        else:
            pc_games.append((release_id, game_title))

    console_games.sort(key=lambda x: x[0])
    pc_games.sort(key=lambda x: x[0], reverse=True)

    result = []

    if console_games:
        result.append("Console Games:")
        for release_id, game_title in console_games:
            release_date = re.sub(r"_\d+$", "", release_id)
            result.append(f">>>{release_date}: {game_title}")

    if pc_games:
        result.append("PC Games:")
        for release_id, game_title in pc_games:
            release_date = re.sub(r"_\d+$", "", release_id)
            result.append(f"<<<{release_date}: {game_title}")

    return "\n".join(result)


print(sort_games(
    ("pc", "Iron Comet"),
    ("console", "Jungle Quest"),
    ("console", "Cyber Realm"),
    ("pc", "Neon Skyline"),
    ("console", "Blade Echo"),
    ("pc", "Sky Frontier"),
    April_12_2025_002="Neon Skyline",
    July_01_2025_004="Cyber Realm",
    July_01_2025_002="Blade Echo",
    December_31_2024_007="Jungle Quest",
    April_12_2025_005="Iron Comet",
    February_14_2025_009="Sky Frontier",
))