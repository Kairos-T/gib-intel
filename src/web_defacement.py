from helpers.query import query, get_sequences
from helpers.writer import write_intel_data
from helpers.config import TENANT_NAME
from utils.logger import log

def parse_web_defacement(result):
    '''
    Parse web defacement data from Group-IB API response and write to a CSV file.

    Parameters:
    - result: The result of the `get_web_defacement()` query in JSON format
    '''
    urls = [item['siteUrl']
            for item in result['items']]  # Extract URLs from API response
    data = []

    for url in urls:
        log("info", f"Web defacement URL Detected: {url}")
        if TENANT_NAME in url: # Check if defaced website belongs to the client
            data.append(url)

    filename = "web_defacements.csv"

    write_intel_data(filename, data)
    
def get_web_defacement_domains():
    '''
    Get web defacement domains and their associated information from Group-IB API
    '''
    result = query('attacks/deface')

    if result.get('count', 0) != 0:
        return parse_web_defacement(result)
