import os
import pandas as pd
from helpers.config import splunk_dir
from utils.logger import log

def write_intel_data(filename, data):
    '''
    Appends data to a CSV file and removes duplicates.

    Parameters:
    - filename: The name of the file to write to, including the path (e.g., 'data/phishing_domains.csv')
    - data: The data to append to the CSV file (e.g., ["https://example.com,example.com", "https://example2.com,example2.com"])
    '''

    # Check if directory and file exists, if it does not exist, set up was not done correctly.
    filename = os.path.join(splunk_dir, filename)
    directory = os.path.dirname(filename)

    if not os.path.exists(directory) or not os.path.exists(filename):
        raise FileNotFoundError(
            f"Directory or file does not exist: {directory} or {filename}. Set up was done incorrectly. Exiting.")

    # Append data to CSV
    with open(filename, 'a') as f:
        for line in data:
            try:
                f.write(line + '\n')
            except Exception as e:
                if "typosquatting" not in filename:
                    log("warning", f"Error writing {line} to file: {e}")
                pass

    # Clean up CSV by removing duplicates
    try:
        df = pd.read_csv(filename)
        df.drop_duplicates(inplace=True)
        df.to_csv(filename, index=False)
    except Exception as e:
        log("error", f"Error cleaning up CSV: {e}")
        pass
