TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are core transport layer protocols used for end-to-end communication between applications over a network
<b>TCP</b> is connection-oriented, meaning it establishes a connection using a three-way handshake before transmitting data, ensuring that all packets arrive correctly and in order. 
Client

SYN
↓

Server

SYN-ACK
↓

Client

ACK

<b> UDP </b> simply sends packet so no handshake , No guarantee of a response, which makes udp scanning easier.
connect()

↓

Handshake

↓

Connected

so if you are calling a service from port 80 but diff protocol, it looks like 
                 Port 80
                   │
        ┌──────────┴──────────┐
        │                     │
     TCP Scan             UDP Scan
        │                     │
socket.SOCK_STREAM     socket.SOCK_DGRAM (python syntex calling)
        │                     │
 connect()              send packet
        │                     │
Handshake?                 reply,
                        maybe not
