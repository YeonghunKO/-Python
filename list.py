#list-container(여러가지 물건들을 수납할 수 있는 가구라고 생각하면 된다.)
s = [1, 'four', 9, 16, 25, 'Pleasure']
print(s)
print(s[4])
#대괄호안에 있는 숫자를 index라고한다. 첫번쨰 자리에 있는 index값은 0이다.
#대활호 안에 있는 목록을 원소(element)라고 한다.
print(len(s))
#괄호안에 있는 내용의 양을 알아내는 태그
##생성하는 법 , 꺼내서 찾아내는 법, 읽어내는 법
s[1] = 4#내용 수정하는 방법
print(s)

del s[2]#index를 이용해서 내용물을 삭제하는 법. 그리고 그 뒤에 있는 원소가 빈자리를 매꿈
s.insert(2,"five")#두번째 index에 five추가
print(s)
s.append('young')#맨끝자리에 원소 추가
##만약 각 원소에 이름을 부여하고 싶다면 dicttionary 태그를 쓰면 된다. 알아서 찾아봐라.
