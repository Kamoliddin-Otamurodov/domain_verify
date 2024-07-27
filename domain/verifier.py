import requests


def check_domain(domain: str) -> str:
    url = f"https://api.domainsdb.info/v1/domains/search?domain={domain}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if 'domains' in data and data['domains']:
            return f"Domain {domain} is registered."
        else:
            return f"Domain {domain} is available."
    else:
        return f"Domain {domain} is available."
    
