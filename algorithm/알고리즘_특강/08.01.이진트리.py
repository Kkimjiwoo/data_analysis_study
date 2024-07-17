'''이진트리의 간단 구현'''
'''
이진트리
- 나무를 거꾸로 뒤집어 놓은 형태
- 모든 노드의 자식이 최대 2개인 트리(자식이 2개 이하로 구성)

부모노드
자식노드: 부모노드 아래에 있는
리프노드: 차수 = 0: 자식

이진 트리의 종류
- 포화이진트리
- 완전이진트리
- 일반이진트리: 부모노드부터 숫자를 셀 때, 자식 노드가 한개 일 때
- 편향이진트리: 왼쪽*오른쪽 편향 이진 트리

이진 팀색 트리 특징
- 왼쪽 서브 트리는 루트 노드보다 모두 작은 값을 가진다
- 오른쪽 서브 트리는 루트 노드보다 모두 큰 값을 가진다.
- 각 서브트리도 위와 같은 특징을 갖는다.
- 모든 노드값은 중복되지 않는다.
즉, 중복된 이진 탐색 트리에 저장할 수 없다
'''
# 높이가 2고 데이터가 6개인 완전 이진 트리 생성

## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

# step 1 빈 메모리를 준비하고, 루트를 none으로 초기화
memory = []
root =None
i = 0
# step 2 배열에 있는 데이터를 이진 탐색 트리에 삽입
nameAry = ['블랙핑크','레드벨벳','에이핑크','걸스데이','트와이스','마마무']
node = TreeNode() # 빈 노드 생성 -> TreeNode() 를 생성하기 위해서는 class 함수를 가져와야 함
node.data = nameAry[i]
i += 1
root = node
memory.append(node)

# step 3 두번 째 이후 데이터 삽입
node = TreeNode()
node.data = nameAry[i]
i += 1
current = root # 위 루트 노드의 값을 current로 함
if node.data < current.data:
    current.left = node
else:
    current.right = node

memory.append(node)



#---------------------------------------------
## 함수
class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None

## 변수

## 메인
node1 = TreeNode()
node1.data = '화사'

node2 = TreeNode()
node2.data = '솔라'
node1.left = node2

node3 = TreeNode()
node3.data = '문별'
node1.right = node3

node4 = TreeNode()
node4.data = '휘인'
node2.left = node4

node5 = TreeNode()
node5.data = '쯔위'
node2.right= node5

node6 = TreeNode()
node6.data = '선미'
node3.left= node6

#print(node1.data)
#print(node2.data,node3.data)
#print(node4.data,node5.data,node6.data)

root = node1
print(root.data)
print(root.left.data,root.right.data)
print(root.left.left.data, root.left.right.data,root.right.left.data)