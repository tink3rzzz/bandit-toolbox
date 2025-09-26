import paramiko
import os

# SSH CONNECTION DETAILS
host = "bandit.labs.overthewire.org"
port = 2220
user = "bandit3"
password = os.getenv("BANDIT_PASS")

# CREATING SSH CLIENT
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # CONNECTING TO SERVER
    c.connect(host, port=port, username=user, password=password)

    # LIST HIDDEN FILES IN "inhere" DIRECTORY
    stdin, stdout, stderr = c.exec_command("ls -a ./inhere")
    files = stdout.read().decode().strip()
    files = files.split()

    for f in files:
        if f != "." and f != "..":
            stdin, stdout, stderr = c.exec_command(f"cat ./inhere/{f}")
            hidden = f
    
    # FORMATTING PASSWORD
    bandit4_pass = stdout.read().decode().strip()
    print(f'''Hidden File: "{hidden}"
Password: {bandit4_pass}''')

finally:
    c.close()
