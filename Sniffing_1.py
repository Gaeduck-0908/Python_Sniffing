from scapy.all import *

def showPacket(packet): # prn 인자가 될 함수
    a = packet.show() # 캡쳐한 패킷을 보기 쉽게 변환
    print (a) # 출력
    
def sniffing(filter):
    sniff(filter = filter, prn = showPacket, count = 1) # 중지할때까지 캡쳐하며 데이터링크 계층 ~ TCP/UDP 계층까지 출력
    
if __name__ == '__main__':
    filter = 'ip' #필터 설정
    sniffing(filter) #스니핑