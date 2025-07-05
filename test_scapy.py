# test_scapy.py
try:
    from scapy.all import ARP, Ether, srp
    print("Scapy installed successfully! Ready for cybersecurity tasks.")
    # Create a sample ARP packet
    packet = ARP()
    print("Created ARP packet:", packet.summary())
    # Basic network scan (run in a safe lab environment)
    arp = ARP(pdst="192.168.8.110/24")  # Replace with your network range
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp
    result = srp(packet, timeout=3, verbose=0)[0]
    for sent, received in result:
        print(f"IP: {received.psrc} MAC: {received.hwsrc}")
except ImportError:
    print("Error: Scapy not installed. Run 'pip install scapy' in your virtual environment.")