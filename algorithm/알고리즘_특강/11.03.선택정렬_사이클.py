'''
선택정렬- 사이클

두 변수 값 교환
- 알고리즘을 구현할 때는 두 변수 값을 교환해야 하는 경우가 종종 생기는데, 
원칙적으로 한 번에 두 변수의 값을 교환할 수 없으므로, 임시공간을 사용함
임시공간 -> temp
'''
## 함수
from random import randint
def selectSort(ary) :
    n = len(ary) # 전체 데이터 개수  # 20개
    for i in range(0, n-1, 1) : # 사이클 (큰 회전) 
                                # -> 0부터 19까지 있다면 큰 회전은 18까지 돌려야함
        minIdx = i  # 0
        for j in range(i+1, n, 1) : # for j in range(1,20)
                                    # 큰 회전과 달리 range( ,20) 20으로 잡은 이유
                                    #마지막에는 n-1(즉, n-2) 인덱스의 값은 n(즉, n-1)의 값과 비교해야 함함 
            if (ary[minIdx] > ary[j]) :
                minIdx = j
        #ary[i], ary[minIdx] = ary[minIdx], ary[i]
        temp=ary[i]
        ary[i]=ary[minIdx]
        ary[minIdx]=temp

    return ary

## 변수
dataAry = [randint(30, 190) for _ in range(20)]

## 메인
print('정렬 전-->', dataAry)
dataAry = selectSort(dataAry)
print('정렬 후-->', dataAry)
​