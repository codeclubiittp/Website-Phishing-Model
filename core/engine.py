from modules.osint import OSINTModule
from modules.scanning import ScanningModule
from modules.brute_force import BruteForceModule

class PenTestEngine:
    def __init__(self):
        self.osint = OSINTModule()
        self.scanner = ScanningModule()
        self.brute_force = BruteForceModule()

    def run(self):
        print("1. OSINT")
        print("2. Scanning")
        print("3. Brute Force")
        choice = input("Select an option: ")

        if choice == "1":
            target = input("Enter target for OSINT: ")
            self.osint.run(target)
        elif choice == "2":
            target = input("Enter target for scanning: ")
            self.scanner.scan(target)
        elif choice == "3":
            target = input("Enter target for brute force: ")
            self.brute_force.attack(target)
        else:
            print("Invalid choice")