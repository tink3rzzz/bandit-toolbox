import paramiko
import os

# SSH CONNECTION DETAILS
host = "bandit.labs.overthewire.org"
port = 2220
user = "bandit1"
password = os.getenv("BANDIT_PASS")

# CREATE SSH CLIENT
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    c.connect(host, port=port, username=user, password=password)
    stdin, stdout, stderr = c.exec_command("cat ./-")
    bandit2_pass = stdout.read().decode().strip()
    print(bandit2_pass)

finally:
    c.close()
