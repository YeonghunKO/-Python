#!python
print ("Content-Type: text/html")#header 라고하는것이다. print(''' '''라고 하면 줄바꿈 자동 인지하게 됨.)
print ()
#좆나 오래걸림 이거 구현하느라... keyerror:id 라고 계속 떠서. id값을 찾을 수 없다는 말이다.
#그말은 즉슨 밑에   title:'pageID' 라고 입력했기 때문 title:pageId가 아니고!!!
#여튼 해결하고나니 기분좋음 ㅎㅎ
#원리는 체인 연결처럼 이어지는 거다. ol 태그 에 걸린 링크에 id를 설정->pageId=form[id]로 이어짐->title=pageId->h2태그의{title} 로 연결되는 구조.

import cgi, os, view



##감격적이지 않냐?ㅠㅠ 포문 을 통해 files 안에 있는 리스트(item)에 링크를 걸고 목록을 만든다음 그 목록들을 더하는 작업을 ''반복'' 하도록 만들었다.
##그리고 이 listStr을 맨 마지막 format에 추가 시키고 <ol> 태그에 {listStr} 적어서 HTML코드를 한줄로 요약하였다. 이렇게 되면 이제 DATA data폴더안에
##있는 문서만 수정하면 된다. DATA폴더에 PYTHON 폴더만 만들면 끝나는 거다. 대단하다 이고잉. 그리고 이런 작업을 문장으로 표현한 인간도 경의롭다. 그 창의력과 상상력에.

form = cgi.FieldStorage()#사용자가 index.py뒤에 id값을 받을때 이 코드를 사용함.
if 'id' in form:
    pageId = form["id"].value
    description = open('data/'+pageId, 'r').read()#description의 값을 설정해줘야함.id가 있으면 데이터폴더에 들어가서 id에 해당하는파일을 읽는 모드로 바꾼다음('r') 열어라(open). 그리고 그 열은 값을 description에 포함시켜라 는 뜻. 함수이다.
    description = description.replace('<', '&lt;')
    description = description.replace('>', '&gt;')
    
    #자바를 이용해 해킹하려고 할떄 replace 메소드를 썼다. (<와>를 lt와gt로 치환한다. 그럼글자로 표시되면서 해킹을 막을 수 있는 보안장치이다.)
    update_link = '<a href="update.py?id={}">update</a>'.format(pageId)#update기능을 추가했다. id값이 있는 즉,content 를 눌렀을떄는 update가 표시되게하고 아니면 else처럼 공백이 뜨도록했다. 그리고 밑에 create링크 옆에 update format을 추가함.
    delete_action = '''
       <form action="process_delete.py" method="post">
         <input type="hidden" name="pageId" value="{}">
         <input type="submit" value="delete">
       </form>
      '''.format(pageId)
      #delete기능은 링크로 하면 안되고 form으로 처리해야한다. delete를 링크로 처리해 공유하게 되면, 누구나 삭제를 감행할 수 있기 때문.
else:
    pageId = 'Welcome'
    description = 'Hello, ET'
    update_link = ''
    delete_action = ''
#조건문을 사용했더니 쌈빡하게 되었다. if 'id' in form 는 ''폼안에 id 있으면''이라는 뜻.
#중요!:if 위에 변수 두줄을 빼먹지 말것!
##HTML로만 만든 웹사이트와 파이썬을 통해 만든 웹사이트에는 엄청난 차이가 있다. HTML 코드가 index.py에 철저히 갇혀있고, 이것만 바꾸면 모든 페이지에 적용가능하다. 그리고 data폴더안에 내용이 깔끔하게 저장되어있다
##읽어야하는 코드수가 현저하게 줄어드니 나가는 돈도 줄어든다. 폭발적인 변화이다.

print('''<!doctype html>
<html>
<head>
  <title>WEB1 - Welcome</title>
  <meta charset="utf-8">
</head>
<body>
  <h1><a href="index.py">WEB</a></h1>
  <ul>
    {listStr}
  </ul>
  <a href="create.py">create</a>
   {update_link}
   {delete_action}
  <h2>{title}</h2>
  <p>{desc}</p>
</body>
</html>
'''.format(title=pageId,
           desc=description,
           listStr=view.getList(), #위의 명확하게 표현된 함수를 사용함으로써 가독성을 높인다. 그리고 view.를 통해 view 모듈안에 getList가 있다는 것을 알 수 있다.
           update_link=update_link,
           delete_action=delete_action
           ))


#query string
