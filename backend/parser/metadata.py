"""Parse raw metadata in #scores-feed scores"""

from loguru import logger

logger = logger.opt(colors=True)

PLATFORMS = {
    "a": ["Android", ":android:", "<:android:"],
    "i": [":ios:", ""],
    "w": ["🪟"],
    "b": ["🌐", "web"],
    "u": ["❓"]
}


def parse_platform(raw_platform: str) -> str:
    """Parse raw platform string into platform char
    a android, i ios, w windows, b web, u/e unknown
    (e - uknown by parser, u - uknown by #scores-feed)"""
    logger.trace("Parsing <m>{}</> into known platform", raw_platform)

    for char, matches in PLATFORMS.items():
        if raw_platform in matches:
            return char

    return "e"
