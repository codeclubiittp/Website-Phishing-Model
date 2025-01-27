import nmap

class ScanningModule:
    def scan(self, target):
        print(f"Scanning {target}...")
        nm = nmap.PortScanner()
        nm.scan(hosts=target, arguments="-sS")
        print(nm.csv())