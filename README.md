# Packet Sniffer

A command-line tool that captures live network packets and displays important packet information including source and destination IP addresses, protocol type, packet size, and timestamps in real time.

Built with Python using Scapy and basic packet sniffing concepts.

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![Scapy](https://img.shields.io/badge/Scapy-Networking-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## Features

- Captures live network packets
- Displays source and destination IP addresses
- Detects TCP, UDP, ICMP, and other protocols
- Displays packet size
- Records timestamps for every packet
- Displays packet information in real time
- Automatically captures 100 packets before stopping

---

## Technologies Used

- Python
- Scapy
- VS Code

---

## Project Structure

```
packet-sniffer/
│
├── packet_sniffer.py
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/packet-sniffer.git
```

Move into the project folder

```bash
cd packet-sniffer
```

Install the required package

```bash
pip install scapy
```

---

## Usage

Run the program with administrator/root privileges.

```bash
sudo python3 packet_sniffer.py
```

The packet sniffer will begin capturing live network traffic and display packet information in the terminal.

The program automatically stops after capturing 100 packets.

---

## Sample Output

```
==================================================
Packet No. : 1
Time       : 14:37:28
Source IP  : 192.168.0.104
Destination: 142.250.183.46
Protocol   : TCP
Length     : 74 Bytes
==================================================
```

---

## Learning Outcomes

This project helped reinforce concepts including:

- Packet sniffing
- Network traffic monitoring
- TCP/IP communication
- IP packet analysis
- Python networking with Scapy
- Real-time packet processing

---

## Future Improvements

- Save captured packets to a CSV file
- Display source and destination port numbers
- Filter packets by protocol
- Detect suspicious network activity
- Color-coded terminal output
- Live traffic statistics dashboard

---

## License

This project is licensed under the MIT License.
