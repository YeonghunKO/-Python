import os #os is not defined 라는 에러가 뜨면 이 태그를 써서 os 모듈을 불러와야한다
def getList():#def 라고 하고 getList라고 설정해주면 목록을 가져오는 코드라는 것이 명확해 지면서 가독성이 좋아진다. 이러한 작업을 'Refactoring' 이라고 한다. 이렇게 함수라는 수납상자를 이용해서 글을 깔끔하게 만들자.
    files = os.listdir('data')#데이터 폴더안에 있는 파일 목록을 불러오는 문법이다. 그걸 files 변수에 담았다.
    listStr = ''
    for item in files:
        listStr = listStr + '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)
    return listStr
