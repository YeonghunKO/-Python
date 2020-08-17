user_id = input('id')
user_pwd = input('password?') #사용자에게 입력할 수 있게 바톤을 넘겨줌 개발자가 입력하는게 아니라.
#조건문.
'''
if user_pwd == '111111':
    print('Hello bastard')#파이썬은 같은 블럭을 같은 문법으로 인식 그래서 들여쓰기, 띄어쓰기 통일!
else:
    print('who are you?')
'''
#패스워드가111111이면 hello 가 뜨고 아니면 who are you가 뜨도록 만들었다.
#p.s:''' '''으로 감싸면 그냥 문장이 된다.
'''
if user_id == 'young':
 if user_pwd == '111111':
        print('Hello')
 else:
        print('who?')
'''
#조건문 중복으로 쓰기 가능

#and논리 연산자는 둘다 true 일때 print 안에 있는 값을 실행시킨다.
#그리고 또다른 연산자를 추가하고 싶을때는 else if의 약자 elif를 추가시킨다.
if user_id == 'young' and user_pwd == '1111':
    print('Hello young! Welcome to my world')

elif user_id == 'kim' and user_pwd == '2222':
    print('Hello kim! Welcome to my world')
else:
    print('Who the hell are you?')
