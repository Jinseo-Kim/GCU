import sys

arr = sys.stdin.readline().rstrip()
stack = []
mid = len(arr) // 2

for idx, value in enumerate(arr):
    if mid > idx:
        stack.append(value)
    elif (mid == idx) and (len(arr) % 2 == 1):
        continue
    else:
        chk = stack.pop()
        if chk != value:
            print(f'두 문자가 다릅니다. cur: {value} stack: {chk}')
            break
