"""Parse a message from #scores-feed"""

import re

from loguru import logger

from parser.metadata import parse_platform

logger = logger.opt(colors=True)


def load_regex(path: str):
    """Load regex from the file and compile it"""
    logger.trace("Loading regex from <m>{}</>", path)

    # [NOTE: regex was simplyfied.. consider not reading
    #  from the file anymore?]
    with open(path, "r", encoding="UTF-8") as file:
        rx = re.compile(file.read())

    return rx


def apply_regex_raw(msg: str):
    """Apply regex without any post-processing done"""
    logger.trace("Applying regex (raw) to <w>{}</>", msg)

    rx = load_regex("parser/regex.txt")
    msg_split = rx.findall(msg)
    logger.debug("Regex's reply: <w>{}</>", msg_split)

    return msg_split


def apply_regex(msg: str) -> [list[str], int, [str, str]]:
    """Apply #scores-feed regex to the string, extracting
    names (usernames / level name), scores and raw metadata"""
    logger.trace("Applying regex to <w>{}</>", msg)

    msg_split = apply_regex_raw(msg)

    names, score, metadata = [], 0, ""
    for group in msg_split:

        if group[0] != "":
            name = group[0][1:-1]
            names.append(name)

        elif group[1] != "":
            raw_metadata = group[1][1:-1]
            metadata = raw_metadata.split(" - ")

        # overwrites previous score. only care
        # about the last one
        elif group[2] != "":
            score = int(group[2])

    return names, score, metadata


def parse_contents(msg: str) -> dict|None:
    """Second step of parsing a score"""
    logger.trace("Parsing contents for: <w>{}</>", msg)

    names, score, raw_metadata = apply_regex(msg)
    logger.debug("Got names: <m>{}</>, score <m>{}</>, metadata <m>{}</>",
                 names, score, raw_metadata)

    usernames, level = names[:-1], names[-1]
    if len(usernames) == 2:
        p1, p2 = usernames
        mode = 1
    else:
        p1, p2 = usernames[0], None
        mode = 0

    country, raw_platform = raw_metadata
    platform = parse_platform(raw_platform)

    result = {
        "username1": p1,
        "username2": p2,
        "_level": level,
        "score": score,
        "country": country,
        "platform": platform,
        "_mode": mode
    }

    return result


def parse_score(raw: str) -> dict|None:
    """Parse given message into a score"""
    logger.debug("Parsing score: <w>{}</>", raw)

    # get the last line (remove "new world record!", etc)
    message = raw.splitlines()[-1]

    # ignore era 1 scores, set era to 2
    if "(era 1)" in message:
        return None
    era = 2

    data = parse_contents(message)

    result = {
        "era": era,
    }

    result.update(data)
    logger.debug("Parsing result: <w>{}</>", result)
    return result