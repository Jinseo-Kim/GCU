import sys

def divide_arr (full_arr):
    operators = ['+', '-', '*', '/', '(', ')']
    slice_arr = []
    gwalho = []
    idx = 0
    flag = 0
    current_num = ''
    length = len(full_arr)


    while (length > idx):
        if idx == 0:
            if full_arr[idx] in operators and full_arr[idx] != '(':
                print(f'^ 이 위치에 오류가 있습니다.')
                return None
        
        if full_arr[idx] == ' ':
            idx+=1
            continue

        if full_arr[idx] == '.':
            if '.' in current_num:
                print(f'{' ' * (idx)}^ 이 위치에 오류가 있습니다.')
                return None

        if full_arr[idx] in operators:
            if current_num:
                slice_arr.append(float(current_num))
                flag = 0

            if full_arr[idx] != '(' and full_arr[idx] != ')':
                flag += 1
            else:
                gwalho.append(full_arr[idx])

            if flag > 1:
                print(f'{' ' * (idx)}^ 이 위치에 오류가 있습니다.')
                return None

            if full_arr[idx] == '*':
                if length > idx+1 and full_arr[idx+1] == '*':
                    slice_arr.append('**')
                    idx += 2
                    current_num = ''
                    continue

            slice_arr.append(full_arr[idx])
            current_num = ''
        elif full_arr[idx].isdigit() or full_arr[idx] == '.':
            current_num += full_arr[idx]
        else:
            print(f'{' ' * (idx)}^ 이 위치에 오류가 있습니다.')
            return None

        idx += 1

    if current_num:
        slice_arr.append(float(current_num))


    cnt = 0
    while (len(gwalho) != 0):
        chk_gwalho = gwalho.pop()
        if chk_gwalho == '(':
            cnt += 1
        else:
            cnt -= 1
    
    if cnt != 0:
        print(f'{' ' * (idx)}^ 이 위치에 오류가 있습니다.')
        return None

    # print(slice_arr)
    return slice_arr


def infix2Postfix (infix):
    prim_operators = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '**': 3}
    stack = []
    postfix = []

    for term in infix:
        if term == '(':
            stack.append('(')
        elif term == ')':
            while (len(stack) != 0):
                op = stack.pop()
                if op == '(':
                    break
                else:
                    postfix.append(op)
        elif prim_operators.get(term) != None:
            while (len(stack) != 0):
                op = stack[-1]
                if prim_operators.get(term) <= prim_operators.get(op):
                    postfix.append(op)
                    stack.pop()
                else:
                    break
            stack.append(term)
        else:
            if float(term).is_integer():
                postfix.append(int(term))
            else:
                postfix.append(term)

    while (len(stack) != 0):
        postfix.append(stack.pop())
    
    return postfix

def evalPostfix(postfix):
    operators = ['+', '-', '*', '/', '**']
    stack = []
    for token in postfix:
        if token in operators:
            val2 = stack.pop()
            val1 = stack.pop()
            if (token == '+'): 
                stack.append(val1 + val2)
            elif (token == '-'): 
                stack.append(val1 - val2)
            elif (token == '*'): 
                stack.append(val1 * val2)
            elif (token == '/'): 
                stack.append(val1 / val2)
            elif (token == '**'):
                stack.append(val1 ** val2)
        else:
            stack.append(token)

    return stack.pop()


def main ():
    infix = divide_arr(sys.stdin.readline().strip())
    if infix != None:
        # print(infix)
        postfix = infix2Postfix(infix)
        # print(postfix)
        result = evalPostfix(postfix)
        result = round(result, 10)

        if float(result).is_integer():
            print(f'= {int(result)}')
        else:
            print(result)

main()
