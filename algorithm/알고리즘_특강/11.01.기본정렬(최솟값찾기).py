'''기본 정렬 알고리즘의 원리와 구현'''
'''
정렬
- 중요 알고리즘 중 하나인 정렬은 자료들을 일정한 순서대로 나열

정렬 알고리즘의 종류
- 선택 정렬(Selection Sort)
: 여러 데이터 중에서 가장 작은 값을 뽑는 작동을 반복하여 값을 정렬
- 삽입 정렬(Insertion Sort)
- 버블 정렬(Bubble Sort)
- 퀵 정렬(Quick Sort)
'''
## 최솟값을 찾는 방법

## 함수
def findMinIndex(ary):
    minIdx = 0      # 초기값
    for i in range(1,len(ary)):     # ary는 list 변수testAry = [55,88,33,77]
            #range(1,4)  1부터 3까지
        if (ary[minIdx]>ary[i]): # step 1 : 55>88 => False => minIdx = 0 
                                 # step 2 : 55>33 => Ture => minIdx = 2
                                 # step 3 : 33>77 => False => minIdx = 2  
            minIdx = i
    return minIdx       # minIdx = 2
## 변수 
testAry = [55,88,33,77]

## 메인

minPos = findMinIndex(testAry)  # 사용자 정의 함수
print('최솟값->', testAry[minPos])