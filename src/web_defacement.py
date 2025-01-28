from helpers.query import query
from helpers.writer import write_intel_data
from helpers.config import TENANT_NAME
from utils.logger import log

def parse_web_defacement(result):
    '''
    Parse web defacement data from Group-IB API response and write to a CSV file.

    Parameters:
    - result: The result of the `get_web_defacement()` query in JSON format
    '''
    entries = [f"{item['siteUrl']},{item['tsCreate'].replace('T', ' ').strip('Z')}"
            for item in result['items']]  # Extract URLs from API response
    data = []

    for entry in entries:
        log("info", f"Web defacement URL Detected: {entry.replace(',', ' (')})")
        if TENANT_NAME in entry: # Check if defaced website belongs to the client
            data.append(entry)

    filename = "web_defacements.csv"

    write_intel_data(filename, data)
    
def get_web_defacement_domains():
    '''
    Get web defacement domains and their associated information from Group-IB API
    '''
    result = query('attacks/deface')

    if result.get('count', 0) != 0:
        return parse_web_defacement(result)
