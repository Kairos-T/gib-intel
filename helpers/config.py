#########################
# Global Configurations #
#########################

# Output directory for generated files
tmp_dir = "data/"
# dir = "C:/Program Files/Splunk/etc/apps/search/lookups"
dir = "data/"

# Default filenames and columns for CSV files
file_columns = {
    "phishing_domains.csv": ["Domain"],
    "typosquatting_domains.csv": ["Domain"]}

##################################
# Module Specific Configurations #
##################################

# typosquatting.py
resolve_dns = False
