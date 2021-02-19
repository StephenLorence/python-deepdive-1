# goalfunctions

import csv
import itertools
from collections import namedtuple
from collections import defaultdict
import datetime

# Iteration functions.
def csv_iterator(csv_file):
    with open(csv_file) as f:
        rows = csv.reader(f)
        yield from rows

# Functions to clean input data.

# Convert string to integer.
def clean_int(string):
    return int(string.replace('-', ''))

# Convert string to datetime object.
def clean_datetime(string):
    return datetime.datetime.strptime(string, '%Y-%m-%dT%H:%M:%SZ')

# Parse file name from file path.
def clean_filename(csv_file):
    return csv_file.split('\\')[-1].rpartition('.csv')[0]

# Parse row from employment file.
# Output should be: string, string, int, int
def clean_employment_row(lst):
    return [lst[0], lst[1], clean_int(lst[2]), clean_int(lst[3])]

# Parse row from personal_info file.
# Output should be: int, str, str, str, str
def clean_personal_info_row(lst):
    return [clean_int(lst[0]), lst[1], lst[2], lst[3], lst[4]]
    
# Parse row from update_status file.
# Output should be: int, datetime, datetime
def clean_update_status_row(lst):
    return [clean_int(lst[0]), clean_datetime(lst[1]), clean_datetime(lst[2])]

# Parse row from vehicles file.
# Output should be: int, str, str, str
def clean_vehicles_row(lst):
    return [clean_int(lst[0]), lst[1], lst[2], clean_int(lst[3])]

# Create namedtuple class from header row.
def create_namedtuple_from_csv_iterator(csv_file):
    # Grab the file name from the file path.
    filename = clean_filename(csv_file)
    # Create an iterator from the file.
    csv_iter = csv_iterator(csv_file)
    # Grab the header row from the iterator.
    header_row = next(csv_iter)
    # Create the namedtuple class using the file name
    # as the class name and the header row as the fields.
    return namedtuple(filename, header_row)

# Convert csv file into namedtuple rows.
def parse_csv(csv_file):
    # Create dictionary pairing filenames with the
    # correct function to clean rows in that file.
    cleaning_dict = {'employment': clean_employment_row,
                     'personal_info': clean_personal_info_row,
                     'update_status': clean_update_status_row,
                     'vehicles': clean_vehicles_row}
    # Grab filename (minus '.csv') from file path.
    filename = clean_filename(csv_file)
    # Create namedtuple class.
    nt_class = create_namedtuple_from_csv_iterator(csv_file)
    # Convert the remaining rows in the file into namedtuples.
    # Apply correct row formatting based on file name.
    csv_iter = csv_iterator(csv_file) # Create the iterator.
    next(csv_iter) # Skip the header row.
    # Clean each row using the row cleaning function
    # specific to the filename.
    cleaned_tuples = (nt_class( # Create a named tuple out of...
                                *cleaning_dict[filename](row)) # the unpacked list of cleaned data...
                                for row in csv_iter) # from each row in the file.
    yield from cleaned_tuples

# Take in a tuple containing multiple namedtuple objects,
# then convert each namedtuple into a dictionary, then
# combine each dictionary into one new dictionary and
# output that new dictionary. 
def dict_from_namedtuples(tuple_gen):
    # Create a generator of dictionaries from the tuple.
    dic_gen = (nt._asdict() for nt in tuple_gen)
    # Create an empty dictionary to add into.
    dic = {}
    # Iterate through each dictionary in the generator
    # and add to the key:value pairs in the consolidated
    # dictionary.
    for item in dic_gen:
        dic = {**dic, **item}
    return dic

# Create a named tuple to represent the employee based on
# the combined dictionary of elements from each individual
# named tuple.
def create_combined_namedtuple(dic):
    Employee = namedtuple('Employee',dic.keys())
    employee = Employee(*dic.values())
    return employee

# Take in two iterables of named tuples and align the second
# iterable's contents to line up with the contents of the first
# iterable based on the ssn of each named tuple.
def find_ssn(primary, secondary):
    results = []
    for p in primary:
        for s in secondary:
            # Find the row in the secondary iterable that
            # has the same ssn as the given row in the primary
            # iterable, then tack that row onto the result list.
            if s.ssn == p.ssn:
                results.append(s)
                break
    return results

# Take in multiple iterables and align the contents of each
# iterable to match the order of the first iterable provided,
# based on the ssn of each named tuple in each iterable.
def align_ssns(*args):
    # Make sure each iterable is a list because we'll be
    # running through them multiple times, so an iterator
    # would be exhausted.
    args = [list(arg) for arg in args]
    # Split the arguments into the primary iterable and
    # the list of secondary iterables.
    primary, *secondaries = args
    aligned_rows = []
    # For each iterable in the 'secondaries' list, run the
    # iterable through the 'find_ssn' function, comparing
    # against the primary iterable.
    for secondary in secondaries:
        aligned_rows.append(find_ssn(primary, secondary))
    yield from (zip(primary, *aligned_rows))

'''
# Create a dictionary containing vehicle makes and a count
# of how many times those makes are represented in the given
# iterable.
def count_makes(iter):
    # Create a defaultdict that will return a value of 0 when
    # provided with a key that doesn't exist in the dictionary.
    vehicle_dict = defaultdict(int)
    # Run through the iterable and add 1 to the value of the
    # given vehicle make for each named tuple.
    for emp in iter:
        vehicle_dict[emp.vehicle_make] += 1
    return vehicle_dict

# Take in a dictionary of vehicle makes and counts. Return the
# vehicle make (or makes) with the single highest count, then
# print out the make(s) and the count.
def find_max_makes(dictionary):
    # Look through the dictionary and return the value from the
    # key:value pair with the highest value.
    max_value = max(dictionary.items(), key=lambda x: x[1])[1]
    # Take the maximum value and find all makes with that value
    # in the dictionary. This is to double check whether there are
    # more than one make that share the same high value.
    max_make = [k for k, v in dictionary.items() if v == max_value]
    print(f'  Most popular make(s): {max_make}\n    Quantity: {max_value}')
'''

# Create a group key function for use when sorting and grouping data.
def group_key(item):
    return item.vehicle_make

# Take in the combined employee data, filter it by gender, sort by
# vehicle make, group by vehicle make, 
def group_data(input_data, gender):
    # Filter the employees by gender.
    filtered_employees = filter(lambda x: x.gender == gender, input_data)
    # Sort the employees by vehicle make.
    sorted_data = sorted(filtered_employees, key=group_key)
    # Group the sorted employees by vehicle make.
    groups = itertools.groupby(sorted_data, key=group_key)
    group_counts = ((g[0], len(list(g[1]))) for g in groups)
    yield from sorted(group_counts, key=lambda row: row[1], reverse=True)