import pytest

from pizza_order import (
    pizza_price,
    order_discount,
    delivery_status
)


# ==========================================
# 1. PIZZA PRICE - BRANCH COVERAGE
# ==========================================

def test_invalid_size():
    with pytest.raises(ValueError, match="unknown size"):
        pizza_price("extra_large", 2, False)


def test_negative_toppings():
    with pytest.raises(ValueError, match="invalid toppings"):
        pizza_price("medium", -1, False)


def test_three_or_fewer_toppings():
    assert pizza_price("small", 3, False) == 320


def test_more_than_three_toppings():
    assert pizza_price("large", 4, False) == 650


def test_cheese_burst_small_pizza():
    with pytest.raises(
        ValueError,
        match="cheese burst not available for small"
    ):
        pizza_price("small", 0, True)


def test_cheese_burst_medium_pizza():
    assert pizza_price("medium", 0, True) == 450


def test_without_cheese_burst():
    assert pizza_price("small", 0, False) == 200


# ==========================================
# 2. ORDER DISCOUNT - BRANCH COVERAGE
# ==========================================

def test_order_below_300():
    assert order_discount(299, "monday", True) == 0


def test_tuesday_without_student_discount():
    assert order_discount(300, "tuesday", False) == 150


def test_saturday_discount_without_student():
    assert order_discount(500, "saturday", False) == 0


def test_normal_weekday_with_student_discount():
    assert order_discount(500, "monday", True) == 100


# ==========================================
# 3. DELIVERY STATUS - BRANCH COVERAGE
# ==========================================

def test_distance_above_10_km():
    assert delivery_status(20, 11) == "not deliverable"


def test_delivery_exactly_10_km_and_30_minutes():
    assert delivery_status(30, 10) == "on time"


def test_delivery_exactly_45_minutes():
    assert delivery_status(45, 5) == "late"


def test_delivery_after_45_minutes():
    assert delivery_status(46, 5) == "free pizza"