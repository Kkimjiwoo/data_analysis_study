'''단순 연결 리스트'''
'''
단순연결리스트 : 노드 구조
- 단순 연결 리스트는 다음 데이터를 가리키는 링크가 더 필요
- 노드는 데이터와 링크로 구성된 항목
'''
## 함수
# 클래스라는 문법을 사용하여 Node 데이터형 정의
class Node() :              # Node 라는 데이터형을 만듦
    def __init__(self):     # 인스턴스(데이터형)가 생성될 때마다 자동으로 호출됨
        self.data = None    # 노드의 데이터를 저장하는 속성 
        self.link = None    # 다음 노드를 가리키는 링크를 저장하는 속성
        # 초기값은 None
## 변수

## 메인
# 첫 번째 노드를 생성하기 위한 코드
node1 = Node()          # 노드 생성
node1.data = '다현'     # 노드에 데이터 삽입

node2 = Node()
node2.data = '정연'
node1.link = node2      # 첫번째 노드의 링크에 두 번째 노드를 넣어 연결

node3 = Node()
node3.data = '쯔위'
node2.link = node3

node4 = Node()
node4.data = '사나'
node3.link = node4

node5 = Node()
node5.data = '지효'
node4.link = node5

print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
print(node1.link.link.link.link.data, end=' ')

#노드 삽입 과정
# node2 뒤에 삽입하고 싶을때 
newNode = Node()
newNode.data = '재남'        # 데이터를 '재남'으로 설정
newNode.link = node2.link    # newNode를 node2링크와 동일하게 설정
                             # if 두번째 뒤에 삽입하고 싶다면 두번째 링크를 카피해야함
node2.link = newNode         # node2링크를 새 노드에 카피하고, node2 링크를 수정해야함
''' 재남의 삽입 여부 확인 코드
print(node1.data, end=' ')
print(node1.link.data, end=' ')
print(node1.link.link.data, end=' ')
print(node1.link.link.link.data, end=' ')
'''

# 삭제 
# node3를 삭제하고 싶을때
node2.link = node3.link        # node2 링크에 node3 링크를 대입
# 즉 node2 링크는 node4에 연결한다.
del(node3)

'노드의 처음부터 끝까지 출력하는 함수'
# 데이터가 5개인 단순 연결 리스트 생성

# step 1 첫 번째 노드를 현재 노드로 지정
current = node1
print(current.data, end=' ')
# step 2 현재의 노드 링크가 비어 있지 않다면,  
while (current.link != None) :  # 현재의 노드의 링크가 비어 있으면 종료, 아닐 시 반복
    current = current.link
    # 현재 노드의 링크가 가리키는 노드를 변경
    print(current.data, end=' ')

