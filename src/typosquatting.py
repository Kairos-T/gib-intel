import dns.resolver
import math
import os
from ail_typo_squatting import runAll
from pathlib import Path
from dotenv import load_dotenv
from helpers.config import resolve_dns
from helpers.writer import write_intel_data

load_dotenv(Path('.') / '.env')
TENANT_NAME = os.getenv('TENANT_NAME')


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
            except:
                results.remove(url)

    filename = "typosquatting_domains.csv"
    write_intel_data(filename, results)
