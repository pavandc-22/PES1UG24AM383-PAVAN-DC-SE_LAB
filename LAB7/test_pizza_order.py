
import pytest
from hypothesis import given, strategies as st, settings

from pizza_order import (
    toppings_price,
    pizza_inches,
    split_bill
)


# ==========================================
# 1. FUZZ TEST: TOPPINGS PRICE
# ==========================================

@given(st.text() | st.none())
@settings(max_examples=100)
def test_toppings_price_no_unexpected_crash(s):
    try:
        toppings_price(s)
    except ValueError:
        pass


# ==========================================
# 2. FUZZ TEST: PIZZA INCHES
# ==========================================

@given(st.text() | st.none())
@settings(max_examples=100)
def test_pizza_inches_no_unexpected_crash(s):
    try:
        pizza_inches(s)
    except ValueError:
        pass


# ==========================================
# 3. FUZZ TEST: SPLIT BILL
# ==========================================

@given(st.text() | st.none())
@settings(max_examples=100)
def test_split_bill_no_unexpected_crash(s):
    try:
        split_bill(s)
    except ValueError:
        pass


# ==========================================
# 4. VALID INPUT TESTS
# ==========================================

def test_valid_toppings():
    assert toppings_price("cheese,olives") == 70


def test_valid_pizza_size():
    assert pizza_inches("M") == 10


def test_valid_bill_split():
    assert split_bill("900/3") == 300.0


# ==========================================
# 5. INVALID INPUT TESTS
# ==========================================

@pytest.mark.parametrize("value", ["", "   ", None, "unknown"])
def test_invalid_toppings(value):
    with pytest.raises(ValueError):
        toppings_price(value)


@pytest.mark.parametrize("value", ["", "X", "XX", None])
def test_invalid_pizza_size(value):
    with pytest.raises(ValueError):
        pizza_inches(value)


@pytest.mark.parametrize(
    "value",
    ["", "/", "900/0", "abc/2", "900", None, "-100/2"]
)
def test_invalid_bill(value):
    with pytest.raises(ValueError):
        split_bill(value)
