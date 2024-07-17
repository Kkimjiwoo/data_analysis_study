'''큐의 간단 구현'''
'''
큐
- 큐 자료 구조는 입구와 출구가 따로 있는 원통형태

큐의 구조와 용어
- enQueue(인큐) : 큐에 데이터를 삽입하는 작동
- deQueue(데큐) : 큐에 데이터를 추출하는 작동
- front(머리)   : 저장된 데이터 중 첫 번째 데이터
- rear(꼬리)    : 저장된 데이터 중 마지막 데이터

# 아무 데이터가 없을때 front = rear = -1
데이터를 삽일할 때 (enQueue)
1. rear을 한 칸을 오른쪽으로 이동 rear=0
2. rear 위치에 데이터 추가
데이터를 하나 더 추출할 때
1. rear을 한 칸을 오른쪽으로 이동 rear = 1
2. rear 위치에 데이터 추가

데이터를 추출할 때(deQueue)
1. front를 한 칸 오른쪽으로 이동 front = 0
2. 데이터를 하나 추출 -> 그 자리 None 값으로 변경
'''

## 함수

## 변수
SIZE = 5
queue = [ None for _ in range(SIZE) ]
front = rear =-1

## 메인

## enqueue()
rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'

print('출구 <==',queue,'<==입구')


#dequeue()
front += 1      # 이를 먼저 하는 이유: 1을 더하기 전에는 0, 리스트의 인덱스 값을 추출할 수 없음
data = queue[front] # data라는 변수에 front 값을 대입하는 이유? 
queue[front] = None # 추출하기 위해서는 이 위치의 값을 None으로 변경해줘야 함
print('식사손님==>', data)

front += 1
data = queue[front]
queue[front] = None
print('식사손님==>', data)

front += 1
data = queue[front]
queue[front] = None
print('식사손님==>', data)

print('출구<--', queue, '<--입구')