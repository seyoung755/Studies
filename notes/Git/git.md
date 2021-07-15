## 자주 쓰는 Git 명령어 정리

1. Branch 관련 명령어
  - 로컬 branch 생성하기
    - git branch [branch name] + git checkout [branch name] == git checkout -b [branch name]
  - 원격 저장소에 branch 생성
    - git push --set-upstream origin [branch name] == git push -u origin [branch name]
  - 원격 저장소에 branch 삭제
    - git push origin --delete [branch name]

## Git의 3가지 영역
#### Git의 역할? 아래 3가지 영역을 동기화해준다. (Synchronization)
1. 작업 영역(폴더)
  : 우리가 실시간으로 코드를 작업하는 로컬 공간
2. 인덱스 영역(스테이징된 공간)
  : 로컬에서 작업하던 어느 순간을 기록해놓는 공간
3. 헤드 영역(Commit)
  : 인덱스 영역들의 시점을 보관해놓는 공간으로 HEAD를 통해 특정 시점으로 되돌아갈 수 있다.
