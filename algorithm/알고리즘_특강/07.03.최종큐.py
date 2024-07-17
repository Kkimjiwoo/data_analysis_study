'''큐의 일반 구현'''
# 큐가 꽉 찼는지 확인하는 함수 개선

## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if (rear != SIZE-1) : # Case 1 : 가장 해피한 경우
        return False      # WHY? rear이 마지막 인덱스가 아니라는 것은 꽉 차지 않았다는 의미
    elif (rear == SIZE-1 and front == -1) : # Case 2 : 진짜 꽉참
        return True
    elif (rear == SIZE-1 and front != -1) : # else. Case 3 : 앞 여유
        for i in range(front+1, SIZE, 1) : # [none(0), none(1), '다연','지우','다은'] 이때 front는 1
                                           # range(2,5) 인덱스 2부터 4까지 돌겠다 (다연, 지우, 다은)
            queue[i-1] = queue[i]          # 다연을 앞에 있는 칸으로 끌어옴
            queue[i] = None                # None을 해주지 않으면 3명을 앞으로 끌었을때 [다연, 지우, 다은, 다은, 다은] 이 될것이다. 
        front -= 1
        rear -= 1
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear += 1
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return
    return queue[front+1]

## 변수
SIZE = 5
queue = [None for _ in range(SIZE)]
front = rear = -1

## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
enQueue('선미')
print('출구<--', queue, '<--입구')

retData = deQueue()
print('손님 이리로 :', retData)
retData = deQueue()
print('손님 이리로 :', retData)

print('출구<--', queue, '<--입구')

enQueue('재남')
print('출구<--', queue, '<--입구')

enQueue('정국')
print('출구<--', queue, '<--입구')

enQueue('길동')
print('출구<--', queue, '<--입구')
​