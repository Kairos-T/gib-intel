from helpers.config import ioc_list
from helpers.writer import write_intel_data

def get_phishing_iocs():
    '''
    Get phishing IOCs from the configuration file
    '''
    filename = "phishing_iocs.csv"
    write_intel_data(filename, ioc_list)
    
