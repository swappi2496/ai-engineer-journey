from plates import is_valid

def test_valid_plates():
    assert is_valid("CS50") == True
    assert is_valid("AB") == True
    assert is_valid("ABCDEF") == True
    assert is_valid("AB12") == True

def test_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("") == False

def test_must_start_with_two_letters():
    assert is_valid("1A") == False
    assert is_valid("A1") == False
    assert is_valid("12") == False

def test_first_number_cannot_be_zero():
    assert is_valid("AAA01") == False
    assert is_valid("AAA10") == True

def test_no_punctuation_or_space():
    assert is_valid("AB.CD") == False
    assert is_valid("AB CD") == False
    assert is_valid("AB-12") == False
    assert is_valid("PI3.14") == False

def test_no_special_chars():
    assert is_valid("AB!@") == False
    assert is_valid("AB#1") == False

def test_numbers_only_at_the_end():
    assert is_valid("A1b2") == False
    assert is_valid("AAA2A") == False
    assert is_valid("AB22") == True
