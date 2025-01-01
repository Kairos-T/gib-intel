import os
import glob
from src import phishing


def clear_data():
    """
    Deletes all CSV files in the data/ directory.
    """
    data_dir = "data/"
    csv_files = glob.glob(os.path.join(data_dir, "*.csv"))
    for csv_file in csv_files:
        try:
            if "phishing_ioc" in csv_file: # Static IOC file
                continue
            os.remove(csv_file)
            print(f"Deleted: {csv_file}")
        except Exception as e:
            print(f"Failed to delete {csv_file}: {e}")


def main():
    clear_data()
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
