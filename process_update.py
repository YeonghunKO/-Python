#!python

import cgi, os #os is not defined이라는 error가 뜨면 여기에 os를 추가해주면 된다.
form = cgi.FieldStorage()
pageId = form["pageId"].value #page Id를 별도로 받아야한다. update.py에서 pageId를 보냈으므로.
title = form["title"].value
description = form["description"].value

##우선 기본 cgi양식을 가져왔다. 그리고 []안의 값을 불러오는 FieldStorage를 적어준다. 그래서 [title] 값을 가져오도록 한다음 title변수안에 담아놓고 description도 마찬가지로 설정

opened_file = open('data/' +pageId, 'w')#data폴더안에 pageId를 입력한다. pageId는 숨김표시를 했기때문에 바뀌지 않는 고유의 정체성이 되는것이다. 그럼 결국에는 업데이트를 해도 data폴더안에 있는 파일의 제목은 변하지 않게 된다. 그렇게 수정된 파일을 쓰라고(만들라고) 명령.
opened_file.write(description)#마찬가지로 그리고 그 밑에 description을 쓰라고 명령.
opened_file.close()#쓰기 기능뒤에 반드시 닫기 기능을 달아줘야한다.

os.rename('data/' +pageId, 'data/' +title)
#rename이라는 함수는 os라는 module에 소속되어있어서 위에 import에 추가해야한다.
#path(경로)를 지정해줄 때 data 폴더 안에 / pageId라고 지정해야한다.(src(원본),dst(목적,수정하고픈 제목))


#Redirection이라고 한다. 사용자를 다른 경로로 보내는것. querystring, index.py?id 값이 title로 보내는 것이다.
print("Location: index.py?id="+title)
print()


#header 라고하는것이다. query string(url)을 설정하는 역할을 한다. (Content-Type: text/html) 라고하면 웹서버가 웹브라우저에게 '이제부터 전송하는거는 htmltext니깐 브라우저 너가 잘처리해' 라는 뜻이다.
#그러나 위의 코드처럼 적으면, 웹서버가 웹브라우저에게 '웹페이지야 submit을 클릭했을때 id값이 title웹페이지로 바로 이동해' 라고 하는것이다.
