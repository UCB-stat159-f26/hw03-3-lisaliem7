"""Download a player's career data from tennisabstract.com."""
import requests

from tennisage.clean import _build_career_frame, _parse_birthdate

CAREER_URL = "https://www.tennisabstract.com/jsmatches/{slug}Career.js"
PAGE_URL = "https://www.tennisabstract.com/cgi-bin/player.cgi?p={slug}"


def _name_to_slug(player_name):
    """'serena williams' or 'Serena Williams' -> 'SerenaWilliams'."""
    words = player_name.split()
    if len(words) > 1:
        return "".join(word.capitalize() for word in words)
    return player_name.strip()
