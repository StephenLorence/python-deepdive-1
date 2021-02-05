# goal1

# Goal 1
# Your first task is to create iterators for each of the four files that contained cleaned up data,
# of the correct type (e.g. string, int, date, etc), and represented by a named tuple.

# For now these four iterators are just separate, independent iterators.

from goal1functions import *
import itertools
import os

# Find path to data directory.
data_directory = os.path.abspath('.\\project_4_description')

# Generate absolute file paths for source files.
employment = os.path.join(data_directory, 'employment.csv')
personal_info = os.path.join(data_directory, 'personal_info.csv')
update_status = os.path.join(data_directory, 'update_status.csv')
vehicles = os.path.join(data_directory, 'vehicles.csv')

# Create (lazy) iterators of cleaned data from each source file.
# Each row returned will be in an appropriately formatted
# named tuple.
employment_rows = parse_csv(employment) # Create employment iterator.
personal_info_rows = parse_csv(personal_info) # Create personal info iterator.
update_status_rows = parse_csv(update_status) # Create update status iterator.
vehicles_rows = parse_csv(vehicles) # Create vehicles iterator.

rows_list = [employment_rows, personal_info_rows, update_status_rows, vehicles_rows]


for item in rows_list:
    for row in itertools.islice(item, 0, 5):
        print(row)

# employment:
# ['employer', 'department', 'employee_id', 'ssn']
# ['Stiedemann-Bailey', 'Research and Development', '29-0890771', '100-53-9824']
#           str                     str                 int             int

# personal_info:
# ['ssn', 'first_name', 'last_name', 'gender', 'language']
# ['100-53-9824', 'Sebastiano', 'Tester', 'Male', 'Icelandic']
#        int            str         str     str         str

#update_status:
# ['ssn', 'last_updated', 'created']
# ['100-53-9824', '2017-10-07T00:14:42Z', '2016-01-24T21:19:30Z']
#       int             datetime                    datetime

# vehicles:
# ['ssn', 'vehicle_make', 'vehicle_model', 'model_year']
# ['100-53-9824', 'Oldsmobile', 'Bravada', '1993']
#       int             str         str      int