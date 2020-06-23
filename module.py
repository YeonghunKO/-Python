#Module
#수학공식을 파일마다 일일이 입력할필요없이. 하나의 파일에 중복되는 수학공식을 입력하고(math2)
#그 수학공식이 필요할 떄 마다 module 의 형태로 가져오면 된다. 그때 import math2 라고 입력하면 된다.
'''
import math2 # **module 'math' has no attribute 'av' 이런 에러가 뜬다면 모듈의 이름을 바꾸고 다시 실행해보자.
             #다른 모듈을 가져오고 싶을때 import math, ** 처럼 , 를 쓰면 된다.
print(math2.av(10,12,14,16))
print(math2.plus(1,2))
print(math2.pi)
'''

#math2라는 중복을 줄이고 싶을 때
from math2 import av, plus, pi

print(av(10,12,14,16))
print(plus(1,2))
print(pi)
#math2 라는 모듈에서 average,plus,pi 라는 함수를 불러온다. 라고 더 명령을 세분화시켜주는 것이다. 마치 html에서 link 태그를 이용해 css.style을 불어오는거랑 비슷한 원리이다.
