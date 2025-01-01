from src import phishing

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
