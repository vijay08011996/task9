def validate_bangladesh_mobile_number(number):
    pattern = r'^01\d{9}$'
    return bool(re.match(pattern, number))
