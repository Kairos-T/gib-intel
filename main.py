from src import phishing_ioc, phishing, typosquatting, web_defacement
from utils.logger import log

def main():
    intel_streams = {
        "phishing_iocs": phishing_ioc.get_phishing_iocs,
        "phishing_domains": phishing.get_phishing_domains,
        "typosquatting_domains": typosquatting.get_typosquatting_domains,
        "web_defacement": web_defacement.get_web_defacement_domains
    }
    for stream_name, func in intel_streams.items():
        func()
        
    for stream_name, func in intel_streams.items():
        try:
            func()
            log("success", f"Successfully processed: {stream_name}")
        except Exception as e:
            log("error", f"Failed to process {stream_name}: {e}")

if __name__ == "__main__":
    main()
