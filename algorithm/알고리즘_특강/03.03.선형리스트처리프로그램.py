'''선형리스트 처리 프로그램'''

## 함수 선언 부분 ##

def add_data(friend) :
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 마지막 칸에 데이터 입력
    katok[kLen-1] = friend

def insert_data(position, friend):
    # 1단계 : 빈칸 추가
    katok.append(None)
    kLen = len(katok)
    # 2단계 : 마지막 친구부터, 삽일할 위치까지 한칸씩 뒤로 이동
    for i in range(kLen-1, position, -1):
        katok[i] = katok[i-1]
        katok[i-1] = None
    # 3단계 : 위치에 친구 입력
    katok[position] = friend

    #katok[6] = katok[5] 인덱스 5에 위치한 값을 6으로 이동
    #katok[5] = None

def delete_data(position):
    # 1 단계 : 데이터 삭제
    katok[position] = None
    kLen = len(katok)
    # 2 단계 : 한칸씩 앞으로
    for i in range(position+1,kLen,1):
        katok[i-1] = katok[i]
        katok[i] = None
    # 3 단계 : 마지막 칸을 제거
    del(katok[kLen-1])

    

## 전역 변수 선언 부분
katok = []
select = -1 # 1.추가 2.삽입 3.삭제 4.종료
'''
-1은 초기화되지 않은 상태를 나타내거나 
기본값으로 사용되는 값 중 하나입니다.
특히 선택지를 받는 경우에는 사용자가 
아직 선택을 하지 않았음을 나타내기 위해 
-1을 초기값으로 설정하는 경우가 많다.
+ select 변수는 사용자와 프로그램 간의 상호작용을 가능하게 함
+ 사용자가 메뉴에서 1을 선택하면 특정 동작을 실행하고, 
2를 선택하면 다른 동작을 실핼하는 식으로 프로그램이 동작할 때
'''


## 메인 코드 부분 ##
# if__name__ == '__main__':
while(select != 4):
    select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)-->"))

    if(select == 1):
        data = input('추가할 데이터 --> ')
        add_data(data)
        print(katok)
    elif(select == 2):
        pos = int(input("삽일할 위치 -->"))
        data = input('추가할 데이터 -->')
        insert_data(pos, data)
        print(katok)
    elif(select == 3):
        pos = int(input("삭제할 위치 -->"))
        delete_data(pos)
        print(katok)
    elif(select ==4):
        print(katok)
        exit
    #  while 반복문의 조건이 false가 되어도 해당 루프에서는 
    # 여전히 사용자의 입력을 받고 조건을 검사합니다. 
    #이로 인해 사용자가 4를 선택하면 해당 루프에서 if 절이 실행되게 되는 것입니다.
    else :
        print("1~4중 하나를 입력하세요.")
        continue