# 스택의 일반 구현

## 변수
SIZE = 5           # 5개짜리 빈 스택을 생성하는 코드
stack = [None for _ in range(SIZE)]
top = -1
print(stack)

## 함수
#  스택이 꽉 찼는지 확인하는 함수
def isStackFull() :
    global SIZE, stack, top
    if (top == SIZE-1) :
        return True
    else :
        return False

# 스택에 데이터를 삽입하는 함수
def push(data) :
    global SIZE, stack, top
    if (isStackFull()) :
        print('스택 꽉!')
        return
    top += 1
    stack[top] = data

# 스택이 비었는지 확인하는 함수
def isStackEmpty() :
    global SIZE, stack, top
    if (top == -1) :
        return True
    else :
        return False

# 스택에서 데이터를 추출하는 함수
def pop() :
    global SIZE, stack, top
    if (isStackEmpty()) :   # True 이다면, 텅 비었다면, 
        print('스택 텅~')
        return
    data = stack[top]
    stack[top] = None   # 추출을 하면 그 칸은 빈칸이 되므로 None을 해줘야 함
    top -= 1    # 스택이 추출되면 top도 한 칸 줄어들어야 하므로
    # stack을 추출한 후에 시행해야함
    return data

# top위치의 데이터를 확인하는 함수
def peek():
    global SIZE, stack, top
    if (isStackEmpty()):   # if(isStackEmpty()==true)
        print('스택 텅~')
        return None
    return stack[top]



## 메인
push('커피')
push('녹차')
push('꿀물')
push('콜라')
push('환타')
print('바닥:', stack)

push('게토레이')
# print('바닥:', stack)

retData = pop()
print('팝-->', retData)

searchData = peek()
print('다음예정-->', searchData)

retData = pop()
print('팝-->', retData)

retData = pop()
print('팝-->', retData)
print('바닥:', stack)

