# number = 0
#
# while number < 10:
#     print(number)
#     number = number + 1 #number = number + 1가 없으면 while이 무한히 반복
#
# #print("=====메뉴=====")
# #print("1. 시작하기")
# #print("2. 종료하기")
# #print("==============")
#
# #user_input = -1
#
# #while user_input != 2:
# #   user_input = int(input("값을 입력하세요 >>"))
#
# while True:
#   print("=====메뉴=====")
#   print("1. 시작하기")
#   print("2. 종료하기")
#   print("==============")
#
#   user_input =int(input("값을 입력하세요 >>"))
#   if user_input == 2:
#       # break

import random

answer = random.randrange(0, 10)
user_input = -1

#사용자가 answer 맞출때까지 반복

while True:
    user_input =int(input("값을 입력하세요 >>"))

    if user_input == answer:
        print("정답입니다!")
        break

        # 사용자가 answer 맞출때까지 반복
        # 1. 사용자에게 기회주기
        # 2. 틀렸을때 updown 출력해주기
