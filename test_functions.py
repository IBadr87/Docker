from operator import truediv
from main import count_char, check_if_maj, check_if_special, check_if_valid_password

def test_count_char():
    
    input1 = ""
    expected1 = 0
    
    input2 = "Bon"
    expected2 = 3
    
    input3 = "Bonjour"
    expected3 = 7

    result1 = count_char(input1)
    assert expected1 == result1
    
    result2 = count_char(input2)
    assert expected2 == result2
    
    result3 = count_char(input3)
    assert expected3 == result3

def test_check_if_maj():
    input1 = "bonjour"
    expected1 = 0

    input2 = "BonJOur"
    expected2 = 3
    
    input3 = "BONJOUR"
    expected3 = 7

    result1 = check_if_maj(input1)
    assert expected1 == result1

    result2 = check_if_maj(input2)
    assert expected1 == result2

    result3 = check_if_maj(input3)
    assert expected1 == result3

def test_check_if_special():
    input1 = "bonjour"
    expected1 = 0

    input2 = "Bonjour!"
    expected2 = 1
    
    input3 = "Bon_jour*"
    expected3 = 2

    result1 = check_if_special(input1)
    assert expected1 == result1

    result2 = check_if_special(input2)
    assert expected1 == result2

    result3 = check_if_special(input3)
    assert expected1 == result3

def test_check_if_valid_password():
    input1 = "bon"
    expected1 = False

    input2 = "Bonjour"
    expected2 = False
    
    input3 = "bonjourrrrrr"
    expected3 = True

    result1 = check_if_valid_password(input1)
    assert expected1 == result1

    result2 = check_if_valid_password(input2)
    assert expected2 == result2

    result3 = check_if_valid_password(input3)
    assert expected3 == result3
    