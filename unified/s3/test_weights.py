import pytest
from weights import shipping_cost

import pytest

@pytest.mark.parametrize("weight, expected", [
    (1, 5),          # normal case under 2kg
    (2, 5),          # boundary case at 2kg
    (5, 5 + 1.5 * 3),# normal case between 2kg and 10kg
    (10, 5 + 1.5 * 8),# boundary case at 10kg
    (12, 20),        # normal case above 10kg,
    (0, 5)           # boundary case at 0kg
])
def test_shipping_cost(weight, expected):
    assert shipping_cost(weight) == expected

def test_shipping_cost_negative():
    with pytest.raises(ValueError):
        shipping_cost(-1)