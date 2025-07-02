import socket
import threading

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        s.connect((ip, port))
        print(f"[+] Port {port} is OPEN")
        s.close()
    except:
        pass

if __name__ == "__main__":
    target_ip = input("Enter IP address to scan: ")
    print(f"[*] Scanning {target_ip} for open ports 1–1024...\n")

    threads = []
    for port in range(1, 1025):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()  # Wait for all threads to finish
        
