def calculate_days_passed(birthday_str): # The year is the last 4 characters of the string "DD-MM-YYYY"
    birth_year = int(birthday_str[6:])
    current_year = 2026  # We only count "whole years" between the birth year and current year
    whole_years = (current_year - birth_year) - 1

    if whole_years < 0: #     # If I was born last year or this year, whole_years might be 0 or negative
        whole_years = 0

    days_passed = whole_years * 365

    return days_passed



my_bday = "02-02-2006"
print(f"Total days in whole years: {calculate_days_passed(my_bday)}")