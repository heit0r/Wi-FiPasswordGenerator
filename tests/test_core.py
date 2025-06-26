from wi_fipasswordgenerator import core

def test_63_character_length():
    assert core.verify_input_size(100) == 63 
    assert core.verify_input_size(63) == 63
    assert core.verify_input_size(10) == 10
    assert core.verify_input_size(8) == 8
    assert core.verify_input_size(3) == 8
    assert core.verify_input_size(-3) == 8
    
def test_verify_easy_or_hard_characters():
    assert core.verify_characters(0) == core.easy_characters
    assert core.verify_characters(1) == core.hard_characters
    assert core.verify_characters(2) == core.hard_characters
    assert core.verify_characters(3) == core.hard_characters

def test_password_with_lenght_of_1000():
    password = core.generate_password(1000, 0)
    assert len(password) == 1000
    assert "|" "l" "I" "\\" not in password

