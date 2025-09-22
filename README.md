# Welcome to the Bandit ToolBox!

This repo contains Python scripts that I have written to automate the process of solving the OverTheWire Bandit CTFs.

As someone who is still gaining experience in writing Python for cybersecurity use in general, I decided to create these scripts to:

1. Practice using Python libraries specific to CTFs
2. Automate steps involved in solving these challenges
3. Build a library for educational and learning purposes

## Table of Contents
- [About](#about)
- [Setup](#setup)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
- [Disclaimer](#disclaimer)

### About
The Bandit Toolbox was created to help me practice Python scripting in a CTF/pentesting context and it may help you too! These scripts automate tasks such as:
- Connecting to OTW Bandit levels via SSH
- Executing commands on target and retrieving that output
- Parsing through output to extract relevant information

Each script corresponds to a specific Bandit level and can be found in their designated folder to keep things organized.

### Setup
1. Clone the repository:
```
git clone https://github.com/tink3rzzz/bandit-toolbox.git
cd bandit-toolbox
```

2. Install required Python packages (if any):
```
pip install -r requirements.txt
```

**NOTE:** A `requirements.txt` file is in the making as I create more scripts

*(For most Bandit scripts, `paramiko` may be required for SSH automation)*

### Environment Variables
All scripts use environment variables to avoid hardcoding credentials:

`BANDIT_PASS`: password for Bandit level

### Usage
1. Set environment variables for credentials to keep them secure:
- Bash: `export BANDIT_PASS=<password>`
- Windows PowerShell: `setx BANDIT_PASS <password>`

2. Run the script for a specific level:
`python3 bandit#.py`

Each script will output the password or relevant information for that level.

### Disclaimer
These scripts are intended for educational purposes and CTF practice only. Do not use them on unauthorized systems or real targets! By using this repo, you also abide by OverTheWire's rules.
