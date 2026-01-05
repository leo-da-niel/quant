def year_fraction(start, end, convention="ACT/360"):
    days = (end - start).days

    if convention == "ACT/360":
        return days / 360.0
    elif convention == "ACT/365":
        return days / 365.0
    else:
        raise ValueError("Unsupported day count")
