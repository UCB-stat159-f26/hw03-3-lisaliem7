"""Private helpers that turn a tennisabstract career JS string into a clean DataFrame."""
import json
import re


def _extract_matches(js_text):
    """Return the list of match rows stored in 'var morematchmx = [[...]];'."""
    marker = re.search(r"morematchmx\s*=\s*", js_text)
    if marker is None:
        raise ValueError("Could not find match data in the JS file.")
    rows, _ = json.JSONDecoder().raw_decode(js_text[marker.end():])
    return rows
