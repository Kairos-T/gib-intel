import os
from helpers.config import file_columns, dir


# Initialise CSV files with column headers if they don't already exist.
for filename, columns in file_columns.items():
    filepath = os.path.join(dir, filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(','.join(columns) + '\n')
