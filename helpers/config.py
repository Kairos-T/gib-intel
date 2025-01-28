#########################
# Global Configurations #
#########################

import os
from dotenv import load_dotenv
from pathlib import Path

# API credentials
load_dotenv(Path('.') / '.env')
GROUPIB_USERNAME = os.getenv('GROUPIB_USERNAME')
GROUPIB_API_KEY = os.getenv('GROUPIB_API_KEY')
TENANT_NAME = os.getenv('TENANT_NAME')

# Output directory for generated files
local_dir = "data/"
splunk_dir = "C:/Program Files/Splunk/etc/apps/search/lookups"
# splunk_dir = "data/"

# Retries and timeout for API requests
retries = 5
delay = 5

# Default filenames and columns for CSV files
file_columns = {
    "phishing_domains.csv": ["domain"],
    "typosquatting_domains.csv": ["domain"],
    "phishing_ioc.csv": ["ioc"],
    "web_defacements.csv": ["url", "first_seen"],
    "bad_bots.csv": ["bad_bot"],
    "c2_domains.csv": ["domain"],
    "c2_ips.csv": ["ip"]
    }

##################################
# Module Specific Configurations #
##################################

# typosquatting.py
resolve_dns = False

# phishing_ioc.py
ioc_list = ["Request", "Follow up", "Urgent", "Important", "Are you available?", "Are you at your desk?", "Payment Status", "Hello", "Purchase", "Invoice Due", "Re:", "Direct Deposit", "Expenses", "Payroll", "Install", "Security alert", "Suspend"]

# bad_bots.py
additional_list = ["sqlmap/1.6.4#stable+(https://sqlmap.org)", "dirbuster", "dirb"]
