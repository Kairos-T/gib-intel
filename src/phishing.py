from helpers.query import query, get_sequences
from helpers.writer import write_intel_data
import tldextract
from datetime import datetime, timedelta

def parse_phishing_domains(result):
    '''
    Parse phishing domains from Group-IB API response and write to a CSV file.

    Parameters:
    - result: The result of the `get_phishing_domains()` query in JSON format
    '''
    urls = [item['domain']
            for item in result['items']]  # Extract URLs from API response
    data = []

    for url in urls:
        # Extract the main domain (FQDN) using tldextract
        extracted = tldextract.extract(url)
        # Combine domain and suffix
        domain = f"{extracted.domain}.{extracted.suffix}"
        data.append(url)
        data.append(domain)

    filename = "phishing_domains.csv"

    write_intel_data(filename, data)


def get_phishing_domains():
    '''
    Get phishing domains and their associated information from Group-IB API
    '''
    current_date = datetime.now()
    
    sequence = get_sequences(current_date.strftime(format='%Y-%m-%d'))['attacks/phishing_group']
    
    if sequence:
        while True:
            result = query('attacks/phishing_group/updated' +
                        "?seqUpdate=" + str(sequence))

            if result.get('count', 0) != 0:
                return parse_phishing_domains(result)

            # If count is 0, decrease the date by 1 day and get the new sequence 
            # This usually would not happen as the script is run daily
            current_date -= timedelta(days=1)
            sequence = get_sequences(current_date.strftime(format='%Y-%m-%d'))['attacks/phishing_group']
