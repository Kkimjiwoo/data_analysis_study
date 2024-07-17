'''
원형큐
- 큐의 처음과 끝이 연결된 구조

왼쪽으로 이동 후 front 왼쪽으로 이동( 오버헤드 발생)
rear도 감소

데이터 삽입때 
rear 증가 후 데이터 삽입

원형큐에서 rear과 front의 초기값은 0
'''

## 변수
SIZE = 5  #0,1,2,3,4
queue = [None for _ in range(SIZE)]
front = rear = 0

## 함수
def isQueueFull() :
    global SIZE, queue, front, rear
    if ( (rear+1)%SIZE == front) : # rear이 만약 4라면 5%5=0, front가 0이면, SIZE = 5인 원형큐의 칸은 0,1,2,3,4 이므로 꽉참
        return True
    else :
        return False

def enQueue(data) :
    global SIZE, queue, front, rear
    if (isQueueFull()) :
        print('큐 꽉!')
        return
    rear = (rear+1)%SIZE
    queue[rear] = data

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :        # 원형큐에서 front=rear은 꽉 찼지만 텅 빈걸로 취급
        return True
    else :
        return False

def deQueue() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return
    front = (front+1)%SIZE
    data = queue[front]
    queue[front] = None
    return data

def peek() :
    global SIZE, queue, front, rear
    if (isQueueEmpty()) :
        print('큐 텅~')
        return
    return queue[(front+1)%SIZE]


## 메인
enQueue('화사')
enQueue('솔라')
enQueue('문별')
enQueue('휘인')
print('출구<--', queue, '<--입구')
#
retData = deQueue()
print('손님 이리로 :', retData)
print('출구<--', queue, '<--입구')

retData = deQueue()
print('손님 이리로 :', retData)
print('출구<--', queue, '<--입구')

enQueue('재남')
print('출구<--', queue, '<--입구')

enQueue('정국')
print('출구<--', queue, '<--입구')

enQueue('길동')
print('출구<--', queue, '<--입구')

print('출구<--', queue, '<--입구')

enQueue('재남')
print('출구<--', queue, '<--입구')

enQueue('정국')
print('출구<--', queue, '<--입구')

enQueue('길동')             # 안들어가짐
print('출구<--', queue, '<--입구')