import os
import pandas as pd
from helpers.config import dir

def write_intel_data(filename, data):
    '''
    Appends data to a CSV file and removes duplicates.

    Parameters:
    - filename: The name of the file to write to, including the path (e.g., 'data/phishing_domains.csv')
    - data: The data to append to the CSV file (e.g., ["https://example.com,example.com", "https://example2.com,example2.com"])
    '''

    # Ensure directory exists
    filename = os.path.join(dir, filename)
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Append data to CSV
    with open(filename, 'a') as f:
        for line in data:
            f.write(line + '\n')

    # Clean up CSV by removing duplicates
    df = pd.read_csv(filename)
    df.drop_duplicates(inplace=True)
    df.to_csv(filename, index=False)
