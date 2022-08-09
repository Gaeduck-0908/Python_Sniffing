from scapy.all import *

protocols = {1:'ICMP', 6:'TCP', 17:'UDP'} # 프로토콜 ID

def showPacket(packet): # prn 인자가 될 함수
    src_ip = packet[0][1].src
    dst_ip = packet[0][1].dst
    proto = packet[0][1].proto
    
    if proto in protocols:
        print ("protocol: %s: %s -> %s" %(protocols[proto], src_ip, dst_ip))
        
        if proto == 1:
            print ("TYPE: [%D], CODE[%d]" %(packet[0][2].type, packet[0][2].code))
            
def sniffing(filter):
    sniff(filter = filter, prn = showPacket, count = 0)
    
if __name__ == '__main__':
    filter = 'ip'
    sniffing(filter)