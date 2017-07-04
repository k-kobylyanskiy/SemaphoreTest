import pytest
import main

def test_sum():
    assert main.sum(2, 2) == 4

def test_sub():
    assert main.sub(6, 2) == 4

def test_mul():
    assert main.mul(2, 2) == 5
