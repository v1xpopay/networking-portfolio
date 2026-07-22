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
