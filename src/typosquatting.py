import dns.resolver
import math
from ail_typo_squatting import runAll
from helpers.config import resolve_dns, TENANT_NAME
from helpers.writer import write_intel_data
from utils.logger import log


def get_typosquatting_domains():
    results = []
    domain = TENANT_NAME
    formatoutput = "text"
    results = runAll(
        domain=domain,
        limit=math.inf,
        formatoutput=formatoutput,
        pathOutput=None,
        verbose=False,
        givevariations=False,
        keeporiginal=False
    )
    if resolve_dns:
        for url in results:
            # check if there is a dns record for the domain
            try:
                dns.resolver.resolve('url')
            except Exception as e:
                log("info", f"Potential typosquatting url {url} does not have a DNS record: {e}")
                results.remove(url)

    filename = "typosquatting_domains.csv"
    write_intel_data(filename, results)
