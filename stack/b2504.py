'''
괄호 짝 검사를 하는 함수를 만들어서 체크 
체크를 통과하면 계산을 하는 함수를 통과해서 총 괄호 계산
'''
def check():
    stack = []
    for i in bracket:
        if i == '(' or i == '[':            # 열린 괄호면 일단 받음
            stack.append(i)
        else:
            if stack:                       # 열린 괄호가 있는 스택에 경우 
                if stack[-1] + i == '()':   # 짝이 맞으면 pop
                    stack.pop()
                elif stack[-1] + i == '[]':
                    stack.pop()
                else:                       # 열린괄호가 있는데 짝이 안맞는 경우
                    return 0
            else:                           # 스택에 아무것도 없는데 닫힌 괄호가 들어오는 경우
                return 0
    return 0 if stack else 1

def calc(b):
    stack = []
    i = 0
    while(i < len(b)):
        if b[i:i+2] == '()':        # 열자마자 닫힌 괄호에는 숫자 할당해서 다시 스택에 집어 넣음
            stack.append(2)
            i += 2
        elif b[i:i+2] == '[]':
            stack.append(3)
            i += 2
        elif b[i] == '(':           # 열린 괄호가 나오면 일단 스택에 넣음
            stack.append('(')
            i += 1
        elif b[i] == '[':
            stack.append('[')
            i += 1
        elif b[i] == ')':           # 위의 조건으로 인해 닫힌 괄호일 때 stack에는 무조건 숫자들이 스택에 쌓여있음
            n = 0
            while(stack[-1] != '('): # 열린 괄호가 나올 때까지 스택에 있는 숫자를 합치는 연산
                                        # (()()) => (, 2, 2, ||  ) => 8 
                n += stack.pop()
            stack.pop()              # 닫힌 괄호 제거
            stack.append(n*2)
            i += 1
        elif b[i] == ']':
            n = 0
            while(stack[-1] != '['):
                n += stack.pop()
            stack.pop()
            stack.append(n*3)      
            i += 1
    return sum(stack)
    
bracket = input()
if check():
    print(calc(bracket))
else:
    print(0)


    
'''
숏코딩
replace 를 통해 괄호를 다 풀어서 eval 로 계산함
'''
s=str.replace
try:print(eval(s(s(s(s(s(input(),'()','+2'),'[]','+3'),'(','+2*('),'[','+3*['),']','][0]')))
except:print(0)
