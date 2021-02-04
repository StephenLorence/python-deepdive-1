# goal1functions

import csv
import itertools
from collections import namedtuple
import datetime

# Iteration functions.
def csv_iterator(csv_file):
    with open(csv_file) as f:
        rows = csv.reader(f)
        yield from rows

# Functions to clean input data.

# Convert string to integer.
def clean_int(string):
    return int(string.strip('-'))

# Convert string to datetime object.
def clean_datetime(string):
    return datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%SZ')

# Parse file name from file path.
def clean_filename(csv_file):
    return csv_file.split('/')[-1].rstrip('.csv')

# Parse row from employment file.
# Output should be: string, string, int, int
def clean_employment_row(lst):
    return [a, b, clean_int(c), clean_int(d) for a, b, c, d in lst]

# Parse row from personal_info file.
# Output should be: int, str, str, str
def clean_personal_info_row(lst):
    return [clean_int(a), b, c, d for a, b, c, d in lst]
    
# Parse row from update_status file.
# Output should be: str, datetime, datetime
def clean_update_status_row(lst):
    return [a, clean_datetime(b), clean_datetime(c) for a, b, c in lst]

# Parse row from vehicles file.
# Output should be: int, str, str, str
def clean_vehicles_row(lst):
    return [clean_int(a), b, c, clean_int(d) for a, b, c, d in lst]

# Create namedtuple class from header row.
def create_namedtuple_from_csv_iterator(csv_file):
    filename = clean_filename(csv_file)
    csv_iter = csv_iterator(csv_file)
    header_row = next(csv_iter)
    return namedtuple(filename, header_row)

# Convert csv file into namedtuple rows.
def parse_csv(csv_file):
    # Grab filename (minus '.csv') from file path.
    filename = clean_filename(csv_file)
    # Create namedtuple class.
    nt_class = create_namedtuple_from_csv_iterator(csv_file)
    # Convert the remaining rows in the file into namedtuples.
    # Apply correct row formatting based on file name.
    csv_iter = csv_iterator(csv_file) # Create the iterator.
    next(csv_iter) #Skip the header row.
    ( for row in csv_iter)

