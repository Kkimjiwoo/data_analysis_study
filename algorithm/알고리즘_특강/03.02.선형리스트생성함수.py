'''선형 리스트를 생성하는 함수'''

## 함수

# 선형 리스트 생성하는 함수
def add_data(friend) :
    '''step1: 빈칸 추가'''
    katok.append(None)
    kLen = len(katok)
    '''step2: 마지막 칸에 데이터 입력'''
    katok[kLen-1] = friend

#-----------------------------------------------
# 데이터 삽입하는 함수
def insert_data(position,friend):   # 현재 5개의 데이터 있음
    '''step 1: 빈칸 추가'''
    katok.append(None)              # 빈칸 추가 총 6개의 자리
    klen=len(katok)                 # None을 추가하였으므로 총 6
    '''step2: 마지막 친구부터, 삽일할 위치까지 한칸씩 뒤로 이동'''
    for i in range(klen-1,position,-1):    # range(0,klen) 은 0부터 klen-1까지
        # position이 3일때 range(5,3,-1) 
        # 들리는 인덱스 5,4
        katok[i] = katok[i-1]          
        katok[i-1] = None
        # i = 5 => katok[5] = katok[4]
        # i = 4 => katok[4] = katok[3]
        # 인덱스 5 칸에 4의 값을 넣어야함
        # 목적: 인덱스 3칸을 비워야 함
        # 그러기 위해서는 i를 4까지만 돌리면 되기 때문에 range(5,3) 

        #katok[6] = katok[5] 인덱스 5에 위치한 값을 6으로 이동

    '''step3: 위치에 친구 입력'''
    katok[position] = friend

#---------------------------------------------------
# 데이터 삭제 함수
def delete_data(position):
    # 1 단계 : 데이터 삭제
    katok[position] = None
    kLen = len(katok)
    # 2 단계 : 한칸씩 앞으로
    for i in range(position+1,kLen,1): # 원소가 5개라면 인덱스는 0-4, position=2이다면, range(2,4)
        katok[i-1] = katok[i]
        katok[i] = None
    # 3 단계 : 마지막 칸을 제거
    del(katok[kLen-1])
# 원소가 5개라면 인덱스는 0-4, position=2이다면, range(2,4)
''' 이 방법도 가능
    for i in range(position,klen-1): # 원소가 5개라면 인덱스는 0-4, position=2이다면, range(2,4)
        katok[i] = katok[i+1]
        katok[i+1] = None
    del(katok[klen-1])
'''
'''
def del_data(position):
    del(katok[position])
리스트의 크기가 매운 큰 경우에는 비효율적
리스트의 요소를 삭제하면 그 뒤 모든 요소들이 
한 칸씩 앞으로 이동해야 하기 때문에
delete_data 함수는 요소의 이동이 필요하지 않기 때문에(요소를 앞당김)
요소를 이동시키는 경우, 요소의 이동의 횟수와 시간이 정비례
-> 메모리 내에서 데이터의 이동이 발생하지 않으면 시간이 덜 소요 
'''
    

## 변수
katok = []


## 메인
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(katok)
add_data('모모')
print(katok)


insert_data(3,'미나')
print(katok)
insert_data(7,'문별')
print(katok)

delete_data(3)
print(katok)


