import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.string_utils_positive_test
@pytest.mark.parametrize('text, result', [('hello', 'Hello'), ('Skypro', 'Skypro'), ('SkyPRO', 'SkyPRO'),
                                          ('1234', '1234')])
def test_capitalize_positive(text, result):
    new_text = ''
    new_text += string_utils.capitalize(text)
    assert new_text == result

@pytest.mark.string_utils_negative_test
@pytest.mark.parametrize('text, result', [('', ''), (' ', ' ')])
def test_capitalize_negative(text, result):
    new_text = ''
    new_text += string_utils.capitalize(text)
    assert new_text == result

@pytest.mark.string_utils_negative_test
@pytest.mark.parametrize('text', [1234, True, None])
def test_capitalize_negative_error(text):
    with pytest.raises(AttributeError):
        string_utils.capitalize(text)

@pytest.mark.string_utils_positive_test
@pytest.mark.parametrize('text, result', [(' mouse', 'mouse'), ('     mouse', 'mouse'),
                                          ('   Я тебя люблю', 'Я тебя люблю')])
def test_trim_positive(text, result):
    new_text = ''
    new_text += string_utils.trim(text)
    assert new_text == result

@pytest.mark.string_utils_negative_test
@pytest.mark.parametrize('text, result', [('book', 'book'), ('Я иду домой', 'Я иду домой'), ('', ''), (' ', '')])
def test_trim_negative(text, result):
    new_text = ''
    new_text += string_utils.trim(text)
    assert new_text == result

@pytest.mark.string_utils_negative_test
@pytest.mark.parametrize('text', [1234, True, None])
def test_trim_negative_error(text):
    with pytest.raises(AttributeError):
        string_utils.trim(text)

@pytest.mark.string_utils_positive_test
@pytest.mark.parametrize('text, symbol, result', [('Bottle of water', 'l', True), ('Bottle', 'b', False),
                                                  ('Love, hate', ',', True), ('Candy', 'o', False),
                                                  ('Термометр', 'т', True), ('Love and hate', ' ', True),
                                                  ('Hello', 'el', True), ('1234', '2', True)])
def test_contains_positive(text, symbol, result):
    value = string_utils.contains(text, symbol)
    assert value == result

@pytest.mark.string_utils_negative_test
@pytest.mark.parametrize('text, symbol', [(1234, 3), (None, None)])
def test_contains_negative_error(text, symbol):
    with pytest.raises(AttributeError):
        string_utils.contains(text, symbol)

@pytest.mark.string_utils_positive_test
@pytest.mark.parametrize('text, symbol, result', [('Airpods', 'i', 'Arpods'), ('my computer', 'm', 'y coputer'),
                                                  ('new book', ' ', 'newbook'), ('Bottle', 'B', 'ottle'),
                                                  ('bottle', 't', 'bole'), ('hamster', 'am', 'hster'),
                                                  ('pops', 'pops', '')])
def test_delete_symbol_positive(text, symbol, result):
    new_text = ''
    new_text += string_utils.delete_symbol(text, symbol)
    assert result == new_text

@pytest.mark.string_utils_negative_test
@pytest.mark.parametrize('text, symbol, result', [('', '', ''), ('mobile', '', 'mobile'), ('94827', '4', '9827'),
                                                  ('phone', 'k', 'phone')])
def test_delete_symbol_negative(text, symbol, result):
    new_text = ''
    new_text += string_utils.delete_symbol(text, symbol)
    assert result == new_text


