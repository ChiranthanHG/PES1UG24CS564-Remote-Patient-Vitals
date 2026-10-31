import pytest
from movie_tickets import ticket_price, group_discount, snack_combo

# --- Code Coverage Test Suite (Achieves 100% Line Coverage) ---

# ticket_price line coverage tests
def test_ticket_price_invalid_seat():
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("invalid_seat", 25, 15, False)

def test_ticket_price_invalid_hour():
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 25, False)

def test_ticket_price_morning_show():
    # Regular (150) - Morning discount (50) = 100
    assert ticket_price("regular", 25, 10, False) == 100

def test_ticket_price_evening_weekend():
    # Premium (250) + Evening (30) + Weekend (40) = 320
    assert ticket_price("premium", 25, 19, True) == 320

def test_ticket_price_infant():
    # Age < 3 -> 0
    assert ticket_price("recliner", 2, 14, False) == 0

def test_ticket_price_child_discount():
    # Regular (150) // 2 = 75
    assert ticket_price("regular", 10, 14, False) == 75

def test_ticket_price_standard_adult():
    # Regular (150)
    assert ticket_price("regular", 30, 14, False) == 150


# group_discount line coverage tests
def test_group_discount_invalid_tickets():
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)

def test_group_discount_large():
    # >= 10 tickets -> 15%
    assert group_discount(12, False) == 15

def test_group_discount_medium():
    # >= 5 tickets -> 10%
    assert group_discount(6, False) == 10

def test_group_discount_small():
    # < 5 tickets -> 0%
    assert group_discount(2, False) == 0

def test_group_discount_student():
    # >= 10 tickets (15) + student (5) = 20%
    assert group_discount(10, True) == 20


# snack_combo line coverage tests
def test_snack_combo_small_with_coupon():
    # Small (120) - 50 = 70
    assert snack_combo("small", True) == 70

def test_snack_combo_medium_with_coupon():
    # Medium (180) - 50 = 130
    assert snack_combo("medium", True) == 130

def test_snack_combo_large_with_coupon():
    # Large/other (250) - 50 = 200
    assert snack_combo("large", True) == 200
