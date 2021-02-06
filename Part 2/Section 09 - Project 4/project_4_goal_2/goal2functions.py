# goal2functions

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
    filename = clean_filename(csv_file)
    csv_iter = csv_iterator(csv_file)
    header_row = next(csv_iter)
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




# Take in a variable number of iterables of named tuples and
# align them based on the ssn value of each named tuple.
'''
def align_all_rows(*args):
    args = [list(arg) for arg in args]
    index = 0
    # Set the iterable against which to align the others.
    primary = args[0]
    # Create the list to build onto. Initially it will just
    # be equal to the first iterable.
    final_list = primary
    # Iterate once for each iterable passed in.
    while index < len(args)-1:
        results = []
        # Grab the next iterable in line to search through.
        secondary = args[index+1]
        for p in primary:
            for s in secondary:
                # Find the row in the secondary iterable that
                # has the same ssn as the given row in the primary
                # iterable, then tack that row onto the result list.
                if s.ssn == p.ssn:
                    results.append(s)
                    break
        # Initially we can just zip the two sets of named tuples.
        if index == 0:
            final_list = list(zip(final_list, results))
        # Once the elements in the list are themselves lists, we
        # need to get fancier in order to extend each sub-list with
        # the new aligned named tuple.
        else:
            new_list = []
            for a, b in zip(final_list, results):
                # Unpack each neamed tuple from the previous list,
                # then add the new named tuple to the end.
                new_list.append([*a, b])
            final_list = new_list
        index += 1
    yield from final_list
'''