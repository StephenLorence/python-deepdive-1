# goal1

# Goal 1
# Your first task is to create iterators for each of the four files that contained cleaned up data,
# of the correct type (e.g. string, int, date, etc), and represented by a named tuple.

# For now these four iterators are just separate, independent iterators.

from goal1functions import *

employment = 'project_4_description/employment.csv'
personal_info = 'project_4_description/personal_info.csv'
update_status = 'project_4_description/update_status.csv'
vehicles = 'project_4_description/vehicles.csv'

employment_tuple = create_namedtuple_from_csv_iterator(employment)

print(employment_tuple('Stiedemann-Bailey', 'Research and Development', '29-0890771', '100-53-9824'))


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
#       str             datetime                    datetime

# vehicles:
# ['ssn', 'vehicle_make', 'vehicle_model', 'model_year']
# ['100-53-9824', 'Oldsmobile', 'Bravada', '1993']
#       int             str         str      int