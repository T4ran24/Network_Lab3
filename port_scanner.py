import socket

def scan_ports():
    target = "127.0.0.1"
    open_ports = []

    print(f"Scanning open ports on {target} (1–1024)...\n")

    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)  
        result = sock.connect_ex((target, port))

        if result == 0:
            open_ports.append(port)
            print(f"Port {port} is OPEN")
        
        sock.close()

    if not open_ports:
        print("No open ports found in the range 1–1024.")
    else:
        print(f"\nTotal open ports found: {len(open_ports)}")

if __name__ == "__main__":
    scan_ports()
