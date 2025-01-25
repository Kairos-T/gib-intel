import requests
from helpers.writer import write_intel_data

def get_bad_bots():
    '''
    Get bad bots from https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/refs/heads/master/_generator_lists/bad-user-agents.list
    '''
    url = 'https://raw.githubusercontent.com/mitchellkrogza/nginx-ultimate-bad-bot-blocker/refs/heads/master/_generator_lists/bad-user-agents.list'
    response = requests.get(url)
    bad_bots = response.text
    results = []
    
    for line in bad_bots.splitlines():
        results.append(line)
    
    filename = "bad_bots.csv"
    
    write_intel_data(filename, results)
