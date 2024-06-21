API_DESCRIPTION = """Custom leaderboards for PewPewLive.<br>
Note that for every method, you can drop /v1 part or use /latest.<br>
Artemii Kravchuk 2024"""

API_TAGS_METADATA = [
    {
        "name": "scores",
        "description": "Get raw data from the database on player/level scores",
    },
    {
        "name": "leaderboards",
        "description": """Access cached data from calculations for the leaderboard
            (vars like N and R)""",
    },
    {
        "name": "parse",
        "description": "Parse message from #scores-feed in Discord server",
    },
    {
        "name": "update",
        "description": "Mostly used internally functions for updating scores in the database",
    }
]
