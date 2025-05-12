import socket
from datetime import datetime
#create one fuction named port_scan
def port_scanner(target, start_port, end_port):
    print(f"Scanning target: {target}")
    print(f"Scanning ports: {start_port} to {end_port}")
    print("-" * 50)

    start_time = datetime.now()#get the starting scan time 
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# Basic syntax for socket 
        sock.settimeout(1)  # Set timeout for the connection attempt
        result = sock.connect_ex((target, port))  # Attempt to connect to the port
        print(result)
        if result == 0:
            print(f"Port {port}: OPEN")#Print the port 
        sock.close()
    end_time = datetime.now()#For get the end of the scan time 
    print("-" * 50)
    print(f"Scanning completed in: {end_time - start_time}")#Print the scan taken time  

if __name__ == "__main__":
    target = input("Enter the target (IP address or hostname): ")#Get the ip address for scan
    start_port = int(input("Enter the starting port: "))#Get the starting port
    end_port = int(input("Enter the ending port: "))#Get the ending port
    port_scanner(target, start_port, end_port)#Call the function with three parameter 
