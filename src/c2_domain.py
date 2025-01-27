import requests
from helpers.writer import write_intel_data
from urllib.parse import urlparse
import re

def get_c2_domains():
    '''
    Get C2 domains from https://threatfox.abuse.ch/export/csv/urls/recent/
    '''
    
    url = 'https://threatfox.abuse.ch/export/csv/urls/recent/'
    response = requests.get(url)
    if response.status_code == 200:
        # Extract all C2 domains using urlparse
        domains = set()
        
        lines = response.text.splitlines()
        
        for line in lines:
            if line.count(',') > 2:
                try:
                    domain = urlparse(line.split(',')[2].replace('"', '')).netloc
                    
                    if domain and not domain[-1].isdigit():
                        domains.add(domain)
                except Exception:
                    pass
                
        filename = "c2_domains.csv"
        write_intel_data(filename, list(domains))
