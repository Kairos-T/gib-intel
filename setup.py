import os
from helpers.config import GROUPIB_USERNAME, GROUPIB_API_KEY, TENANT_NAME, file_columns, local_dir
from utils.logger import log

# Check if environment variables are set
if not GROUPIB_USERNAME or not GROUPIB_API_KEY or not TENANT_NAME:
    log("error", "Environment variables are not set. Set up the .env file before running this script. Exiting...")    
    exit()

# Initialise CSV files with column headers if they don't already exist.
for filename, columns in file_columns.items():
    filepath = os.path.join(local_dir, filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(','.join(columns) + '\n')

log("info", "Step 1/2 completed successfully.")
log("info", "Please create lookup tables and definitions in Splunk before running the main.py script.")
