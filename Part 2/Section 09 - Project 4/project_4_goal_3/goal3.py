# goal3

# Goal 3
# Next, you want to identify any stale records, where stale simply means
# the record has not been updated since 3/1/2017 (e.g. last update date 
# < 3/1/2017). Create an iterator that only contains current records (i.e.
# not stale) based on the last_updated field from the status_update file.

from goal3functions import *
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

for item in itertools.islice(fresh_employees, 0, 20):
    print(item)

# Employee(ssn=100539824, first_name='Sebastiano', last_name='Tester', gender='Male', language='Icelandic', employer='Stiedemann-Bailey', department='Research and Development', employee_id=290890771, last_updated=datetime.datetime(2017, 10, 7, 0, 14, 42), created=datetime.datetime(2016, 1, 24, 21, 19, 30), vehicle_make='Oldsmobile', vehicle_model='Bravada', model_year=1993), 
# Employee(ssn=101714702, first_name='Cayla', last_name='MacDonagh', gender='Female', language='Lao', employer='Nicolas and Sons', department='Sales', employee_id=416841359, last_updated=datetime.datetime(2017, 1, 23, 11, 23, 17), created=datetime.datetime(2016, 1, 27, 4, 32, 57), vehicle_make='Ford', vehicle_model='Mustang', model_year=1997), 
# Employee(ssn=101840356, first_name='Nomi', last_name='Lipprose', gender='Female', language='Yiddish', employer='Connelly Group', department='Research and Development', employee_id=987952860, last_updated=datetime.datetime(2017, 10, 4, 11, 21, 30), created=datetime.datetime(2016, 9, 21, 23, 4, 7), vehicle_make='GMC', vehicle_model='Yukon', model_year=2005), 
# Employee(ssn=104220928, first_name='Justinian', last_name='Kunzelmann', gender='Male', language='Dhivehi', employer='Upton LLC', department='Marketing', employee_id=569817552, last_updated=datetime.datetime(2017, 3, 28, 12, 38, 29), created=datetime.datetime(2016, 4, 15, 11, 37, 17), vehicle_make='Oldsmobile', vehicle_model='Intrigue', model_year=2000), 
# Employee(ssn=104847144, first_name='Claudianus', last_name='Brixey', gender='Male', language='Afrikaans', employer='Zemlak-Olson', department='Business Development', employee_id=462886707, last_updated=datetime.datetime(2018, 2, 19, 1, 34, 33), created=datetime.datetime(2016, 3, 15, 14, 7, 57), vehicle_make='Ford', vehicle_model='Crown Victoria', model_year=2008)]