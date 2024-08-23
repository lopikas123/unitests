import pytest
from main1 import count_vowels

def test_only_vowels():
    assert count_vowels('аеёиоуыэюя') == 10
    assert count_vowels('АЕЁИОУЫЭЮЯ') == 10

def test_no_vowels():
    assert count_vowels('бгд') == 0
    assert count_vowels('БГД') == 0

def test_mixed_strings():
    assert count_vowels('Привет, как дела?') == 5
    assert count_vowels('ПРИВЕТ, КАК ДЕЛА?') == 5
    assert count_vowels('Hello, world!') == 3