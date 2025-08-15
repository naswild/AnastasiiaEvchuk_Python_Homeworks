import pytest
from string_processor import StringProcessor

string_processor = StringProcessor()

@pytest.mark.parametrize('text, result', [('привет.', 'Привет.'), ('Пока', 'Пока.'), ('котик', 'Котик.'),
                                          (None, '.'), ([], '.')])
def positive_test_string_processor(text, result):
    res = string_processor.process(text)
    assert res == result

@pytest.mark.parametrize('text', [1234, True])
def negative_test_string_processor(text):
    with pytest.raises(TypeError):
        string_processor.process(text)