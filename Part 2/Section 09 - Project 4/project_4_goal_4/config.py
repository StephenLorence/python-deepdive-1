# config

import os

# Find path to data directory.
data_directory = os.path.abspath('.\\project_4_description')

# Generate absolute file paths for source files.
employment = os.path.join(data_directory, 'employment.csv')
personal_info = os.path.join(data_directory, 'personal_info.csv')
update_status = os.path.join(data_directory, 'update_status.csv')
vehicles = os.path.join(data_directory, 'vehicles.csv')