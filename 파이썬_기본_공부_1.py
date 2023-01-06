# -*- coding: utf-8 -*-
"""파이썬 기본 공부 1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PPHXNSv4L_e-ezPduipaieF5WcRK7iev
"""

#구구단 출력하기
#먼저 차례대로 누가 먼저 변화하는지 확인 한다
#그 안에 순서대로 조건문을 걸어준다
dan = 1
while dan <=9:
  print("=={}단==".format(dan))

  i =1
  while i<=9:
    print("{}*{}={}".format(dan,i,dan,dan*i))
    i+=1
  dan +=1

#구구구단 출력하기
#먼저 차례대로 누가 먼저 변화하는지 확인 한다
#그 안에 순서대로 조건문을 걸어준다
dan = 1
while dan <=3:
  print("=={}단==".format(dan))

  i = 1
  while i <=3:

    j = 1
    while j<=3:
      print("{}*{}*{} ={}".format(dan,i,j,dan*i*j))
      j+=1
    i+=1

  dan+=1

#함수의 개념 및 사용법
#함수를 선언 하고 실행한다
#함수명은 서로 다른것을 사용해야 한다 그 이유는 실행문이 어느것을 실행해야 하는지 모르기때문이다
#함수 선언 안에 함수 실행문을 넣을 수 있다

def a():
  i= 1
  while i<=10:
    print(i)
    i +=1

def b():
  a()

b()

# 문제 : 함수를 사용해서 코드량을 확 줄여주세요.
def print_8_dan():
  dan  = 8
  i = 1
  while i <= 9:
    print("{} * {} = {}".format(dan, i, dan * i))
    i += 1

i = 1
while i<=9:
  print("== {}번째 구구단 8단 출력 ==".format(i))
  print_8_dan()
  i+=1

#전역변수는 프로그램이 시작되고 종료를 기점으로 살아있다
#전역변수는 함수 내외부를 상관 하지 않고 모든 곳에서 사용가능하다
#지역변수는 함수 내부에서 시작되고 종료를 기점으로 살아있다

#전역공간(함수 외부)
dan  = 8 #전역변수
def print_8_dan():
  #지역공가(함수 내부)
  dan = 8 #지역변수
  i = 1
  while i <= 9:
    print("{} * {} = {}".format(dan, i, dan * i))
    i += 1

i = 1
while i<=9:
  print_8_dan()
  i+=1

#매개변수 사용법
#매개변수는 사용할 함수안에 넣어준다
#매개변수를 사용하기 위해서는 실행문에 인자값을 넣어주어야 한다
#매개변수를 지정하고 실행문의 인자값만 자유대로 변경하면
#하나의 식으로 여러 실행문을 실행 할 수 있다
#또한 매개변수와 인자의 값은 서로 일치하여한다
#인자와 매개변수는 순서대로 들어간다
#매개변수는 지역변수의 일종이다
def print_8_dan(dan,limit):
  
  i = 1
  while i <= limit:
    print("{} * {} = {}".format(dan, i, dan * i))
    i += 1
print_8_dan(8,516) #괄호 안에 있는 값을 인자 값이라고 한다
print_8_dan(32,12)


#dan = 7
#limit = 1616
#print_8_dan(dan,limit)

