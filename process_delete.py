#!python

import cgi, os
form = cgi.FieldStorage()
pageId = form["pageId"].value
##우선 기본 cgi양식을 가져왔다. 그리고 []안의 값을 불러오는 FieldStorage를 적어준다. 그래서 [title] 값을 가져오도록 한다음 title변수안에 담아놓고 description도 마찬가지로 설정

os.remove('data/'+pageId)

#Redirection
print("Location: index.py")
print()


#header 라고하는것이다. query string(url)을 설정하는 역할을 한다. (Content-Type: text/html) 라고하면 웹서버가 웹브라우저에게 '이제부터 전송하는거는 htmltext니깐 브라우저 너가 잘처리해' 라는 뜻이다.
#그러나 위의 코드처럼 적으면, 웹서버가 웹브라우저에게 '웹페이지야 submit을 클릭했을때 id값이 title웹페이지로 바로 이동해' 라고 하는것이다.
