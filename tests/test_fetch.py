from tennisage.fetch import _name_to_slug


def test_name_to_slug_accepts_three_formats():
    assert _name_to_slug("serena williams") == "SerenaWilliams"
    assert _name_to_slug("Serena Williams") == "SerenaWilliams"
    assert _name_to_slug("SerenaWilliams") == "SerenaWilliams"
