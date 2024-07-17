
'''
리스트
- 순서대로 index 값을 관리하고, 값을 수정하는 자료구조
- 리스트 + 리스트 = 합쳐짐
"""

# 문자열 리스트 + 문자열 리스트는 연결
# 숫자형 리스트 + 숫자형 리스트는 덧셈
# but, 숫자형 리스트 + 문자열 리스트 -> 에러 발생

a=[1,2,3]
a*3
print('a*3 =>', a*3)
# 위치 지정 후 리스트 추가
a[2]=99
print('a[2]=99 =>',a)
a[1:2]=['a','b','c']
print("a[1:2]=['a','b','c'] =>",a)
a[-1]=['d','e','f']
print("a[-1]=['d','e','f'] =>", a)
del a[-1]
print("del a[-1] =>", a)
# 리스트 추가
a.append(5)
print('a.append(5) =>', a)
b

b = ['Life','is','too','short']
# 대문자 A => 67, 소문자 a  => 97
# 대문자 A가 더 작은 숫자이므로 앞에 배열

b.sort()
b
# 작은 숫자에서 큰숫자로

"""3차시"""

# 나눗셈의 주의 사항
'''
- 숫자 0을 어ㄷ
'''

"""나눗셈의 주의사항
- 숫자 0을 어떤 수로 나누어도 결과는 항상 0임
- 숫자를 0으로 나눌 수 없음
- 나눗셈 결과 나머지가 없는 경우에도 항상 실수임
- 결과값의 자료형이 정수형이길 원한다면 직접 자료형 변환을 해야함 ex) type (int(10/2))
-  나머지가 있는 경우에 정수로 자료형 변환을 하면 소수점 이하의 데이터는 손실됨

나머지 구하기 -> %

몫 -> //

거듭제곱 -> **  ex) 2**3 =2*2*2
"""

import keyword # kewoord,py를 가져온다.
print(keyword.kwlist)

s = 'Now is better than Never'
#  01234 # index 는 0부터 시작
s2 = s[0]+s[1]+s[2]
s2

# index 뒤에서 부터 접근
s3 = s[-3]+s[-2]+s[-1]
s3

# 슬라이싱 now 를 얻고싶을 때
s[0:3]

s[:3] # 인덱스 0부터 2까지

s[4:] # 뒤의 숫자를 생략하면 끝까지

"""4차시

자료구조정리
1. 인덱스 사용 가능
- 문자열 - 원소값 변경 불가능
- 리스트[] - 원소값 변경 가능
- 튜플() - 원소값 변경 불가능
2. 인덱스 사용 불가능
- 딕셔너리{} - 원소값 변경 가능
- 집합() - 원소값 변경 가능

5주차 리스트 자료형

리스트
- 순서대로 index 값을 관리하고, 값을 수정하는 자료구조
- 리스트 + 리스트 = 합쳐짐
"""

# 문자열 리스트 + 문자열 리스트는 연결
# 숫자형 리스트 + 숫자형 리스트는 덧셈
# but, 숫자형 리스트 + 문자열 리스트 -> 에러 발생

a=[1,2,3]
a*3
print('a*3 =>', a*3)
# 위치 지정 후 리스트 추가
a[2]=99
print('a[2]=99 =>',a)
a[1:2]=['a','b','c']
print("a[1:2]=['a','b','c'] =>",a)
a[-1]=['d','e','f']
print("a[-1]=['d','e','f'] =>", a)
del a[-1]
print("del a[-1] =>", a)
# 리스트 추가
a.append(5)
print('a.append(5) =>', a)
b

b = ['Life','is','too','short']
# 대문자 A => 67, 소문자 a  => 97
# 대문자 A가 더 작은 숫자이므로 앞에 배열

b.sort()
b
# 작은 숫자에서 큰숫자로

"""리스트 길이 조회
len() 함수
- 위의 함수로 리스트의 길이 확인 가능
- 리스트 길이 외 문자열의 길이도 확인 가능
"""

len('python')

# for문을 이용한 리스트 전체 조회
balls =['야구공','축구공','탁구공','골프공','농구공']
for item in balls:
  print('item : ',item)

# enumereate()함수를 이용하여 아이템을 조회할때 인덱스도 출력 가능
# enumereate() 함수는 인덱스와 아이템을 반환 -> 리스트, 튜플, set에 이용 사능
balls =['야구공','축구공','탁구공','골프공','농구공']
for index, item in enumerate(balls):
  print('index : ',index,'item : ',item)

# while 문을 이용한 리스트 전체 조회
# len()함수를 이용하여 리스트 전체 아이템을 조회
balls =['야구공','축구공','탁구공','골프공','농구공']

i = 0 # 초기값 설정

while i < len(balls):
    print(balls[i])
    i+=1

# 리스트, 튜플, 셋, 딕셔너리  등의 자료구조가 나온다면 반복문으로 처리

# index() 함수
# 리스트에서 특정 아이템의 인덱스 값을 조회하는 함수
# index() 함수의 괄호 안에 아이템을 넣어주면 해당 인덱스 값을 출력
num=[10,20,30,40,50]
num.index(20)

# 조회하려는 아이템이 2개 이상인 경우 가장 앞에 있는 인덱스 값이 출력
num=[10,20,30,40,50,10]
num.index(10)

# append()함수
# 리스트 끝에 아이템을 추가하는 함수
# 새로운 아이템이 리스트 마지막에 추가되고 그에 따라 인덱스도 1 증가함
num=[10,20,30,40,50]
num.append(10)
num

# insert() 함수
# 리스트의 원하는 위치에 아이템 삽입하는 함수
num=[10,20,30,40,50]
num.insert(1,10)
num

# extend() 함수
# 리스트에 또 다른 리스트를 연결하는 함수
# 함수 안에 연결할 리스트 이름을 넣어줌
num=[10,20,30,40,50]
num2=[60,70,80]
num.extend(num2) # num에 num2를 붙임
num

# + 기호 이용
num=[10,20,30,40,50]
num2=[60,70,80]
num = num + num2
num

a = 'hello '+'jiwoo'
a

# pop()함수
# 리스트 맨 끝에 아이템을 삭제하는 함수
# 함수 괄호는 빈 채로 둠
# 삭제함으로써 리스트 변경

# pop() 함수
# pop() 함수의 괄호 안에 삭제할 인덱스를 넣으면 그 인덱스에 있는 아이템이 삭제됨

# del()
# >> pop 함수와 del함수 모두 리스트의 모양에 영향을 줌

# remove()
# pop와 del에 인덱스를 넣었다면 remove에는 특정 아이템을 넣어 삭제함
# 중복된 아이템의 경우 앞에 있는 아이템 삭제

# 리스트에 특정 아이템 여러 개를 모두 찾아서 삭제하는 경우
# for문 이용
num=[10,20,30,10,40,50,10]
print(num)

for i in num:
  if i == 10:
      num.remove(10)

print(num)

# 리스트에 특정 아이템 여러 개를 모두 찾아서 삭제하는 경우
# while문  이용
num=[10,20,30,10,40,50,10]
print(num)

while 10 in num:
    num.remove(10)
print(num)

# sort() 함수
# 리스트의 아이템을 정렬하는 함수
# reverse 옵션이 false면 오름차순, true면 내림차순
# 기본값 오름차순
num=[40,80,60,10,30]
num.sort(reverse = True)
num

# reverse() 함수
# 아이템을 역순으로 뒤집는 함수
vegetables =['당근','오이','양파','감자','고구마']
vegetables.reverse()
vegetables

a=[2,1,0,2,3,2,4,2]

a.count(2) # 2의 값이 몇개 인지

"""6차시

튜플 Tuple 자료형
- 리스트와 비슷하게 데이터를 묶어서 처리하는 컨테이머 자료형
- 튜플에 포함된 아이템을 수정할 수 없음
- 데이터가 수정되면 안되는 예: 회사의 급여 명세서

튜플  tuple
- 순서대로(index) 값을 관리하나 값은 변경 불가인 자료 구조
- 괄호를 이용하여 튜플 생성
- 한개만 저장할 경우에도 쉼표를 넣어야 함
- 괄호를 생략하여 정의할 수 있다.
- 튜플 안에 리스트 형태의 다른 데이터 저장 가능
"""

fruits = ('사과','포도','수박','참외','배','자두','복숭아','바나나')
fruits

type(fruits)

"""튜플의 아이템 조회
- 튜플은 아이템의 수정이 불가능-> 아이템의 삽입, 삭제, 정렬 등의 기능은 없고 조회기능만 주로 사용함
- 인덱스를 이용하여 아이템에 접근
"""

fruits = ('사과','포도','수박','참외','배','자두','복숭아','바나나')
print(fruits[3])
print(fruits[len(fruits)-1])  # 마지막 인덱스

t1 =(1,)  # 불변 : 수정 불가
t2 =(1,2,3)
t3 =1,2,3
t4 =(1,2,(3,4),('Life','is'))

t4[0]
print('t4[0] =>',t4[0])
t4[3][-1]
print('t4[3][-1]] =>',t4[3][-1])
t4[0:3]
print('t4[0:3] =>',t4[0:3])
t1+t2
print('t1+t2=>',t1+t2)

# index()함수
# 튜플 내 특정아이템의 인덱스 조회할 때 사용하는 함수
fruits = ('사과','포도','수박','참외','배','자두','복숭아','바나나')
print(fruits.index('포도'))
print(fruits.index('바나나'))

# 아이템이 있는지 확인 in
fruits = ('사과','포도','수박','참외','배','자두','복숭아','바나나')
print('참외'in fruits)

# 아이템이 없는지 확인 not in
fruits = ('사과','포도','수박','참외','배','자두','복숭아','바나나')
print('귤' not in fruits)
print('수박' not in fruits)
# not in -> djqt으면 true 있으면 false

# +연산자
t1 =(1,2,3)
t2 =(10,20,30)
sumT = t1+t2
sumT

# Extend() 함수는 튜플에서 사용할 수 없다
t1 =(1,2,3)
t2 =(10,20,30)
#t1.extend(t2)
# 'tuple' object has no attribute 'extend'

# 튜플 -> 리스트 : 튜플의 아이템을 수정하기 위해 변환
# 리스트 -> 튜플 : 리스트로 선언된 데이터를 수정이 안되게 하기 위해 변환
colors = ('red','orange','yellow','green','blue','indigo','purple')
print('colors의 자료형 :',type(colors))

# 튜플을 리스트로 데이터 타입 변
colors = list(colors)
print('colors의 자료형 :',type(colors))

# 리스트를 튜플로 데이터 타입 변환
colors = tuple(colors)
print('colors의 자료형 :',type(colors))

"""튜플의 아이템 정렬 sorted()
- 튜플은 아이템을 수정할 수 없기 때문에 기본적으로 정렬이 불가능함
- 내장함수 sorted()를 이용하면 튜플도 정렬가능
- 반환되는 데이터 리스트
"""

colors = ('red','orange','yellow','green','blue','indigo','purple')
print(colors)
print('정렬 후: ',sorted(colors))
print('자료형: ',type(sorted(colors)))
# 오름차순으로 정렬한 리스트를 반환
# sorted의 결과물은 리스트

# 튜플과 문자열을 더할 수 없다 >> 에러
# t1 + 'hi jiwoo'

t2*3
# 3번 반복

#t2[2] = 99
# 튜플은 불변이기에, 값이 변하지 않는다
# 불변 : 수정을 시도하면 에러 발생

"""6주차

딕셔너리
- 키와 값의 쌍으로 관리하며, 순서는 없음(정확히는 순서가 보장되지 않음)
- 키와 값을 갖는 딕셔너리 생성
- 기존의 딕셔너리에 키와 값을 추가하는 경우 D4['park']='대구'
- 키에는 문자열, 정수 등이 올 수 있고, 값에는 리스트, 튜플, 딕셔너리, 정수, 실수 등이 올 수 있다.
"""

dic0 = {'이름':'지우','나이':25,'주소':'시흥대로','취미':['축구','야구','탁구'], '몸무게':85.3}
dic0

print(dic0['나이'])
print(dic0['취미'])

# 딕셔너리 추가
# 새로 추가하는 키는 기존에 있던 키와 중복되어서는 안 됨
# 만약 중복되면 저장되어 있는 값이 바뀜
dic0 = {'이름':'지우','나이':25,'주소':'시흥대로','취미':['축구','야구','탁구'], '몸무게':85.3}
dic0['형액행'] = 'o형'
dic0

# 나이를 수정할 때
dic0['나이'] = dic0['나이'] + 1
dic0

# 딕셔너리 제거
# 1 이라는 key를 가진 value을 제거
del dic0['몸무게']
dic0

# key를 통해 값을 찾고 싶을 때
dic0['이름']

# key와 value를 뽑고싶을 때
print(dic0.keys())  # 전체 키 조회
print(dic0.values())  # 전체 값 조회
print(type(dic0.keys()))

# key를 list의 형태로 바꾸고 싶을 때
a = list(dic0.keys())
print(a)
print(type(a))

list(dic0.values())

# 반복문으로 출
# keys() 함수로 조회한 키와 for문을 이용하여 각 키에 해당하는 값 출력
dic0 = {'이름':'지우',
        '나이':25,
        '주소':'시흥대로',
        '취미':['축구','야구','탁구'],
        '몸무게':85.3}

for i in dic0:
  print (i,'\t:',dic0[i])


# \n 줄 바꿈//\t 탭

# 키와 값을 한번에 사용하고 싶을 때
# 튜플 형태로, 반복문에서 사용 가능
dic.items()

#  딕셔너리의 모든 내용을 지우고 싶을 때
dic.clear()
dic

"""8차시

집합 set
- 각 키는 유일해야 하며, 어떤 것이 존재하는지만 판단할 때 셋을 사
- 집합은 중복을 허용하지 않는 데이터 구조이며 순서도 없음(순서가 보장되지 않음)
- 빈 집합을 생성할 때는 set()함수를 사용해야 한다 s1 = set()
- 값을 가지고 생성 s1 = {1,2,3}
- 중복을 허용하지 않기 때문에 요소는 하나씩만 저장됨
- 다른 자료 구조를 set으로 변경 가능( 튜플>>set)
- >>set이라는 함수를 통해 중복을 제거함
"""

# set 집합 생성하는 법
s1 = {1,2,'a',5}    # 중괄호 안에 콤마로 구분된 값을 넣으면서
s2 = set([1,2,3,4,5,6])   # set()함수를 사용하
s2

# 리스트를 집합set으로 변경 가능
s3 = set([4,5,6,7,8,9])
s3

# 교집합 &
s2&s3

# intersection : 교집합
s2.intersection(s3)

# 합집합 |  > 중복은 사라짐
# |는 or
s2 | s3

# union : 합집합
s2.union(s3)

# 차집합 -
s2 - s3

# difference차집합
s2.difference(s3)

# difference차집합
s3.difference(s2)

"""셋 컴프리헨션
- 표현식 for 표현식 in 순회가능한 객체
- 표현식 for 표현식 in 순회가능한 객체 if테스트
"""

# misson: 리스트 L의 각 요소들을 제곱한 값들을 저장해서 출력하는 실습
# set표현식, 리스트 표현식과 비슷
# 최종결과 {1,4,9,16,25}
L=[1,2,3,4,5]
s = set()

for i in L:
    c = i**2
    s.add(c)

s

# 셋컴프리헨션
s2={ i**2 for i in L}
s2

# 7을 추가
s2.add(7)
s2

# update를 통해 한번에 집합 set에 넣기 가능
s2.update([6,7,8,9,10])
s2

# 7을 삭제하고자 할때
s2.remove(7)
s2

# set을 사용하는 목적
# L과 같은 리스트가 존재한다면 set으로 변환시켜 중복을 제거하는 형태
L=[1,1,2,2,3,4,4]
S1 =set(L)
S1

# 리스트 3개 준비
m=['korea','japan','toronto']
k=['jinju','seoul','changwon']
s=['ottawa','chicago','la']

# 리스트를 요소가 갖는 튜플
# 튜플의 경우 괄호 또는 무괄
tupleoflist = m,k,s
tupleoflist

# 리스트를 리스트로 갖는 리스트
listoflist = [m,k,s]
listoflist

# 리스트를 갖는 딕셔너리
dictoflist={'m':m,'k':k,'s':s}
dictoflist

# 리스트의 각 요소들을 연결해서 문자열로 만드는 실습
str1=""
str2=""
str3=""
for i in dictoflist:
   if i == 'm':
        L1 = dictoflist[i]
        print('L1:',L1)
        for i in L1:
          str1+=i + ' '
   elif i == 'k':
        L2 = dictoflist[i]
        print('L2:',L2)
        for i in L2:
          str2+=i + ' '
   elif i == 's':
        L3 = dictoflist[i]
        print('L3:',L3)
        for i in L3:
          str3+=i + ' '
print('str1 : ',str1)
print('str2 : ',str2)
print('str3 : ',str3)

"""9차시
불 자료형, 변수관리
"""

# 논리 연산자
'''
- 피연산자의 논리 자료형 True False을 이용하는 연산자로 and, or, not이 있음
and 연산자: 피연산자가 모두 True인 경우에만 결과가 True
 or 연산자: 피연산자 중 하나라도 True라면 결과값은 True
