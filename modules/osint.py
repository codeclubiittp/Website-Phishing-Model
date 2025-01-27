import requests
import socket
import os
from dotenv import load_dotenv  # Import the dotenv library

class OSINTModule:
    def __init__(self):
        # Load the .env file
        load_dotenv()  # This will load the environment variables from a .env file

    def run(self, target):
        print(f"Performing OSINT on {target}...")
        
        # 1. Fetch DNS information
        try:
            print("\n[+] DNS Records:")
            ip = socket.gethostbyname(target)
            print(f"Target IP: {ip}")
        except socket.gaierror:
            print("[-] Unable to fetch DNS records.")
            return

        # 2. Perform WHOIS Lookup
        try:
            print("\n[+] WHOIS Lookup:")
            whois_url = f"https://api.whoisfreaks.com/v1.0/whois?apiKey=1247a85d57bd4ce3aaffc6dc325d4558&whois=live&domainName={target}"
            #headers = {"Authorization": "3 "}
            response = requests.get(whois_url,)
            print(response)
            if response.status_code == 200:
                whois_data = response.json()
                print(whois_data)
                print(f"Registrar: {whois_data.get('domain_registrar')}")
                print(f"Creation Date: {whois_data.get('create_date')}")
                print(f"Expiration Date: {whois_data.get('expiry_date')}")
            else:
                print("[-] WHOIS lookup failed.")
        except Exception as e:
            print(f"[-] Error during WHOIS lookup: {e}")
        
        # 3. Query Shodan (requires API key)
        try:
            shodan_api_key = os.getenv("SHODAN_API_KEY")  # Load the key from environment variables
            if not shodan_api_key:
                print("[-] SHODAN_API_KEY not found in environment variables.")
                return

            print("\n[+] Shodan Results:")
            # ip ="8.8.8.8"
            shodan_url = f"https://api.shodan.io/shodan/host/{ip}?key={shodan_api_key}"
            response = requests.get(shodan_url)
            if response.status_code == 200:
                shodan_data = response.json()
                print(f"Organization: {shodan_data.get('org')}")
                print(f"Open Ports: {shodan_data.get('ports')}")
            else:
                print("[-] No data from Shodan.")
        except Exception as e:
            print(f"[-] Error querying Shodan: {e}")
