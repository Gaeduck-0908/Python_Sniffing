# Python_Sniffing
### Python 을 이용한 스니핑
참고한 게시글 : https://secretpack.tistory.com/112
# Scapy Install
```
pip install Scapy
```
![image](https://user-images.githubusercontent.com/82009667/183590985-0c29ad59-56a7-461f-92b2-72be993e53b6.png)
# import Scapy
```
from scapy.all import *
```
# Important Function
#### sniff() 네트워크 패킷을 스니핑 하는 함수 
|인자|내용|
|------|---|
|**count**|패킷을 캡쳐하는 횟수 0이면 중지할때까지 캡쳐한다.|
|**store**|캡쳐한 패킷을 저장할 것인지 지정 모니터링만 원하면 0으로 지정한다.|
|**prn**|캡쳐한 패킷을 처리하기 위한 함수 지정. 지정한 함수의 인자는 캡쳐한 패킷으로 정해진다.|
|**filter**|원하는 패킷만 볼 수 있는 필터를 지정한다.|
|**timeout**|스니핑 수행 시간을 지정한다 시간이 지나면 종료한다.|
|**iface**|네트워크 인터페이스를 지정한다.|

#### 계층 접근 방법
|구분|내용|
|------|---|
|**packet**|sniff()가 캡쳐한 패킷. prn인자로 지정된 함수의 인자로 전달한다.|
|**packet[0][0]**|MAC Address|
|**packet[0][1]**|IP Address, packet[IP] 로도 접근 가능|
|**packet[0][2]**|TCP,UDP,ICMP 계층 각각 packet[TCP],packet[UDP],packet[ICMP]로 접근가능|

# Run file
### Sniffing_1.py
![image](https://user-images.githubusercontent.com/82009667/183594678-2c6767f7-cd22-431e-859f-c3289952a74d.png)
### Sniffing_2.py
![image](https://user-images.githubusercontent.com/82009667/183603275-a3b0453b-3178-42aa-ade6-f36afab73a99.png)

