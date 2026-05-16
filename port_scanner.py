import socket
import sys
from datetime import datetime

def scan_ports(target_host, port_range):
    try:
        # Resolve target hostname to IP address
        target_ip = socket.gethostbyname(target_host)
    except socket.gaierror:
        print("\n[-] Error: Hostname could not be resolved.")
        return

    print("\n" + "="*50)
    print(f" Scanning Target : {target_ip}")
    print(f" Time Started    : {str(datetime.now())}")
    print("="*50 + "\n")

    # Loop through the user-defined range of ports
    for port in port_range:
        # Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a quick timeout mechanism so it doesn't hang forever on closed ports
        s.settimeout(1.0)
        
        # Attempt to connect to the target IP and port
        result = s.connect_ex((target_ip, port))
        
        # connect_ex returns 0 if the connection was successful
        if result == 0:
            # Try to get a basic description of the port if known
            try:
                service_name = socket.getservbyport(port)
            except:
                service_name = "Unknown Service"
                
            print(f"[+] Port {port:5} : OPEN  ({service_name})")
            
        # Close the socket connection
        s.close()

def main():
    print("=========================================")
    print("       SIMPLE NETWORK PORT SCANNER       ")
    print("=========================================")
    print("[!] AUTHORIZED TARGETS ONLY. Do not scan public servers without permission.")
    
    # Get user inputs for target and range
    target_host = input("\nEnter target host IP or Domain (e.g., localhost or 127.0.0.1): ").strip()
    
    try:
        start_port = int(input("Enter starting port number (e.g., 20): "))
        end_port = int(input("Enter ending port number (e.g., 100): "))
        
        if start_port < 1 or end_port > 65535 or start_port > end_port:
            print("[-] Error: Invalid port range constraints.")
            return
    except ValueError:
        print("[-] Error: Ports must be valid integers.")
        return

    # Create the range sequence
    ports_to_scan = range(start_port, end_port + 1)
    
    # Execute scan loop
    scan_ports(target_host, ports_to_scan)
    print("\n[+] Scan completed successfully.")
    print("=========================================")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[-] Scan terminated by user.")
        sys.exit()