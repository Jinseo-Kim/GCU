import sys

def binary_search(arr, first, last, find_num):
    mid = (first + last) // 2

    print(f'idx: first: {first}, mid: {mid}, last: {last}')
    print(f'num: first: {arr[first]}, mid: {arr[mid]}, last: {arr[last]}\n')

    if find_num == arr[mid]:
        return find_num
    elif find_num > arr[mid]:
        return binary_search(arr, mid + 1, last, find_num)
    else:
        return binary_search(arr, first, mid - 1, find_num)

arr = [i for i in range(1, 10)]
first = 0
length = len(arr)

find_num = int(sys.stdin.readline().rstrip())
print(f'result = {binary_search(arr, first, length - 1, find_num)}')