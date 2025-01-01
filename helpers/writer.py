import os


def write_intel_data(filename, columns, data):
    '''
    Writes the various threat intel data to a CSV file

    Parameters:
    - filename: The name of the file to write to, including the path (e.g., 'data/phishing_domains.csv')
    - columns: The columns of the CSV file (e.g., ['url', 'domain'])
    - data: The data to write to the CSV file (e.g., ["https://example.com,example.com", "https://example2.com,example2.com"])
    '''

    # Ensure directory exists
    filename = os.path.join('data', filename)
    directory = os.path.dirname(filename)
    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # Write data to CSV
    with open(filename, 'w') as f:
        f.write(','.join(columns) + '\n')
        for line in data:
            f.write(line + '\n')
