from string_utils import StringUtils
import pytest

utils = StringUtils()


def test_capitalize_positive():
    result = utils.capitalize("skypro")
    assert result == "Skypro"


def test_capitalize_already_upper():
    result = utils.capitalize("Skypro")
    assert result == "Skypro"


def test_capitalize_empty_string():
    result = utils.capitalize("")
    assert result == ""


def test_capitalize_none():
    with pytest.raises(AttributeError):
        utils.capitalize(None)


def test_capitalize_text_with_space():
    result = utils.capitalize("04 апреля 2023")
    assert result == "04 апреля 2023"


def test_capitalize_numbers():
    result = utils.capitalize("123")
    assert result == "123"


def test_trim_one_space():
    result = utils.trim(" SkyPro")
    assert result == "SkyPro"

def test_trim_many_spaces():
    result = utils.trim("   SkyPro")
    assert result == "SkyPro"

def test_trim_zero_spaces():
    result = utils.trim("SkyPro")
    assert result == "SkyPro"

def test_trim_spaces_in_the_end():
    result = utils.trim("SkyPro ")
    assert result == "SkyPro "

def test_trim_both_sides_spaces():
    result = utils.trim(" SkyPro ")
    assert result == "SkyPro "

def test_contains_symbol():
    result = utils.contains("Skypro", "p")
    assert result == True

def test_not_contains_symbol():
    result = utils.contains("Skypro", "x")
    assert result == False

def test_contains_empty_symbol():
    result = utils.contains("SkyPro", "")
    assert result == True

def test_contains_symbol_in_the_start():
    result = utils.contains("Skypro", "S")
    assert result == True

def test_contains_symbol_in_the_end():
    result = utils.contains("Skypro", "o")
    assert result == True

def test_contains_empty_line():
    result = utils.contains("", "o")
    assert result == False

def test_contains_none_string():
    with pytest.raises(TypeError):
        utils.contains(None, "o")

def test_contains_none_symbol():
    with pytest.raises(TypeError):
        utils.contains("SkyPro", None)


def test_delete_symbol():
    result = utils.delete_symbol("SkyPro", "k")
    assert result == "SyPro"


def test_delete_line():
    result = utils.delete_symbol("SkyPro", "Pro")
    assert result == "Sky"


def test_delete_multi_symbols():
    result = utils.delete_symbol("banana", "a")
    assert result == "bnn"


def test_delete_not_existing_symbol():
    result = utils.delete_symbol("SkyPro", "x")
    assert result == "SkyPro"


def test_delete_empty_line():
    result = utils.delete_symbol("", "a")
    assert result == ""


def test_delete_none_string():
    with pytest.raises(TypeError):
        utils.delete_symbol(None, "a")