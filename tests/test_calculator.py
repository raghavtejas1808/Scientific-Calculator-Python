from calculator.calculator import *

def test_square_root():
    assert square_root(16) == 4

def test_factorial():
    assert factorial(5) == 120

def test_log():
    assert round(natural_log(1), 5) == 0

def test_power():
    assert power(2,3) == 8