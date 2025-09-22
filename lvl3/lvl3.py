import paramiko
import os

# SSH CONNECTION DETAILS (CHANGE "host" VARIABLE)
host = "target_host"
port = 2220
user = "bandit2"
password = os.getenv("BANDIT_PASS")

# CREATE A SSH CLIENT
c = paramiko.SSHClient()
c.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    c.connect(host, port=port, username=user, password=password)

    # USE SINGLE QUOTES AROUND FILENAME TO HANDLE SPACES CORRECTLY
    stdin, stdout, stderr = c.exec_command("cat './--spaces in this filename--'")
    bandit3_pass = stdout.read().decode().strip()
    print(bandit3_pass)

finally:
    c.close()
