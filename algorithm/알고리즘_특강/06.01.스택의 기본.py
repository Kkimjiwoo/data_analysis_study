'''
STACK 스택
- 스택 자료구조는 한쪽 끝이 막힌 형태
- 입구가 하나이기 때문에 먼저 들어간 것이 가장 나중에 나오는 구조

스택의 기본 구조
- push: 스택에 데이터를 삽입하는 작동
- pop: 스택에 데이터를 추출하는 작동
- top: 스택에 들어있는 가장 위의 데이터

스택의 초기값top은 -1(스택이 텅 비워져 있다는 의미)
top에 따라 스택이 어디까지 쌓여있는 지를 알수 있다.
top =2 => 스택이 3까지 쌓여져 있음

스택을 한 칸 늘린 후에 리스트에 데이터를 삽입 
'''
## 함수

## 변수
# 스택 생성: 배열 크기를 지정한 후 빈 스택 생성
stack = [None, None,None, None,None]
top = -1            # 스택이 하나 쌓이면 top = 0 : 인덱스 또한 0으로 시작

## 메인
# push
top += 1                # top을 한 칸 늘린 이후에 
stack[top] = '커피'     # stack 리스트에 데이터 삽입    

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print('바닥:',stack)

# pop
data = stack[top]        # 데이터라는 변수에 스택의 top를 추출
stack[top] = None        # top의 값을 None으로 대체
top -= 1                 # top을 한 칸 아래로 = 채워진 스택의 개수
print('팝--> ',data)     # data, 즉, 추출한 데이터 표시

data = stack[top]
stack[top] = None 
top -= 1 
print('팝--> ',data)

data = stack[top]
stack[top] = None 
top -= 1 
print('팝--> ',data)