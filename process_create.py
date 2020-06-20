#!python

import cgi
form = cgi.FieldStorage()
title = form["title"].value
description = form["description"].value
##우선 기본 cgi양식을 가져왔다. 그리고 []안의 값을 불러오는 FieldStorage를 적어준다. 그래서 [title] 값을 가져오도록 한다음 title변수안에 담아놓고 description도 마찬가지로 설정

opened_file = open('data/' +title, 'w')#data폴더안에 title안에 입력한 폴더를 쓰라고(만들라고) 명령.
opened_file.write(description)#마찬가지로 그리고 그 밑에 description을 쓰라고 명령.
opened_file.close()#쓰기 기능뒤에 반드시 닫기 기능을 달아줘야한다.

#Redirection
print("Location: index.py?id="+title)
print()


#header 라고하는것이다. query string(url)을 설정하는 역할을 한다. (Content-Type: text/html) 라고하면 웹서버가 웹브라우저에게 '이제부터 전송하는거는 htmltext니깐 브라우저 너가 잘처리해' 라는 뜻이다.
#그러나 위의 코드처럼 적으면, 웹서버가 웹브라우저에게 '웹페이지야 submit을 클릭했을때 id값이 title웹페이지로 바로 이동해' 라고 하는것이다.
