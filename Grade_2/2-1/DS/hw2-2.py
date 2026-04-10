import sys

operators = ['+', '-', '*', '**', '/', '(', ')']
start, end = 0, 0
idx = 0
value_st, op_st = [], []

arr = sys.stdin.readline().strip()
print(f'{arr}, type: {type(arr)}')

while (True):
    if arr[start] in operators:
        print("".join(arr))
        print(f'{idx * ' '}^ 이 위치에 오류가 있습니다.')
        
    if start == 0:
        value_st.append(arr[start])
    

    idx +=1
#     break


# for i, value in enumerate(arr):
#     if float(value).is_integer() == True:
#         arr[i] = int(value)

# print(arr)
