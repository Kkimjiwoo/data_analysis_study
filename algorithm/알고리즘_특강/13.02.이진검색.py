'''
이진 검색
- 데이터가 정렬되어 있다면 이진 검색도 가능
- 순차 검색에 비해 월등히 효과적이라 데이터가 몇 천만개 이상이어도 빠르게 찾아낼 수 있음

이진검색은 전체를 반씩 잘라 내서 한쪽을 버리는 방식을 사용
'''
## 함수
from random import randint, choice
def binSearch(ary, fdata) :
    pos = -1
    start = 0
    end = len(ary)-1        # index
    while (start <= end) :  # start는 mid 값 전에 찾는 값이 없다면 mid+1로 증가할 것이다
                            # 그렇게 계속 증거하면 end
        mid = (start + end) // 2      # 소수점없음
        if (ary[mid] == fdata) :
            pos = mid
            break
        elif (ary[mid] < fdata) :     # 숫자이기 때문에 가능 # 중간지점의 뒷 부분을 확인 
            start = mid + 1     # 중간지점에 없다는 것을 확인했고, start 지점을 mid+1로 바꿔야함
                                # end = len(ary)-1
        else :      # mid 포함 mid의 뒷부분에 찾는 값이 없다는 의미 
            end = mid - 1  # 끝을 중간의 mid-1로 잡는다 # 이때 start = 0
    return pos

## 변수
dataAry = [randint(30, 190) for _ in range(10)]
dataAry.sort()
findData = choice(dataAry) # 할머니 키
# findData = 77

## 메인
print('배열-->', dataAry)
position = binSearch(dataAry, findData)
if (position != -1) :
    print(findData,'는 ', position, '위치에 있음.')
else :
    print(findData, '는 없어요ㅠ')
