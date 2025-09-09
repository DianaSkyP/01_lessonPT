import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("testing", "Testing"),
    ("a", "A"),
    ("UPPERCASE", "Uppercase"),
    ("привет", "Привет"),
])
def test_capitalize_positive(input_str, expected):
    """Позитивные тесты для capitalize с параметризацией"""
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    ("!hello", "!hello"),
    ("@world", "@world"),
])
def test_capitalize_negative(input_str, expected):
    """Негативные тесты для capitalize с параметризацией"""
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("     hello", "hello"),
    ("  test", "test"),
    (" single", "single"),
])
def test_trim_positive(input_str, expected):
    """Позитивные тесты для trim с параметризацией"""
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("     ", ""),
    ("skypro", "skypro"),
    ("skypro   ", "skypro   "),
    ("\t\thello", "\t\thello"),
    ("\n\nworld", "\n\nworld"),
])
def test_trim_negative(input_str, expected):
    """Негативные тесты для trim с параметризацией"""
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),
    ("hello", "e", True),
    ("test", "test", True),
    ("programming", "gram", True),
    ("123abc", "2", True),
    ("Hello@World", "@", True),
])
def test_contains_positive(string, symbol, expected):
    """Позитивные тесты для contains с параметризацией"""
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "U", False),
    ("SKYPRO", "s", False),
    ("hello", "X", False),
    ("", "a", False),
    ("test", "z", False),
])
def test_contains_negative(string, symbol, expected):
    """Негативные тесты для contains с параметризацией"""
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("Mississippi", "s", "Miiippi"),
    ("SkyPro", "Pro", "Sky"),
    ("Hello World", " ", "HelloWorld"),
    ("test123test", "1", "test23test"),
])
def test_delete_symbol_positive(string, symbol, expected):
    """Позитивные тесты для delete_symbol с параметризацией"""
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "X", "SkyPro"),
    ("", "a", ""),
    ("test", "", "test"),
    ("SkyPro", "s", "SkyPro"),
    ("hello", "z", "hello"),
])
def test_delete_symbol_negative(string, symbol, expected):
    """Негативные тесты для delete_symbol с параметризацией"""
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.defect
def test_trim_with_tabs():
    """Тест выявляющий дефект: trim не обрабатывает табуляции"""
    result = string_utils.trim("\t\thello")

    assert result == "\t\thello"


@pytest.mark.defect
def test_trim_with_newlines():
    """Тест выявляющий дефект: trim не обрабатывает переносы строк"""
    result = string_utils.trim("\n\nworld")

    assert result == "\n\nworld"


@pytest.mark.defect
def test_contains_empty_symbol():
    """Тест граничного случая: поиск пустого символа"""
    result = string_utils.contains("SkyPro", "")

    assert result is True


@pytest.mark.performance
def test_trim_performance_issue():
    """Тест выявляющий проблему производительности trim"""
    import time

    long_string = " " * 1000 + "test"

    start_time = time.time()
    result = string_utils.trim(long_string)
    end_time = time.time()

    assert result == "test"

    execution_time = end_time - start_time
    print(f"Время выполнения trim для 1000 пробелов: "
          f"{execution_time:.6f} секунд")


@pytest.mark.validation
def test_capitalize_with_none():
    """Тест валидации: capitalize с None должен вызвать исключение"""
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


@pytest.mark.validation
def test_trim_with_none():
    """Тест валидации: trim с None должен вызвать исключение"""
    with pytest.raises(AttributeError):
        string_utils.trim(None)


@pytest.mark.validation
def test_contains_with_none():
    """Тест валидации: contains с None должен вызвать исключение"""
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")


@pytest.mark.validation
def test_delete_symbol_with_none():
    """Тест валидации: delete_symbol с None должен вызвать исключение"""
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")
