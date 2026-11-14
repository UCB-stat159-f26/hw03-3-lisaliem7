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


def _download_career_js(slug):
    """Return the career JS text, or raise a clear error for unknown players."""
    response = requests.get(CAREER_URL.format(slug=slug), timeout=15)
    if response.status_code != 200 or "morematchmx" not in response.text:
        raise ValueError(
            f"No player found for '{slug}'. Check the spelling, e.g. 'Serena Williams'."
        )
    return response.text


def _download_birthdate(slug):
    """Return the player's own birthdate from their tennisabstract page."""
    response = requests.get(PAGE_URL.format(slug=slug), timeout=15)
    return _parse_birthdate(response.text)
