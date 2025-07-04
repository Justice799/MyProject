# test_scapy.py
try:
    from scapy.all import ARP, Ether, srp
    print("Scapy installed successfully! Ready for cybersecurity tasks.")
    # Create a sample ARP packet
    packet = ARP()
    print("Created ARP packet:", packet.summary())
except ImportError:
    print("Error: Scapy not installed. Run 'pip install scapy' in your virtual environment.")