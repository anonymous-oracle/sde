import pytest

def double(n): return n * 2

def test_first(): assert double(1) == 2

@pytest.mark.parametrize("n, want", [(1, 2), (2, 5), (3, 6), (4, 8)])
def test_double(n, want):
    assert double(n) == want

def test_last(): assert double(0) == 1