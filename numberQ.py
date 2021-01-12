import random

correct = 0
while True:
    a = random.randint(10, 99)
    b = random.randint(10, 99)
    op = random.randint(1, 3)

    if op == 1:
        ans = a + b
        mark = "+"
    elif op == 2:
        if (a < b):
            a, b = b, a
        ans = a - b
        mark = "-"
    else:
        ans = a * b
        mark = "*"

    question = "%d %s %d = ?(끝낼 때는 0) " % (a, mark, b)
    c = int(input(question))

    if c == 0:
        break
    elif c == ans:
        print("정답입니다.")
        correct = correct + 1
    else:
        print("틀렸습니다.")

print("%d 개 맞췄습니다." % correct)
