import pytest
from movie_tickets import ticket_price, group_discount, snack_combo

# ==============================================================================
# Comprehensive Branch Coverage Test Suite
# Target: 100% Branch Coverage & 100% Line Coverage with Decision & Boundary Analysis
# ==============================================================================

# ------------------------------------------------------------------------------
# 1. ticket_price Branch Tests
# ------------------------------------------------------------------------------

def test_ticket_price_invalid_seat():
    # Branch: seat not in SEAT_PRICE (True)
    with pytest.raises(ValueError, match="unknown seat"):
        ticket_price("box_office", 25, 14, False)

def test_ticket_price_hour_negative():
    # Branch: show_hour < 0 (True)
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, -1, False)

def test_ticket_price_hour_exceeds_23():
    # Branch: show_hour > 23 (True)
    with pytest.raises(ValueError, match="invalid show time"):
        ticket_price("regular", 25, 24, False)

def test_ticket_price_morning_boundary_min():
    # Branch: show_hour < 12 (True, boundary 0), age adult, weekday
    # Regular (150) - 50 = 100
    assert ticket_price("regular", 25, 0, False) == 100

def test_ticket_price_morning_boundary_max():
    # Branch: show_hour < 12 (True, boundary 11), age adult, weekday
    # Premium (250) - 50 = 200
    assert ticket_price("premium", 30, 11, False) == 200

def test_ticket_price_afternoon_boundary_start():
    # Branch: show_hour < 12 (False), show_hour >= 18 (False, boundary 12)
    # Recliner (400), no hour adjustment
    assert ticket_price("recliner", 30, 12, False) == 400

def test_ticket_price_afternoon_boundary_end():
    # Branch: show_hour < 12 (False), show_hour >= 18 (False, boundary 17)
    # Regular (150)
    assert ticket_price("regular", 25, 17, False) == 150

def test_ticket_price_evening_boundary_start():
    # Branch: show_hour >= 18 (True, boundary 18)
    # Premium (250) + 30 = 280
    assert ticket_price("premium", 30, 18, False) == 280

def test_ticket_price_evening_boundary_end():
    # Branch: show_hour >= 18 (True, boundary 23)
    # Recliner (400) + 30 = 430
    assert ticket_price("recliner", 30, 23, False) == 430

def test_ticket_price_weekend_adjustment():
    # Branch: is_weekend (True) vs (False)
    # Regular (150) + weekend (40) = 190
    assert ticket_price("regular", 25, 14, True) == 190

def test_ticket_price_infant_boundary_zero():
    # Branch: age < 3 (True, boundary 0)
    assert ticket_price("recliner", 0, 14, True) == 0

def test_ticket_price_infant_boundary_two():
    # Branch: age < 3 (True, boundary 2)
    assert ticket_price("recliner", 2, 20, False) == 0

def test_ticket_price_child_boundary_lower():
    # Branch: age < 3 (False), age <= 12 (True, boundary 3)
    # Regular (150) // 2 = 75
    assert ticket_price("regular", 3, 14, False) == 75

def test_ticket_price_child_boundary_upper():
    # Branch: age <= 12 (True, boundary 12)
    # Premium (250) // 2 = 125
    assert ticket_price("premium", 12, 14, False) == 125

def test_ticket_price_teenager_boundary():
    # Branch: age <= 12 (False, boundary 13), age >= 60 (False)
    # Recliner (400)
    assert ticket_price("recliner", 13, 14, False) == 400

def test_ticket_price_adult_upper_boundary():
    # Branch: age <= 12 (False), age >= 60 (False, boundary 59)
    # Regular (150)
    assert ticket_price("regular", 59, 14, False) == 150

def test_ticket_price_senior_boundary_start():
    # Branch: age <= 12 (False), age >= 60 (True, boundary 60)
    # Regular (150) // 2 = 75
    assert ticket_price("regular", 60, 14, False) == 75

def test_ticket_price_senior_above_boundary():
    # Branch: age >= 60 (True, age 80)
    # Premium (250) // 2 = 125
    assert ticket_price("premium", 80, 14, False) == 125


# ------------------------------------------------------------------------------
# 2. group_discount Branch Tests
# ------------------------------------------------------------------------------

def test_group_discount_zero_tickets():
    # Branch: tickets < 1 (True, boundary 0)
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(0, False)

def test_group_discount_negative_tickets():
    # Branch: tickets < 1 (True, negative)
    with pytest.raises(ValueError, match="no tickets"):
        group_discount(-3, True)

def test_group_discount_small_group_boundary_min():
    # Branch: tickets >= 10 (False), tickets >= 5 (False), boundary 1
    assert group_discount(1, False) == 0

def test_group_discount_small_group_boundary_max():
    # Branch: tickets >= 5 (False), boundary 4
    assert group_discount(4, False) == 0

def test_group_discount_small_group_student():
    # Branch: is_student_group (True) but discount > 0 (False) -> no student bonus
    assert group_discount(3, True) == 0

def test_group_discount_medium_group_boundary_min():
    # Branch: tickets >= 5 (True, boundary 5), is_student_group (False)
    assert group_discount(5, False) == 10

def test_group_discount_medium_group_boundary_max():
    # Branch: tickets >= 5 (True, boundary 9), is_student_group (False)
    assert group_discount(9, False) == 10

def test_group_discount_medium_group_student():
    # Branch: tickets >= 5 (True), is_student_group (True) and discount > 0 (True)
    # 10 + 5 = 15
    assert group_discount(7, True) == 15

def test_group_discount_large_group_boundary_min():
    # Branch: tickets >= 10 (True, boundary 10), is_student_group (False)
    assert group_discount(10, False) == 15

def test_group_discount_large_group_student():
    # Branch: tickets >= 10 (True), is_student_group (True) and discount > 0 (True)
    # 15 + 5 = 20
    assert group_discount(20, True) == 20


# ------------------------------------------------------------------------------
# 3. snack_combo Branch Tests
# ------------------------------------------------------------------------------

def test_snack_combo_small_no_coupon():
    # Branch: size == 'small' (True), has_coupon (False)
    assert snack_combo("small", False) == 120

def test_snack_combo_small_with_coupon():
    # Branch: size == 'small' (True), has_coupon (True)
    assert snack_combo("small", True) == 70

def test_snack_combo_medium_no_coupon():
    # Branch: size == 'medium' (True), has_coupon (False)
    assert snack_combo("medium", False) == 180

def test_snack_combo_medium_with_coupon():
    # Branch: size == 'medium' (True), has_coupon (True)
    assert snack_combo("medium", True) == 130

def test_snack_combo_large_no_coupon():
    # Branch: else branch (True), has_coupon (False)
    assert snack_combo("large", False) == 250

def test_snack_combo_large_with_coupon():
    # Branch: else branch (True), has_coupon (True)
    assert snack_combo("large", True) == 200

def test_snack_combo_unknown_size_with_coupon():
    # Branch: else branch fallback for other size names
    assert snack_combo("extra_large", True) == 200
