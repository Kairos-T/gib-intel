import os
from helpers.config import file_columns, tmp_dir
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path('.') / '.env')
GROUPIB_USERNAME = os.getenv('GROUPIB_USERNAME')
GROUPIB_API_KEY = os.getenv('GROUPIB_API_KEY')
TENANT_NAME = os.getenv('TENANT_NAME')

# Check if environment variables are set
if not GROUPIB_USERNAME or not GROUPIB_API_KEY or not TENANT_NAME:
    print("Error: Environment variables are not set. Set up the .env file before running this script. Exiting...")
    exit()

# Initialise CSV files with column headers if they don't already exist.
for filename, columns in file_columns.items():
    filepath = os.path.join(tmp_dir, filename)
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            f.write(','.join(columns) + '\n')
            
print("Step 1/2 completed successfully.")
print("Please create lookup tables and definitions in Splunk before running the main.py script.")
