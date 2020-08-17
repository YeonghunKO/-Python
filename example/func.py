#code...
a=1
b=2
c=3
s=a+b+c
r=s/3
print(r)
#code...항상 이러한 코드가 1억개가 있다고 생각하자. 그럼 무엇이 무엇과 연관되어있는지 파악하기 매우 힘들다.
#그래서 밑의 평균값처럼 함수식을 쓴다.
'''
def av():#def라고 하면 함수가 시작된다고 생각하면 된다. a~print값을 av라는 함수로 지정하였다.
         #그리고 이제 밑에av()라고하면 자동으로 평균값이 계산된다. 그리고 밑에 나열된 값이 같은취지의 함수라고 보기쉽게 인식될 수 있다.
     a=1
     b=2
     c=453
     d=3234
     s=a+b+c
     r=s/3
     print(r)
'''

'''
#input
#parameter
#argument
def av(a,b,c,d):
     s=a+b+c+d
     r=s/4
     print(r)

av(10,12,14,16)
#이렇게 함수를 더 간략하고 효율적으로 정리 할 수 있다.!!! 원하는 위치에 숫자를 넣기만 하면 되기 때문.
#a,b,c를 parameter(변수)라고하고 10,12,14 함수 입력값으로 줘버린 숫자를 인자(argument)라고 한다.
'''

def av(a,b,c,d):
     s=a+b+c+d
     r=s/4
     return r #r 값이 보여지도록 하기위한 태그이다.

print(av(10,12,14,16))
#함수는 하나의 기능만 담당하는게 좋다. 중복과 복잡성을 막기위해서.