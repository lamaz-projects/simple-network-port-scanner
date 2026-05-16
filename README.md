# Simple Network Port Scanner

A lightweight network reconnaissance tool built in Python using low-level socket programming to scan specific target hosts for open TCP ports.

## ⚠️ Disclaimer
*This tool is designed strictly for educational purposes and authorized security auditing.* Scanning networks or systems without explicit prior permission from the owner is unauthorized and potentially illegal. Always test using local loopback addresses (127.0.0.1 / localhost).

## Technical Architecture
The application works by initializing standard TCP handshakes across a designated loop range using Python's native socket library:
* *socket.AF_INET*: Establishes network communications under standard IPv4 addressing structures.
* *socket.SOCK_STREAM*: Instructs the system socket to run via connection-oriented TCP layer streaming.
* *connect_ex() Exception Handling*: Instead of throwing crashing runtime exceptions upon failing a handshake, this function returns an error code status block (0 for a successful open connection), ensuring smooth script execution.
* *Timeout Implementation*: Utilizes a strict 1.0 second socket connection threshold timeout to skip non-responsive closed ports quickly.

## Usage
1. Open a command line interface.
2. Clone this repository or copy the port_scanner.py file.
3. Execute the script:
   ```bash
   python port_scanner.py
