#!python
print ("Content-Type: text/html")#header 라고하는것이다. print(''' '''라고 하면 줄바꿈 자동 인지하게 됨.)
print ()
#좆나 오래걸림 이거 구현하느라... keyerror:id 라고 계속 떠서. id값을 찾을 수 없다는 말이다.
#그말은 즉슨 밑에   title:'pageID' 라고 입력했기 때문 title:pageId가 아니고!!!
#여튼 해결하고나니 기분좋음 ㅎㅎ
#원리는 체인 연결처럼 이어지는 거다. ol 태그 에 걸린 링크에 id를 설정->pageId=form[id]로 이어짐->title=pageId->h2태그의{title} 로 연결되는 구조.

import cgi, os, view


form = cgi.FieldStorage()#사용자가 index.py뒤에 id값을 받을때 이 코드를 사용함.
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()#description의 값을 설정해줘야함.id가 있으면 데이터폴더에 들어가서 id에 해당하는파일을 읽는 모드로 바꾼다음('r') 열어라(open). 그리고 그 열은 값을 description에 포함시켜라 는 뜻. 함수이다.
else:
    pageId = 'Welcome'
    description = 'Hello, ET'
#조건문을 사용했더니 쌈빡하게 되었다. if 'id' in form 는 ''폼안에 id 있으면''이라는 뜻.
#중요!:if 위에 변수 두줄을 빼먹지 말것!
##HTML로만 만든 웹사이트와 파이썬을 통해 만든 웹사이트에는 엄청난 차이가 있다. HTML 코드가 index.py에 철저히 갇혀있고, 이것만 바꾸면 모든 페이지에 적용가능하다. 그리고 data폴더안에 내용이 깔끔하게 저장되어있다
##읽어야하는 코드수가 현저하게 줄어드니 나가는 돈도 줄어든다. 폭발적인 변화이다.

print('''
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
      <title>Python website</title>
</head>
<body>

<h1><a href="index.py">WEB</a></h1>

 <ol>
  {listStr}
 </ol>


<a href="create.py">create</a>
<form action="process_create.py" method="post">
    <p><input type="text" name="title" placeholder="title"></p>
    <p><textarea rows="6" cols="120" name="description" placeholder="description"></textarea></p>
    <p><input type="submit"></p>
</form>
</body>
</html>

'''.format(title=pageId, desc=description, listStr=view.getList()))
#query string

#이게 무슨뜻이냐면, text박스에 작성한 제목과 설명을 submit 하면, title 그리고 description이라는 이름으로
# process_create.py 파일로 서버를 통해 전송한다는 뜻이다.
#form을 쓰는 이유: 사용자가 입력한 것을 서버로 ''전달''하기 위해 form 태그를 사용할 수 있습니다. 여기서는 새로운 페이지를 생성하기 위해, html페이지에 form(그리고 그 내부에 '제목'과 '내용')을 만들었습니다.
# 그런데 저 상태로 submit을 하게 되면 url 이 노출되면서 사용자가 정보를 마음대로 수정,삭제할 수 있기 때문에 URL을 숨기는 기능을 추가해야한다
#그래서 method="post" 라는 문법을 form 마지막에 추가하는 것이다. (p.s:보통 링크를 클릭해서 정보를 가져올때는 ?id=@@이라고 url이 떠야한다. 그래야 정확한 위치에서 정보를 가져올 수 있으므로)
