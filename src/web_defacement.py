from helpers.query import query, get_sequences
from helpers.writer import write_intel_data
from datetime import datetime, timedelta
from helpers.config import TENANT_NAME

def parse_web_defacement(result):
    '''
    Parse web defacement data from Group-IB API response and write to a CSV file.

    Parameters:
    - result: The result of the `get_web_defacement()` query in JSON format
    '''
    print(result)
    urls = [item['siteUrl']
            for item in result['items']]  # Extract URLs from API response
    data = []

    for url in urls:
        if TENANT_NAME in url: # Check if defaced website belongs to the client
            data.append(url)

    filename = "web_defacements.csv"

    write_intel_data(filename, data)
    
def get_web_defacement_domains():
    '''
    Get web defacement domains and their associated information from Group-IB API
    '''
    current_date = datetime.now()

    sequence = get_sequences(current_date.strftime(format='%Y-%m-%d'))['attacks/deface']
    
    while True:
        result = query('attacks/deface/updated' +
                       "?seqUpdate=" + str(sequence))

        if result.get('count', 0) != 0:
            return parse_web_defacement(result)

        # If count is 0, decrease the date by 1 day and get the new sequence 
        # This usually would not happen as the script is run daily
        current_date -= timedelta(days=1)
        sequence = get_sequences(current_date.strftime(format='%Y-%m-%d'))['attacks/deface']
    
