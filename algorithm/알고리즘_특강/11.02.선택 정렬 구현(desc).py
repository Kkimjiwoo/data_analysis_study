# 선택 정렬 구현

## 함수
from random import randint
# random 모듈에서 radint 함수를 가져옴
# randint(1,10) : 1부터 10까지의 무작위 정수를 생성
def findMinIndex(ary):  #[78, 121, 132, 136, 144, 43, 106, 44]
    minIdx = 0      # 초기값
    for i in range(1,len(ary)):     # ary는 list 변수testAry = [55,88,33,77]
            #range(1,4)
        if (ary[minIdx]>ary[i]): # step 1 : 0 > 55
            minIdx = i
    return minIdx

## 변수
before = [randint(30,190) for _ in range(8)]
# 30부터 190까지 중 무작위로 8개의 숫자를 가져옴
after = []

print(before)


## 메인
print('정렬전-->',before)


for i in range(len(before)):
    minPos = findMinIndex(before)
    after.append(before[minPos])
    del(before[minPos]) # 
'''
for i in range(8): #0부터 7까지 
    # i=0 첫번째 메인 for 문
    minPos = findMinIndex([78, 121, 132, 136, 144, 43, 106, 44])
    minPos = 43
    after.append(before[minPos])
    del(before[minPos])

    # i=1  
    minPos = findMinIndex([78, 121, 132, 136, 144, 106, 44])
    minPos = 44
    after.append(before[minPos])
    del(before[minPos])

    ***

    # i=1  
    minPos = findMinIndex([144])
    minPos = 144
    after.append(before[minPos])
    del(before[minPos])
'''

print('정렬후-->',after)