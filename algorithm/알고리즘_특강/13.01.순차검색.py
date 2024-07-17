'''
검색 
: 어떤 집합에서 원하는 것을 찾는 것으로, 탐색이라고도 함
- 순차 검색, 이진검색, 트리검색
- 검색에 실패하면 -1 을 반환하는 것이 일반적

순차 검색
- 검색할 집합이 정렬되어 있지 않은 상태일때
- 처음부터 차례대로 찾아보는 것으로, 쉽지만, 비효율적임
- 집합의 데이터가 정렬되어 있지 않다면 이 검색 외에 특별한 방법 없음
'''
## 함수
from random import randint, choice  # choice 임의의 항목을 선택하여 반환
def seqSearch(ary, fdata) :
    pos = -1        # 찾는 값이 없으면 -1반환
    for i in range(len(ary)) :
        if (ary[i] == fdata) :
            pos = i
            break
    return pos

## 변수
dataAry = [randint(30, 190) for _ in range(8)]
findData = choice(dataAry) # 누나 키

## 메인
print('배열-->', dataAry)
position = seqSearch(dataAry, findData)
if (position != -1) :       
    print(findData,'는 ', position, '위치에 있음.')
else :              # 찾는 값이 없을 때 -1 반환할때
    print(findData, '는 없어요ㅠ')