'''

# or 연산의 주의사항
# 초기화하지 않은 변수 abc를 출력하면 에러 발생
'''
num = 10
abc   # name 'abc' is not defined

(num>5) or abc
num>5가 true이므로 결과값이 정상적으로 출력됨
'''

(num>5) or abc
#um>5가 true이므로 결과값이 정상적으로 출력됨

# 문자형을 논리형으로 변환
# 빈 문자("")는 False
# 그외 공백 포함 나머지 문자는 True로 반환

# 문자열을 논리형으로 변환
str1=""
print(type(str1))
var = bool(str1)
var

str2=" "
print(type(str2))
var = bool(str2)
var

# 데이터 복사
# 할당연산자 = 을 이용하면 변수에 저장된 데이터를 다른 변수에 쉽게 복사 가능

var1 = 123
var2 = var1
print(var1)
print(var2)

# input()함수
# 사용자에게 데이터를 입력 받을 때 사용하는 함수
# input() 함수로 사용자에서 입력 받은 데이터를 userData 변수에 저장

userData = input()
print(userData)

a = input('인사말을 입력하세요')
a # 입력 받은 값은 모두 str

"""10차시 프로그램 제어(제어문)"""

# 호프집에서 입장 여부 실습
age = int(input('나이를 입력하세요: '))
if age >= 20 :
    print("호프집에 입력하실 수 있습니다.")
else :
    print('당신의 나이는 %.0f이군요. 20살 이상이 입장할 수 있어요.'%age)

'''
score = int(input('점수를 입력하세요'))
while score >100 and score<0:
  score = int(input('점수를 입력하세요'))
