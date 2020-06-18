#데이터의 종류
#Number
print(1) #Integer 정수
#string
print('Hello world')
#Boolean
print(True) #참
print(False) #거짓
#Expression
print(1+1) #산술연산자
print('가' + 'world') #이항연산자. 가 world 가 됨
#Comparsion operater 비교연산자
print(1==1) #True
print(1<2) #True
print(2<1) #False
#Memebership operater
print('world' in 'Hello world') #True -- Hello world라는 문장안에 world 라는 단어가 있으므로. 그룹안에 속해있는 구성원
#어떤 directory 안에 내가 찾고싶은 파일이 있는지 확인하고 싶을떄
import os.path
print(os.path.exists('boolean.py'))
##boolean은 어떤 조건을 만났을때 그 조건이 어떠한 상태인지 표시해주는 데이터타입이다.
