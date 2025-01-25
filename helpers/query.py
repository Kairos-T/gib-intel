import requests
import time
from requests.auth import HTTPBasicAuth
from helpers.config import GROUPIB_USERNAME, GROUPIB_API_KEY, retries, delay
from utils.logger import log

def get_sequences(date_time):
    '''
    Get sequence number for each feed (Get feed info for each day only, as this script is run daily)

    Parameters:
    - date_time: The date to query in the format 'YYYY-MM-DD'

    Returns:
    - sequences: The sequence numbers for each feed
    '''
    url = f'https://tap.group-ib.com/api/v2/sequence_list?date={date_time}'
    response = requests.get(url, auth=HTTPBasicAuth(
        GROUPIB_USERNAME, GROUPIB_API_KEY))
    try:
        sequences = response.json()['list']
    except KeyError as e:
        return None
    return sequences

def query(feed):
    '''
    Query Group-IB API for a specific feed with retry logic.

    Parameters:
    - feed: The feed to query
    - retries: The maximum number of retry attempts (default: 5)
    - delay: The delay between retries in seconds (default: 2)

    Returns:
    - results: The results of the query in JSON format if successful
    '''
    if not GROUPIB_USERNAME or not GROUPIB_API_KEY:
        log("error", "Group-IB username and/or API key not found")
        return
        
    url = f'https://tap.group-ib.com/api/v2/{feed}'

    for attempt in range(retries):
        try:
            response = requests.get(url, auth=HTTPBasicAuth(
                GROUPIB_USERNAME, GROUPIB_API_KEY))
            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as e:
            log("error", f"Attempt {attempt + 1} of {retries} failed: {e}")

            if attempt < retries - 1:
                time.sleep(delay)
            else:
                raise

        except ValueError as e:
            log("error", f"Error decoding JSON: {e}")
            raise
