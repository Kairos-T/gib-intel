import os
from helpers.config import file_columns, tmp_dir


# Initialise CSV files with column headers if they don't already exist.
for filename, columns in file_columns.items():
    filepath = os.path.join(tmp_dir, filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(','.join(columns) + '\n')
            
print("Step 1/2 completed successfully.")
print("Please create lookup tables and definitions in Splunk before running the main.py script.")
