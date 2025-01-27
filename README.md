# gib-intel

Threat intel gatherer from Group IB's API and other tools, for integration with Splunk

## Features

- Fetches the following pieces of information:
  | Name | Description | Source |
  |------|-------------|--------|
  | Phishing Domains / URLs | Domains / URLs associated with phishing campaigns | Group IB |
  | Typosquatting Domains | Domains that are similar to popular domains | ail-typo-squatting |
  | Web Defacements | URLs have been reported as defaced | Group IB |
  | Bad Bots | User agents that are associated with malicious activity | nginx-ultimate-bad-bot-blocker |
  | C2 IPs | IPs associated with C2 servers | criminalip C2-Daily-Feed |
  | C2/Malware Domains | Domains associated with C2 servers or malware | threatfox |
- Integrates with Splunk Lookup Tables

## Setup

1. Clone the repository
   ```bash
   git clone https://github.com/Kairos-T/gib-intel
   ```
2. Install the required packages
   ```bash
    pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory of the repository with the following content:
   ```env
   GROUPIB_USERNAME = <Group IB Username>
   GROUPIB_API_KEY = <Group IB API Key>
   TENANT_NAME = <Desired Tenant Name>
   ```
4. Run `setup.py` to create the necessary directories and files
   ```bash
   python setup.py
   ```
5. Create Splunk Lookup Tables and Definitions based on the files created in the `data/` directory from the previous step
6. Edit [`config.py`](/helpers/config.py) based on your requirements
7. Run the script
   ```bash
   python main.py
   ```
8. Optionally, set up a scheduled task to run the script at regular intervals
