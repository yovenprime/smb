# 🔑 VULN-NEXUS: SMB Auth & RDP Module

This module is the secondary stage of the **VULN-NEXUS** framework. After identifying an active SMB service during the reconnaissance phase, this tool allows for automated credential auditing to identify weak or default passwords.

## ⚙️ How It Works
The script utilizes the `impacket` library to communicate directly with the Windows SMB protocol (Port 445). It performs a series of login attempts using a provided wordlist. Once a valid combination is found, it logs the results and offers an immediate remote desktop connection.

## 🌟 Features
* **Automated Wordlist Processing:** Rapidly tests thousands of password combinations.
* **Smart Logging:** Automatically saves successful `IP | Username | Password` combinations to `found_creds.txt`.
* **RDP Handoff:** Integrated system call to `xfreerdp` for instant GUI access to the target machine upon success.
* **Safety First:** Built-in exception handling to prevent script crashes during network timeouts.

## 🛠️ Requirements
To use this module, ensure your environment is set up:
```bash
# Install Python dependencies
pip install impacket

# Install FreeRDP for the GUI connection
sudo apt install freerdp2-x11

🚀 Usage

Run the script with Python 3:
Bash

python3 smb.py
