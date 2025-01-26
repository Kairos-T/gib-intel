import requests
import re
from helpers.writer import write_intel_data
from helpers.config import additional_list

def get_bad_bots():
    '''
    Get bad bots from https://badbot.org/
    '''
    results = []
    for ua in additional_list:
        results.append(ua)

    url = 'https://badbot.org/'
    response = requests.get(url)
    if response.status_code == 200:
        # Extract all user agent strings using regex
        pattern = r"<dt>User Agent String</dt>\s*<dd><code>(.*?)</code></dd>"
        user_agents = re.findall(pattern, response.text, re.DOTALL)

        if user_agents:
            for user_agent in user_agents:
                results.append(user_agent)
                
            filename = "bad_bots.csv"
            write_intel_data(filename, results)
            
