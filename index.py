#!python
print ("Content-Type: text/html")#header 라고하는것이다. print(''' '''라고 하면 줄바꿈 자동 인지하게 됨.)
print ()
#좆나 오래걸림 이거 구현하느라... keyerror:id 라고 계속 떠서. id값을 찾을 수 없다는 말이다.
#그말은 즉슨 밑에   title:'pageID' 라고 입력했기 때문 title:pageId가 아니고!!! 
#여튼 해결하고나니 기분좋음 ㅎㅎ
#원리는 체인 연결처럼 이어지는 거다. ol 태그 에 걸린 링크에 id를 설정->pageId=form[id]로 이어짐->title=pageId->h2태그의{title} 로 연결되는 구조.
import cgi
form = cgi.FieldStorage()
pageId = form["id"].value

print('''
<!doctype html>
<html>
<head>
    <meta charset="utf-8">
      <title>Python website</title>
</head>
<body>

<h1><a href="index.py?id=WEB">WEB</a></h1>
<div id="grid">
 <ol>
  <li><a href="index.py?id=HTML"> HTML</a></li>
  <li><a href="index.py?id=CSS"> CSS</a></li>
  <li><a href="index.py?id=JAVA"> JAVA</a></li>
 </ol>

<div id="article">
<h2>{title}</h2>
 WEB is short word for West East booger

</body>
</html>

'''.format(title=pageId))
#query string
