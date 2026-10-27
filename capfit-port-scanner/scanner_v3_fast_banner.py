import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP [use 127.0.0.1 only]: ").strip()
# IMPORTANT: Only scan 127.0.0.1 or scanme.nmap.org - that's the ethical rule

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            # Real check: try to grab banner
            try:
                s.send(b'HEAD / HTTP/1.0\r\n\r\n')
                banner = s.recv(1024).decode(errors='ignore').strip()
                # Take only first line
                first_line = banner.split('\n')[0][:80] if banner else "No banner (but open)"
                print(f"[+] Port {port:5} OPEN  -> {first_line}")
            except:
                print(f"[+] Port {port:5} OPEN  -> (open, no banner)")
        s.close()
    except:
        pass

print(f"\n--- Fast scanning {target} ports 1-1024 ---\n")

# 100 threads = fast
with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, range(1, 1025))

print("\n--- Done. If you scanned 127.0.0.1 with http.server 80 running, you should see Port 80 + Python banner ---")