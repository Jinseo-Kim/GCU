class Stack:
    def __init__(self):
        self.size = 100          # 최대 크기
        self.stack = [None] * self.size
        self.top = -1            # 스택이 비어있음을 의미

    # push 연산
    def push(self, value):
        if self.top >= self.size - 1:
            print("Stack Overflow")
            return
        self.top += 1
        self.stack[self.top] = value

    # pop 연산
    def pop(self):
        if self.top == -1:
            print("Stack Underflow")
            return None
        value = self.stack[self.top]
        self.top -= 1
        return value

    # peek (맨 위 값 확인)
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
            return None
        return self.stack[self.top]

    # 비어있는지 확인
    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size -1

    # 출력 (디버깅용)
    def print_stack(self):
        print(self.stack[:self.top + 1])

s = Stack()
## 2*3+4 
## 3 
## *2+34
## 
## 
## 

if not s.is_full() :
    s.push(10)
s.push(20)
s.push(30)

s.print_stack()   # [10, 20, 30]

if not s.is_empty() :
    print(s.pop())    # 30


#======================================================================
# Postfix 계산하기
#======================================================================	
def evalPostfix( expr ):
    s = Stack()			       
    for token in expr :			
        if token in "+-*/" :	
            val2 = s.pop()		
            val1 = s.pop()		
            if (token == '+'): s.push(val1 + val2)	
            elif (token == '-'): s.push(val1 - val2)
            elif (token == '*'): s.push(val1 * val2)
            elif (token == '/'): s.push(val1 / val2)
        else :				        
            s.push( float(token) )	

    return s.pop()		        	


expr1 = [ '8', '2', '/', '3', '-', '3', '2', '*', '+']
expr2 = [ '1', '2', '/', '4', '*', '1', '4', '/', '*']
print(expr1, ' --> ', evalPostfix(expr1))
print(expr2, ' --> ', evalPostfix(expr2))


#======================================================================
# infix to Postfix
#======================================================================

# 우선순위를 돌려주는 함수
def precedence (op):
    if   op=='(' or op==')' : return 0	
    elif op=='+' or op=='-' : return 1	
    elif op=='*' or op=='/' : return 2	
    else : return -1


def Infix2Postfix( expr ):		
    s = Stack()
    output = []			        
    for term in expr :
        if term in '(' :		
            s.push('(')			
        elif term in ')' :		
            while not s.isEmpty() :
                op = s.pop()
                if op=='(' : break;	
                else :			    
                    output.append(op)
        elif term in "+-*/" :
            if s.is_empty() == True:
                print("잘못된 수식이 입력되었습니다.")
                exit()
            while not s.isEmpty() :	
                op = s.peek()		
                if( precedence(term) <= precedence(op)):
                    output.append(op)
                    s.pop()
                else: break
            s.push(term)		
        else :				    
            output.append(term)	

    while not s.isEmpty() :		
        output.append(s.pop())	

    return output	


infix1 = [ '8', '/', '2', '-', '3', '+', '(', '3', '*', '2', ')']
infix2 = [ '1', '/', '2', '*', '4', '*', '(', '1', '/', '4', ')']
postfix1 = Infix2Postfix(infix1)
postfix2 = Infix2Postfix(infix2)
result1 = evalPostfix(postfix1)
result2 = evalPostfix(postfix2)
print('  중위표기: ', infix1)
print('  후위표기: ', postfix1)
print('  계산결과: ', result1, end='\n\n')
print('  중위표기: ', infix2)
print('  후위표기: ', postfix2)
print('  계산결과: ', result2)
