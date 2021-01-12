import random
count=0
secret = random.randint(1,100)
while True:
    num=int(input("숫자를 입력하세요(끝낼때 0):"))
    count+=1
    if num ==0:
        break
    if num == secret:
        print("맞췄습니다,%d번"%count)
    elif num > secret:
        print("입력한 숫자보다  더 작습니다")

    else:
        print("입력한 숫자보다 더큽니다")
