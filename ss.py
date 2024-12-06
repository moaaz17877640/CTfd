from scapy.all import *

# الدالة التي ستقوم بالرد على الحزم
def reply_with_rst_ack(packet):
    # التحقق إذا كانت الحزمة ICMP (ping)
    if packet.haslayer(ICMP) and packet[ICMP].type == 8:  # ICMP Echo Request
        # بناء حزمة RST/ACK
        ip_layer = IP(src=packet[IP].dst, dst=packet[IP].src)
        tcp_layer = TCP(sport=80, dport=packet[IP].sport, flags="RA", seq=12345, ack=packet[IP].id)
        response = ip_layer / tcp_layer
        
        # إرسال الحزمة
        send(response)
        print(f"RST/ACK sent to {packet[IP].src}")

# استماع على الواجهة الافتراضية
sniff(filter="icmp", prn=reply_with_rst_ack)