break

if score >=90:
    grade = 'A'
elif score >=70:
    grade = 'b'
elif score >=50:
    grade = 'C'
elif score >=40:
    grade = 'D'
else:
    grade = 'F'\


  print('당신의 학점은 %s입니다.'%grade)
'''
# break 문은 while 루프 안에 있어야 한다,
# 위의 조건은 항상 거짓

# WHILE 문 적는 법 확실히 하기

while True:
    score = int(input('점수를 입력하세요'))
    if score <=100 and score>=0:
        break

if score >=90:
    grade = 'A'
elif score >=70:
    grade = 'B'
elif score >=50:
    grade = 'C'
elif score >=40:
    grade = 'D'
else:
    grade = 'F'\


print('당신의 학점은 %s입니다.'%grade)

'''
# 숫자 맞히기 게임
import random

def number():
  secret = random.randint(1,100)

  while True:
      user = input('숫자를 입력하세요(1에서 10 사이, 종료를 원하면"종료")')
      if user =='종료':
        print('게임을 종료합니다. 정답은 {}입니다'.f(secret))
        break

      if int(user)>0 and int(user)<=100:
        break

  if
'''

# while 문 실습
# 구조 : 1. 초기값 설정, 2. 조건, 3. 증감
i = 1
while i <10:
  print(i)
  i+=1

#break 실습
for i in range(10):
    if i == 5:
        break
    print(i)

# continue 실습
for i in range(10):
    if i ==5: continue
    print(i)
print('end')

"""13차시"""

# for 문
## 일반적으로 for 문은 어디서부터 어디까지 반복해서 처리하는 경우에 사용
## 리스트 내포방식으로 사용

# 1~10 사이의 정수를 출력하되, 정수의 3의 배수이면 3의 배수 출력하기
for i in range(1,11):
  print('num = ',i)
  if i%3 == 0:
    print("3의 배수")

# 1~10까지 합
# for 문
sum = 0
for i in range(1,11):
    sum+=i

print(sum)

# while 문
sum=0
num=1
while num < 11:
  sum +=num
  num +=1
print(sum)

# 이터러블에 문자열을 넣는 경우
for i in "hello":
  print (i)

# 1-5까지 정수를 순차적으로 출력하기
# for 문
for i in range(1,6):
  print(i)

# while 문
num = 1
while num <6:
  print(num)
  num+=1

# 중첩 반복문을 이용하여 별(*) 찍기
# 1행에는 1개 ~5행에는 5개

for j in range(1,6):
    print('*'*j)

#################

for i in range(1,6):
  for j in range(0,i):
    print('*',end='')
  print()

"""14주차"""

# 함수 만들기
def greet():
    print('hi')
    print('hello')

greet()

# 노트북의 인치
def inch():
  lenthcm = float(input('길이를 입력하세요(cm)'))
  print(lenthcm, 'cm=',lenthcm*0.393701,'inch')

inch()

# 함수 내부에서 다른 함수 호출하기
def fun1():
  print('fun1을 호출합니다')
def fun2():
  print('fun2를 호출합니다')

def fun3():
  fun1()
  fun2()
  print('fun3를 호출합니다')

fun3()

# 함수 호출부에서 전달한 인수가 두 개 이상인 경우
def forecast(temp,humi, rain):
  print('날씨 예보를 알려드리겠습니다')
  print('최고온도는 ',temp,'도입니다')
  print('평균 습도는 ',humi,'% 입니다.')
  print('비올 확률은 ',rain,'% 입니다.')

forecast(32,67,50)

# 가변 매개변

# 점수의 총점과 평균
def sumavg(*scores):
  print(type(scores))

  total = 0
  l= len(scores)

  for score in scores:
    total += score

  print('총점: ',total,'점')
  print('평균: ',round(total/l,2),'점')

sumavg(40,86,98)

# 데이터 반환
# return
def addfunc(n1,n2):
  sum = n1+n2
  return sum

res = addfunc(58,74)
print(res)

# 사칙연수 함수
def cal(n1,n2):
  res1 = n1 + n2
  res2 = n1 - n2
  res3 = n1 * n2
  res4 = n1 / n2
  return (res1,res2,res3,res4)

num1= int(input('숫자를 입력해주세요'))
num2= int(input('숫자를 입력해주세요'))

cal(num1,num2)

# 중첩 함수를 이용한 나눗셈 연산 프로그램

def div(n1,n2):
  def divefun(num1,num2):
    return num1/num2

  if n2 !=0:
    res = divefun(n1,n2)
  elif n2 == 0:
    res = '0으로 나눌 수 없습니다,'

  return res

print(div(5,0))

# 재귀함수로 팩토리얼 구현
def fatori(num):
  if num == 1:
    return 1
  else:
    return num*fatori(num-1)

fatori(4)

