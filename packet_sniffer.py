from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP
from datetime import datetime

# Keeps track of the packet number
packet_count = 0


def process_packet(packet):
    global packet_count

    # Process only packets that contain an IP layer
    if packet.haslayer(IP):

        packet_count += 1

        # Current time
        current_time = datetime.now().strftime("%H:%M:%S")

        # Source and destination IP addresses
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

        # Determine the protocol
        if packet.haslayer(TCP):
            protocol = "TCP"
        elif packet.haslayer(UDP):
            protocol = "UDP"
        elif packet.haslayer(ICMP):
            protocol = "ICMP"
        else:
            protocol = "Other"

        # Packet size in bytes
        packet_length = len(packet)

        # Display packet information
        print("=" * 50)
        print(f"Packet No. : {packet_count}")
        print(f"Time       : {current_time}")
        print(f"Source IP  : {source_ip}")
        print(f"Destination: {destination_ip}")
        print(f"Protocol   : {protocol}")
        print(f"Length     : {packet_length} Bytes")
        print("=" * 50)
        print()


print("=" * 50)
print("         Python Packet Sniffer")
print("=" * 50)
print("Capturing 100 packets...\n")

sniff(
    prn=process_packet,
    count=100,
    store=False
)

print("\nPacket capture completed successfully.")
print(f"Total packets captured: {packet_count}")