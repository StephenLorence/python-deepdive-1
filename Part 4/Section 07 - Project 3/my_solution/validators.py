#validators.py

def validate_string(value, name):
    value = str(value)
    if not len(value):
        raise ValueError(f'{name} must not be empty.')
    return value

def validate_integer(value: int, zero_allowed=False):
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

def validate_hdd_form_factor(value):
    if str(value).strip('"') not in ['2.5', '3.5']:
        raise ValueError('Form factor must be either 2.5" 3.5".or ')
    else:
        return str(value).strip('"') + '"'

def validate_hdd_rpm(value):
    value = validate_integer(value)
    if not (5_000 <= value <= 15_000):
        raise ValueError('RPM must be between 5,000 and 15,000 RPM.')
    if value % 100:
        raise ValueError('RPM must be a multiple of 100.')
    return value

def validate_ssd_interface(value):
    inter_dict = {
        'pcie': 'PCIe',
        'sata': 'SATA',
        'msata': 'mSATA',
        'm.2': 'M.2'
    }
    try:
        return inter_dict[value.lower()]
    except KeyError as ex:
        raise ValueError(f'Interface must be one of the following: {tuple(inter_dict.values())}') from None