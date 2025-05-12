Port Scanner Script
===================

Description:
------------
This Python script performs a basic port scan on a target host, checking whether specified ports are open.
It uses the socket library to attempt TCP connections to the target's ports.

Features:
---------
- Scans a given IP address or hostname
- Checks a range of ports (start to end)
- Displays which ports are open
- Calculates total scan duration

Requirements:
-------------
- Python 3.x
- Standard libraries only (no external dependencies)

Usage:
------
1. Run the script:
       python "port scaner.py"

2. Input the required information when prompted:
   - Target (IP address or hostname)
   - Starting port number (e.g., 20)
   - Ending port number (e.g., 80)

Example:
--------
   Enter the target (IP address or hostname): 127.0.0.1
   Enter the starting port: 20
   Enter the ending port: 80

   The script will then scan ports 20 through 80 on the given IP and print open ports.

Legal Notice:
-------------
Use this script only on devices or networks you own or have permission to scan.
Unauthorized port scanning may be considered illegal or unethical.

Disclaimer:
-----------
This script is provided for educational and ethical testing purposes only.
The author is not responsible for any misuse.
