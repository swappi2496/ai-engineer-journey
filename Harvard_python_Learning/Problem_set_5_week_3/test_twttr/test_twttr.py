from twttr import shorten


def test_lowercase():
    assert shorten("hello") == "hll"
    assert shorten("twitter") == "twttr"

def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("TWITTER") == "TWTTR"

def test_mixed_case():
    assert shorten("Hello") == "Hll"
    assert shorten("Twitter") == "Twttr"

def test_numbers():
    assert shorten("CS50") == "CS50"
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("Hello, world!") == "Hll, wrld!"
    assert shorten("What's up?") == "Wht's p?"

def test_empty_string():
    assert shorten("") == ""

def test_no_vowels():
    assert shorten("rhythm") == "rhythm"
    assert shorten("xyz") == "xyz"
