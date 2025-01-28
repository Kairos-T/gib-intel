from helpers.query import query, get_sequences
from helpers.writer import write_intel_data
import tldextract

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
    
    result = query('attacks/phishing_group')

    if result.get('count', 0) != 0:
        return parse_phishing_domains(result)
