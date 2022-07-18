# 시작

1. git init 을 입력하여  시작

2. touch a.txt로 임의의 텍스트파일 생성
3. 이 상태에서 git status를 해보면



On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        a.txt

nothing added to commit but untracked files present (use "git add" to track)



즉, 1)commit 한 것이 없고 

​      2)git으로 관리되고 있는(tracked) 파일이 없고

​      3)만약 a.txt를 commit 하고 싶으면 git add \<file> 로 commit 할 준비를 해라

라고 알려준다.



# 본격적으로  commit 해보기

1.  git add a.txt를 실행하면 a.txt는 staging area에 올라가게 된다.



###### 잠깐! git의 로컬 저장소?

​	실제 폴더는 따로 있는 상태에서, 로컬 git은

​	working directory - staging area - commits

​	와 같이 구성된다.햇



2. git commit -m "commit message"을 실행하면... 안 된다.

Author identity unknown

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'SSAFY@DESKTOP.(none)')

즉, "니가 누군지도 모르겠는데 commit은 무슨" 이라고 퇴짜를 맞는다.



3. 내가 누군지를 알려줘야 되는데,

   - email의 경우는 깃허브
   - name의 경우는 깃랩

   에 있는 정보를 알려주면 된다. 알려준 뒤 다시 실행해보면

   

   [master (root-commit) faa1629] commit message
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 a.txt

    

   1개의 파일이 변경되었다고 성공적으로 뜬다.

   

4.  이 상태에서  git status를 실행해보면

   On branch master
   nothing to commit, working tree clean

   즉, 코밋할 게 없다(변경사항이 없다)고 뜬다.



## 바뀌면?

1. a.txt를 열고 내용을 수정해본 뒤, 다시 git status를 실행해보면

   Changes not staged for commit:
     (use "git add <file>..." to update what will be committed)
     (use "git restore <file>..." to discard changes in working directory)
           modified:   a.txt

no changes added to commit (use "git add" and/or "git commit -a")



즉 변경사항이 staging area 에 아직 올라가지 않았고

- 업데이트 할 거면 add 해
- 없었던 일로 하려면 git restore을 실행해

라고 말해준다.



2. 변경사항을 commit 해본 뒤에 git log 라는 명령어를 실행해보면 그 동안 commit 한 내역이 뜨고 git commit -m "commit message" 에서 "commit message" 부분을 잘 적었다면 어느 commit에서 어떤 변경사항이 있었는지 확인할 수 있다.

   

3. log들이 길어 하나를 한줄로 간략하게 보고 싶다면 git log --oneline 을 통해 간략하게 볼 수도 있다. 

   

4. 또, 그냥 git commit만 써서 실행하면 commit message를 상세하게 쓸 수 있는 vi 편집기가 나온다. 처음 화면에서 I를 입햐력하면 insert모드에 진입해 글을 쓸 수 있고 esc 키를 통해 insert 모드에서 나갈 수 있다.  insert모드에서 나온 뒤 : wq를 이용해  vi에디터를 종료, 메세지를 저장할 수 있다.



## add

1.  변경사항, 혹은 새로운 것이 여러 개가 생겨서 add를 여러 개 할 필요가 있을 때엔, 폴더에 있는 놈들을 싹 다 올려버릴 수 있을 필요가 있다. 혹시 안 되어있다면 해당 폴더로 디렉토리를 바꿔준 뒤,

    git add .

   을 통해 현재 폴더에 있는 모든 변경사항을 staging area로 올릴 수 있다. git status로 어떤 놈은 수정된 놈이고 어떤 놈은 새로 들어온 놈인지도 알 수 있다.

   그 뒤  평소대로  코밋하면 된다.

2. .gitignore 파일을 생성하고 git으로 관리하고 싶지 않은 파일 이름(복수의 경우 엔터로 구분)을 적어 넣으면 add . 등을 통해서도 올릴 수 없다.

3. git이 관리하던 파일을 수정 후 .gitignore에 추가해도 git이 관리하려고 한다. untrack 하게 바꿀 수도 있지만 **중요한 것은 repo를 생성한 직후에 "로컬에서" .gitignore에 넣어놓는 편이 훨씬 좋다.**



## github와 연동

1. 연동하고 싶은 directory로 이동하고, github를 열어 repository를 하나 만든다
2. 해당 repository의 주소를 복사하고, git remote add origin \(url)을 실행하면, 일단 연동이 된다. git remote -v를 통해 현재 연동된 repository 주소를 확인할 수 있다.



##  github에 push

1. git push origin master을 통해  commit한 놈들은 github로 푸쉬해준다. 처음 push하는 디바이스라면 인증이 필요하다.
   - 만약 git push -u origin master와 같은 형태로 푸쉬하면, 다음부터는 git push만 쳐도 자동적으로 origin master에 push된다.
2.  아직 push 하지 않고 git log를 실행하면 push한 commit과 그렇지 않은  commit을 판별할 수도 있다.



## gitgub에서 pull

1. git clone을 이용해 github push된 상태를 불러올 수 있다. git clone (url) [원하는 디렉토리]
2. 만약 A PC에서 push한 결과물을 B PC에 clone 하면, 후에 A PC 에서 새로 push가 발생했을 때 B PC에서 git pull 을 통해 불러올 수 있다. 

## pull/push 충돌 시 대처
- 충돌이 발생하면 기본적으로 push가 되지 않는다.

1. 중복되지 않는 충돌의 경우, pull로 불러오면 자동으로 merge 커밋이 하나 남고 pull이 되어 push를 할 수 있게된다.

2. 중복되는 충돌의 경우, pull로 불러오려고 하면 merge가 실패했다는 보고가 뜨면서 니가 알아서 해결하라고 한다. 이 때 중복된 파일을 열어보면 원래 가지고 있던 내용물과 pull 해 온 내용물이 구분되어 둘 다 표기되어 있는데, 하나만 선택하든지 아예 새로 쓰든지 알아서 하고 다시 push 하자. (이런 경우 vscode 등으로 열어보면 일반적인 선택 옵션이 몇 개 뜬다.)