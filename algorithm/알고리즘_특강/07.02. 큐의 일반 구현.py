'''큐의 일반 구현'''
# 큐가 꽉 찼는지 그리고 꽉 안찼다면 enQueue에서 왜 데이터 추가가 안되는지 개선 전
# rear 값만 고려해서 꽉 찼는지를 구분함

SIZE = 5
queue = [None for i in range(SIZE)] # SIZE-1까지
front = -1
rear = -1
print(queue)


# 데이터 삽입 과정
# 데이터가 꽉 차있는 지 확인 필수
def isqueuefull():
    global SIZE, front, rear,queue
    if(rear != SIZE-1):
        return False
    elif(front != -1):
        return False
    elif(rear == SIZE-1 and front == -1):
        return True
    
'''
    if (rear >= SIZE-1) :
        return True
    else :
        return False
    
    if (rear != SIZE -1):       # case2 가장 편한 경우
        return False
    elif (rear == SIZE -1 and front == -1):   # case2 진짜 꽉찬 경우
        return True
    elif (rear == SIZE-1 and front != -1):  #else, case3 앞여유가 있는 경우
        for i in range(front+1,SIZE,1):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False
    '''
    
def enqueue(data):
    global SIZE, front, rear, queue
    if isqueuefull():   # 꽉찼다면 삽일할 수 없음
        print('꽉찼어유~')
        return
    
    rear += 1
    queue[rear] = data


# 데이터 추출 과정
# 큐가 비었는지 확인하는 함수
def isqueueempty():
    global SIZE, front, rear, queue
    if(front == rear):
        return True
    else:
        return False

def dequeue():
    global SIZE, front, rear, queue
    if isqueueempty():  # 텅 비었다면 추출을 할 것이 없음
        print("텅 비어서 추출할 데이터가 없습니다.")
        return None
    # 추출하기 전에는 front의 위치를 옮겨야함
    front += 1
    data = queue[front]
    queue[front] = None
    return data

enqueue("지우")
print(queue)
enqueue("지현")
print(enqueue)
enqueue("수진")
print(enqueue)
enqueue("다연")
print(enqueue)
enqueue("유진")
print(enqueue)
enqueue("다은")
print(enqueue)

redata = dequeue()
print(redata,'님의 차례입니다.')

print(queue)

enqueue("다은")
print(enqueue)
# 다은이 채워지지 않음
# 코드 구현할때 rear값만 고려함

        
