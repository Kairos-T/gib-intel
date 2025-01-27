import requests
import datetime
import ipaddress
from helpers.writer import write_intel_data
from utils.logger import log

def get_c2_ips():
    '''
    Get C2 IPs from the daily feed.
    '''
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    
    # Function to fetch C2 IPs for a given date
    def fetch_c2_ips(date):
        url = f'https://raw.githubusercontent.com/criminalip/C2-Daily-Feed/refs/heads/main/{date}.csv'
        response = requests.get(url)
        
        if response.status_code == 200:
            ips = set()
            lines = response.text.splitlines()
            
            for line in lines:
                try:
                    ip = line.split(',')[0].strip()  
                    if ip:
                        try:
                            ipaddress.ip_address(ip)
                            ips.add(ip)  
                        except ValueError:
                            pass
                except Exception as e:
                    log("error", f"Error processing line: {line}. Error: {e}")
            
            return ips
        else:
            return None

    ips = fetch_c2_ips(today)
    
    if ips is None:
        ips = fetch_c2_ips(yesterday)
    
    if ips is not None:
        filename = "c2_ips.csv"
        write_intel_data(filename, list(ips))
    else:
        log("error", "Failed to get C2 IPs from the source for both today and yesterday.")

