#Positional Formating 순서대로 위치에 따라 내가 넣고싶은 값을 통제하는 포메팅.

print('Lorem ipsum dolor sit amet, consectetur adipisicing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.{} Excepteur sint occaecat cupidatat non proident, {} sunt in culpa qui officia deserunt {} mollit anim id est laborum.'.format('young', 29, 'young'))

#Named holders 위의 포메팅보다 더 복잡해졌지만 포메팅 뒤에 중복이 사라졌고, 내가 원하는 값을 괄호안에 자유자재로 넣을 수 있다. 그리고 {age}에 반드시 숫자만 와야겠다고 하면 {age:d}라고 하면 된다. d 는 digit의 약자이다.
print('Lorem ipsum dolor sit amet, consectetur adipisicing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.{name} Excepteur sint occaecat cupidatat non proident, {name} sunt in culpa qui officia deserunt {age:d} mollit anim id est laborum.'.format(name='young', age=29))


print('''Lorem ipsum dolor sit amet,
consectetur adipisicing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam,quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.{name} Excepteur
sint occaecat cupidatat non proident, {name} sunt in culpa qui
officia deserunt {age:d} mollit anim id est laborum.'''.format(name='young', age=29))
