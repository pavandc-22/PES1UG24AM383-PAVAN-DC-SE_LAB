import pytest

from pizza_order import (
    pizza_price,
    order_discount,
    delivery_status
)


# ---------------------------------------
# PIZZA PRICE TEST CASES
# ---------------------------------------

def test_invalid_pizza_size():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra_large", 2, False)


def test_negative_toppings():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)


def test_small_pizza_with_cheese_burst():
    with pytest.raises(
        ValueError,
        match="cheese burst not available for small"
    ):
        pizza_price("small", 2, True)


def test_large_number_of_toppings_with_cheese_burst():
    assert pizza_price("medium", 5, True) == 630


# ---------------------------------------
# ORDER DISCOUNT TEST CASES
# ---------------------------------------

def test_order_below_minimum():
    assert order_discount(250, "monday", True) == 0


def test_tuesday_student_discount():
    assert order_discount(500, "tuesday", True) == 300


def test_weekend_discount():
    assert order_discount(500, "saturday", True) == 50


def test_normal_weekday_discount():
    assert order_discount(500, "monday", True) == 100


# ---------------------------------------
# DELIVERY STATUS TEST CASES
# ---------------------------------------

def test_delivery_not_deliverable():
    assert delivery_status(20, 11) == "not deliverable"


def test_delivery_on_time():
    assert delivery_status(20, 5) == "on time"


def test_delivery_late():
    assert delivery_status(40, 5) == "late"


def test_delivery_free_pizza():
    assert delivery_status(50, 5) == "free pizza"