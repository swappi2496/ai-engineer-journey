from bank import value

def test_hello_lowercase():
    assert value("hello") == 0
    assert value("hello, world") == 0

def test_hello_uppercase():
    assert value("HELLO") == 0
    assert value("Hello, you!") == 0

def test_start_with_h_lowercase():
    assert value("hi") == 20
    assert value("hey, there") == 20

def test_start_with_h_uppercase():
    assert value("How are you?") == 20
    assert value("Hey!") == 20

def test_other_grettings():
    assert value("what's up?") == 100
    assert value("Good Morning") == 100

def test_with_whitespace():
    assert value(" hello") == 0
    assert value(" hi") == 20

def test_empty_string():
    assert value("") == 100
