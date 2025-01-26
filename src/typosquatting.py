import dns.resolver
import math
import chardet
from ail_typo_squatting import runAll
from helpers.config import resolve_dns, TENANT_NAME
from helpers.writer import write_intel_data
from utils.logger import log


def get_typosquatting_domains():
    results = []
    clean_results = []
    domain = TENANT_NAME
    formatoutput = "text"
    results = runAll(
        domain=domain,
        limit=math.inf,
        formatoutput=formatoutput,
        pathOutput=None,
        verbose=False,
        givevariations=False,
        keeporiginal=False,
    )
    
    for url in results:
        if chardet.detect(url.encode())["encoding"] == "ascii":
            clean_results.append(url)

    if resolve_dns:
        for url in clean_results:
        # check if there is a dns record for the domain
            try:
                dns.resolver.resolve(url, "A")
            except Exception as e:
                log(
                    "info",
                    f"Potential typosquatting url {url} does not have a DNS record: {e}",
                    )
                clean_results.remove(url)
    
    clean_results = clean_results[:100] # Limit to 100 results for POC
    
    filename = "typosquatting_domains.csv"
    write_intel_data(filename, clean_results)
