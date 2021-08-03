git clone 이후 runserver까지 해야할 일
1. python -m venv myvenv
2. source myvenv/Scripts/activate
3. pip install -r requirements.txt
4. secret.json 파일 해당 폴더에 넣어주기

->이 부분부터 하시면 됩니다.
최초 BackEnd, FrontEnd branch 받아올 때,
1. git checkout -t origin/BackEnd or git checkout -t origin/FrontEnd
2. pip install -r requirements.txt
3. git checkout -b "feat/change-DB" (branch명은 예시입니다.)
4. 코드 수정 후 git add . git commit git push 
5. PR (비교대상은 master가 아니고 BackEnd, FrontEnd입니다. )

이러면, BackEnd, FrontEnd에 PR을 날리는게 가능합니다. 
이해 안 되시면 말씀해주세요.

작업 시작 시 해야할 일(작업 branch에서)
1. git pull
2. pip install -r requirements.txt

해당 branch는 FE입니다.
팀원은 이곳의 내용을 변경하지 말아주세요.
