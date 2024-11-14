import subprocess
import json
import os

#modules to obtain data about website domain
def whois_lookup(domain):
    try:
        result = subprocess.run(['whois', domain], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return "error"
    
def dnsrecon_lookup(domain):
    try:
        result = subprocess.run(['dnsrecon', '-d', domain, '-j', 'dnsrecon_output.json'], capture_output=True, text=True)

        with open('dnsrecon_output.json', 'r') as f:
            data = json.load(f)

        return data
    except Exception as e:
        return "error"
    
def dnsx_lookup(domain):
    try:
        result = subprocess.run(['dnsx', '-d', domain, '-silent'], capture_output=True, text=True)
        subdomains = result.stdout.strip().split('\n')
        return subdomains
    except Exception as e:
        return "error"