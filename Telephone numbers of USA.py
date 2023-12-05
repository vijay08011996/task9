def validate_usa_telephone_number(number):
    pattern = r'^\d{10}$'
    return bool(re.match(pattern, number))
