import os
from src import phishing
from helpers.config import file_columns, dir


def init_files():
    '''
    Initialize CSV files with column headers if they don't already exist.
    '''
    for filename, columns in file_columns.items():
        filepath = os.path.join(dir, filename) 
        if not os.path.exists(filepath):  
            with open(filepath, 'w') as f:
                f.write(','.join(columns) + '\n')  
    
def main():
    intel_streams = {
        "phishing_domains": phishing.get_phishing_domains,
    }

    for stream_name, func in intel_streams.items():
        try:
            func()
            # TODO: Proper logging
            print(f"Successfully processed: {stream_name}")
        except Exception as e:
            print(f"Failed to process {stream_name}: {e}")


if __name__ == "__main__":
    main()
