import paramiko
import os

# SSH CONNECTION DETAILS
host = "bandit.labs.overthewire.org"
port = 2220
user = "bandit0"
password = os.getenv("BANDIT_PASS")

# CREATING A NEW SSH SESSION OBJECT
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # OPENING SSH CONNECTION WITH CREDS AND SERVER INFO
    c.connect(host, port=port, username=user, password=password)

    # RUN COMMAND TO READ THE README FILE (LVL1)
    stdin, stdout, stderr = c.exec_command("cat readme")

    # PRINT THE PASSWORD
    bandit1_pass = stdout.read().decode().strip()
    print(bandit1_pass)

finally:
    c.close()
