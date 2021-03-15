#validators.py

def validate_string(value, name):
    value = str(value)
    if not len(value):
        raise ValueError(f'{name} must not be empty.')
    return value

def validate_integer(value, zero_allowed=False):
    try:
        value = int(value)
    except ValueError:
        raise TypeError('Value must be an integer.')
    if zero_allowed:
        if value < 0:
            raise ValueError('Value must not be negative.') 
    else:
        if value <= 0:
            raise ValueError('Value must be greater than zero.') 
    return value

