def parse_seat(seat):
    """
    Parses a seat string (e.g., 'H12') into a tuple (row, seat_number).
    Defensively validates type, non-emptiness, row letter, and positive numeric seat number.
    Returns (row, seat_number) if valid, or None if invalid.
    """
    if not isinstance(seat, str):
        return None
    seat = seat.strip()
    if not seat or len(seat) < 2:
        return None
    row = seat[0]
    if not row.isalpha():
        return None
    seat_num_str = seat[1:]
    if not seat_num_str.isdigit():
        return None
    seat_num = int(seat_num_str)
    if seat_num <= 0:
        return None
    return row.upper(), seat_num


def total_price(prices_csv):
    """
    Computes total price including 18% GST from a comma-separated string of prices.
    Defensively handles None, empty strings, malformed tokens, and negative values.
    Returns rounded total or 0.0 if no valid prices are present.
    """
    if not isinstance(prices_csv, str):
        return 0.0
    prices_csv = prices_csv.strip()
    if not prices_csv:
        return 0.0
    prices = []
    for p in prices_csv.split(','):
        p_clean = p.strip()
        if p_clean.isdigit():
            prices.append(int(p_clean))
        else:
            try:
                val = float(p_clean)
                if val >= 0:
                    prices.append(val)
            except (ValueError, TypeError):
                continue
    if not prices:
        return 0.0
    return round(sum(prices) * 1.18, 2)


def average_rating(ratings):
    """
    Computes average rating from space-separated numeric ratings.
    Defensively handles None, empty strings, non-numeric tokens, and prevents ZeroDivisionError.
    Returns rounded average rating (1 decimal place) or 0.0 if empty.
    """
    if not isinstance(ratings, str):
        return 0.0
    ratings = ratings.strip()
    if not ratings:
        return 0.0
    values = []
    for r in ratings.split():
        r_clean = r.strip()
        try:
            val = float(r_clean)
            if val >= 0:
                values.append(val)
        except (ValueError, TypeError):
            continue
    if not values:
        return 0.0
    return round(sum(values) / len(values), 1)


def main():
    print("==== Running parse_seat ====")
    user_input = input("Enter a seat number (e.g. H12): ")
    result = parse_seat(user_input)
    print("Row and Seat:", result)

    print("\n==== Running total_price ====")
    user_input = input("Enter ticket prices as CSV (e.g. 150,250,400): ")
    result = total_price(user_input)
    print("Total with GST:", result)

    print("\n==== Running average_rating ====")
    user_input = input("Enter ratings separated by spaces (e.g. 4 5 3): ")
    result = average_rating(user_input)
    print("Average Rating:", result)


if __name__ == "__main__":
    main()