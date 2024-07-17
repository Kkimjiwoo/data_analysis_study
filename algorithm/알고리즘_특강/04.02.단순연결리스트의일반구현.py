# 단순 연결 리스트 구현
# 노드 삽입, 노드 삭제, 노드 검색등을 사용자 정의 함수를 이용하여 동작을 구현함

## 함수
# (연결리스트의 생성)
class Node() :              # Node라는 데이터 형을 만드는 것


    # 데이터 형을 생성할 때 자동으로 실행되는 부분
    def __init__(self):     
        self.data = None    # 테이터와 링크가 저장되는 부분
        self.link = None    # 테이터와 링크가 저장되는 부분


# 데이터 link연결
def printNodes(start) :
    current = start
    # current 변수를 start로 초기화 함, 이는 출력을 시작할 노드를 가리킴
    # 이때 start 를 head로 받으면 처음부터 시작
    print(current.data, end=' ')     # current 데이터를 출력
    while (current.link != None):    # link로 연결이 되어 있다면 실행
    # 연결리스트의 끝까지 실행
        current = current.link       # 각 노드의 데이터를 출력한 후, current를 다음 노드로 이동
        print(current.data, end=' ')     
    print() # 연결리스트의 끝에 도달하면 마지막 노드의 데이터를 출력한 후, 줄바꿈 
#------------------------------------------------------------
#### 단순 연결 리스트의 일반 형태
## 변수
memory = []  # 안 중요!
head, pre, current = None, None, None
# 처음에는 모두 비어 있으면 되므로 초기화
dataArray = ['다현','정연','쯔위','사나','지효'] #데이터

## 메인
'''
데이터 입력 과정
- 빈노드 생성
- 데이터 입력 
- 첫번째 노드를 헤드로 지정
- 노드를 빈 변수인 memory에 넣음
'''
node = Node()
node.data = dataArray[0]
head = node
memory.append(node) # 무시해도 됨

for data in dataArray[1:]: # [정연, 쯔위,..., 사나, 지효]   # 쯔위
    pre = node# 기존 노드를 임시 저장
    # 처음에 pre는 head와 같은 위치
    node = Node()       # 빈 노드 생성
    node.data = data    # 데이터 입력
    pre.link = node     # 연결데이터 생성(첫번째 프리의 링크에 노드를 넣어)
    memory.append(node) # 새 노드를 메모리에 넣음

'''
current = head
print(current.data, end=' ')
while (current.link != None) :
    current = current.link
    print(current.data, end=' ')
print()
'''
printNodes(head)


 
#---------------------------------------------------------

# 노드 삽입
# ~누구 앞에 삽입
def insertNode(finddata, insertdata):
    global memory, head, pre, current
    # case 1 : 하필 머리 앞에 삽입하기 (다현, 화사)
    if (finddata == head.data):
        node = Node() # 빈칸 만들기
        node.data = insertdata
        node.link = head        # node 링크를 head에 연결
        head = node             # head를 노드로 변경
        memory.append(node)     # 안중요 무시 가능
        return
    # case 2 : 중간 노드 앞에 삽입(사나, 솔라)
    current = head
    while (current.link != None) :      # current에 연결이 되어 있다면 계속 실행
        pre = current   # pre는 head에
        current = current.link   # 정연으로 감
        if(current.data == finddata):
            node = Node()
            node.data = insertdata 
            node.link = current     # node의 링크에 current를 넣어 연결
            # 이때 pre도 current에 node도 current에 연결되어 있음
            pre.link = node # pre의 링크 수정/ pre의 링크에 노드를 연결하여 수정
            memory.append(node)
            return
    # case 3: 없는 노드 앞에 삽입 => 마지막에 삽입해라
    node = Node()
    node.data = insertdata
    current.link = node # 변수 안 마지막 데이터는 current일 것이다, 앞에 조건을 돌고 왔다면
                        # current의 연결에 추가한 노드를 연결하면 마지막에 연결
    memory.append(node)  # 안 중요
    return

## 노드 삭제 함수
def deleteNode(deleteData):
    global memory, head, pre, current
    # case 1 : 하필 머리 삭제 (다현)
    if (deleteData == head.data):  
        current = head          # 현재 노드(current)를 삭제할 노드인 헤드(head)와 동일하게 만듦
                                # 현재 노드를 삭제할 것이다.
        head = head.link        # head를 삭제할 노드(다현 노드)의 링크가 가리키던 정연 노드로 변경
                                # head의 링크는 헤드의 다음 노드
        del(current)            # 현재 노드를 메모리에서 제거
        return
    # case 2 : 중간 노드를 삭제(쯔위)
    current = head              # 헤드에서 시작
    # 언제 까지 찾냐?
    while (current.link != None):       # 어떠한 조건이 나올때 까지 이 코드를 반복할 것인지를
        pre =  current      # pre를 선언해주는 이유? 
                            # 삭제를 하게 되면, 그 삭제 노드의 전 노드가 그 다음 노드와 연결이 되야함
        current = current.link #  다현 => 정연  
        if (current.data == deleteData):   #  delectData가 정연이라면 
            pre.link = current.link        # 다현.link = 정연.link
            del(current)
            return
    # case 3 : 없는 노드를 삭제(재남)
    return

## 노드 검색 함수
# 검색할 데이터를 찾지 못한다면 None을 반환
def findNode(findData):
    global memory, head, pre, current
    current = head # 현재는 head부터
    if(findData == current.data):
        return current
    while(current.link != None):
        current = current.link
        if(findData == current.data):
            return current
    return Node()       #연결 리스트 안에 찾는 데이터가 없을 때 빈 노드를 반환




insertNode('다현','화사')
printNodes(head)    # 시작은 head부터
#insertNode('사나','솔라')
#printNodes(head)
#insertNode('재남','문별')
#printNodes(head)

#deleteNode('다현')
#printNodes(head)

#deleteNode('쯔위')
#printNodes(head)

#deleteNode('쯔위')
#printNodes(head)

retNode = findNode('사나')
print(retNode.data,'의 뮤비가 플레이 됩니다') 