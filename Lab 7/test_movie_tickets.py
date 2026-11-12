from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating


@given(st.text() | st.none())
def test_parse_seat_no_crash(s):
    """
    Hypothesis fuzz test verifying parse_seat never crashes on any arbitrary string or None.
    """
    try:
        parse_seat(s)
    except Exception as e:
        assert False, f"parse_seat crashed with {type(e).__name__}: {e} on input {s!r}"


@given(st.text() | st.none())
def test_total_price_no_crash(s):
    """
    Hypothesis fuzz test verifying total_price never crashes on any arbitrary string or None.
    """
    try:
        total_price(s)
    except Exception as e:
        assert False, f"total_price crashed with {type(e).__name__}: {e} on input {s!r}"


@given(st.text() | st.none())
def test_average_rating_no_crash(s):
    """
    Hypothesis fuzz test verifying average_rating never crashes on any arbitrary string or None.
    """
    try:
        average_rating(s)
    except Exception as e:
        assert False, f"average_rating crashed with {type(e).__name__}: {e} on input {s!r}"