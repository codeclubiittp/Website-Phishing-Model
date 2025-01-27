# Penetration Testing Framework
## **Modules**

1. **Port Scanning**  
   - Utilizes the `nmap` package to perform a TCP SYN (stealthy) scan.  
   - Detects open ports on the target machine.

2. **OSINT (Open Source Intelligence)**  
   - Uses the `socket` package to acquire the IP of the target.  
   - Performs a WHOIS lookup using the WhoisFreaks API.  
   - Retrieves open ports and organizational details using the Shodan API.

3. **Brute Force Attack**  
   - Tries a list of passwords from a file input.  
   - Attempts to establish an SSH connection using the `paramiko` library.

## Installation and Execution
#### Installing the requirements
```bash
python -m venv env
./env/Scripts/activate
pip install -r reqirements.txt
```
#### Executing the Framework
- To run in cli
```bash
python main.py
```

- To run in GUI
```bash
python main.py --gui
```
