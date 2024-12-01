import pytest
from calculator.calculator import Calculator
import math

class TestCalculator:
    @pytest.fixture
    def calc(self):
        return Calculator()
    
    # Basic Operations Tests
    @pytest.mark.parametrize("x, y, expected", [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (99.9, 0.1, 100),
    ])
    def test_add(self, calc, x, y, expected):
        assert calc.add(x, y) == expected
    
    @pytest.mark.parametrize("x, y, expected", [
        (5, 3, 2),
        (1, 1, 0),
        (0, -1, 1),
        (10.5, 0.5, 10),
    ])
    def test_subtract(self, calc, x, y, expected):
        assert calc.subtract(x, y) == expected
    
    @pytest.mark.parametrize("x, y, expected", [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 5, 0),
        (0.5, 2, 1),
    ])
    def test_multiply(self, calc, x, y, expected):
        assert calc.multiply(x, y) == expected
    
    @pytest.mark.parametrize("x, y, expected", [
        (6, 2, 3),
        (5, 2, 2.5),
        (-6, 2, -3),
        (0, 5, 0),
    ])
    def test_divide(self, calc, x, y, expected):
        assert calc.divide(x, y) == expected
    
    def test_divide_by_zero(self, calc):
        with pytest.raises(ValueError):
            calc.divide(1, 0)
    
    # Advanced Operations Tests
    @pytest.mark.parametrize("x, expected", [
        (100, 2),
        (1, 0),
        (10, 1),
    ])
    def test_logarithm(self, calc, x, expected):
        assert calc.logarithm(x) == expected
    
    def test_logarithm_invalid(self, calc):
        with pytest.raises(ValueError):
            calc.logarithm(0)
        with pytest.raises(ValueError):
            calc.logarithm(-1)
    
    @pytest.mark.parametrize("x, expected", [
        (2, 4),
        (-2, 4),
        (0, 0),
        (0.5, 0.25),
    ])
    def test_square(self, calc, x, expected):
        assert calc.square(x) == expected
    
    @pytest.mark.parametrize("x, expected", [
        (4, 2),
        (0, 0),
        (2, math.sqrt(2)),
        (100, 10),
    ])
    def test_square_root(self, calc, x, expected):
        assert calc.square_root(x) == expected
    
    def test_square_root_invalid(self, calc):
        with pytest.raises(ValueError):
            calc.square_root(-1) 