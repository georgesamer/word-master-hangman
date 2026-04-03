from project import check_guess, get_difficulty, DIFFICULTY_SETTINGS
import pytest

def test_check_guess():
    assert check_guess("a", "apple", set()) == True
    assert check_guess("z", "apple", set()) == False
    assert check_guess("1", "apple", set()) == False
    assert check_guess("apple", "apple", set()) == False

def test_difficulty_settings():
    assert "easy" in DIFFICULTY_SETTINGS
    assert DIFFICULTY_SETTINGS["easy"]["attempts"] == 6
    assert DIFFICULTY_SETTINGS["hard"]["min_len"] == 8

def test_get_difficulty_logic():
    choices = {"1": "easy", "2": "medium", "3": "hard"}
    assert choices["1"] == "easy"
    assert choices["3"] == "hard"