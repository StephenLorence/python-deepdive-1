# goal4

# Goal 4
# Find the largest group of car makes for each gender.

# Possibly more than one such group per gender exists (equal sizes).
    # Female -> Ford and Chevrolet (42 in each)
    # Male -> Ford (40)

from config import *
from goalfunctions import *
import itertools

# Create (lazy) iterators of cleaned data from each source file.
# Each row returned will be in an appropriately formatted
# named tuple.
employment_rows = parse_csv(employment) # Create employment iterator.
personal_info_rows = parse_csv(personal_info) # Create personal info iterator.
update_status_rows = parse_csv(update_status) # Create update status iterator.
vehicles_rows = parse_csv(vehicles) # Create vehicles iterator.

# Group each iterator into a list.
rows_list = [personal_info_rows, employment_rows, update_status_rows, vehicles_rows]

# Line up the iterators so that each named tuple in the list has the same serial number.
filtered_rows = align_ssns(*rows_list)

# Iterate through the filtered tuple of named tuples and convert each tuple into a single,
# combined 'Employee' named tuple. Return an iterator of all combined named tuples.
employee_tuples = (create_combined_namedtuple(dict_from_namedtuples(row)) for row in filtered_rows)

# Filter the list of employee tuples and remove any records that haven't been updated since
# before 03/01/2017.
fresh_employees = filter(lambda x: x.last_updated.date() >= datetime.date(2017, 3, 1), employee_tuples)

# Create two copies of the combined employee data so we can iterate through each one.
employee_copies = itertools.tee(fresh_employees, 2)

# Generate a list of vehicle makes for each gender, sorted by how many times
# that vehicle make is associated with that gender in the source data.
for gender, iterator in zip(('Male', 'Female'), employee_copies):
    print(f'{gender} vehicles:')
    vehicles = group_data(iterator, gender)
    for v in vehicles:
        print(v)
    print()





# # # Create two copies of the filtered employee iterator: one to be used in each of the
# # # following filters.
# tee_employees = itertools.tee(fresh_employees, 2)

# # Create two groups: one for male employees and one for female employees.
# male_employees = filter(lambda x: x.gender == 'Male', tee_employees[0])
# female_employees = filter(lambda x: x.gender == 'Female', tee_employees[1])

# # Sort the male employees by vehicle make.
# sorted_data_m = sorted(male_employees, key=group_key)
# # Group the sorted male employees by vehicle make.
# groups_m = itertools.groupby(sorted_data_m, key=group_key)
# group_m_counts = ((g[0], len(list(g[1]))) for g in groups_m)
# print('group m')
# for row in group_m_counts:
#     print(row)

# print()
# # Sort the female employees by vehicle make.
# sorted_data_f = sorted(female_employees, key=group_key)
# # Group the sorted female employees by vehicle make.
# groups_f = itertools.groupby(sorted_data_f, key=group_key)
# group_f_counts = ((g[0], len(list(g[1]))) for g in groups_f)
# print('group f')
# for row in group_f_counts:
#     print(row)

# # Find the vehicle make (or makes) with the highest representation among male...
# print('Male employees:')
# find_max_makes(count_makes(male_employees))
# print('\n')

# # ...and female employees.
# print('Female employees:')
# find_max_makes(count_makes(female_employees))
