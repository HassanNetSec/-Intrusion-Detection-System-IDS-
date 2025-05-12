from scapy.all import sniff

def handle_packet(packet):
    print(packet.summary())

# Start sniffing
sniff(iface="Wi-Fi", prn=handle_packet)
