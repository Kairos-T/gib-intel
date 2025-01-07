#########################
# Global Configurations #
#########################

# Output directory for generated files
tmp_dir = "data/"
dir = "C:/Program Files/Splunk/etc/apps/search/lookups"

# Default filenames and columns for CSV files
file_columns = {
    "phishing_domains.csv": ["Domain"],
    "typosquatting_domains.csv": ["Domain"],
    "phishing_iocs.csv": ["ioc"]}

##################################
# Module Specific Configurations #
##################################

# typosquatting.py
resolve_dns = False

# phishing_ioc.py
ioc_list = ["Request", "Follow up", "Urgent", "Important", "Are you available?", "Are you at your desk?", "Payment Status", "Hello", "Purchase", "Invoice Due", "Re:", "Direct Deposit", "Expenses", "Payroll", "Install", "Security alert", "Suspend"]
