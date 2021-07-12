# 자주 쓰는 Git 명령어 정리

1. Branch 관련 명령어
  - 로컬 branch 생성하기
    - git branch [branch name] + git checkout [branch name] == git checkout -b [branch name]
  - 원격 저장소에 branch 생성
    - git push --set-upstream origin [branch name] == git push -u origin [branch name]
  - 원격 저장소에 branch 삭제
    - git push origin --delete [branch name]
