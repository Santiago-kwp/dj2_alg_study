'''
문제 요구사항에 맞게 하나씩 함수화하여 작성
eval() 함수를 써보는 계기가 되서 좋았음.
'''
import sys

def push(num):
    queue.append(num)

def pop():
    if queue:
        temp = queue[0]
        del queue[0]
        return temp
    else:
        return -1

def size():
    return len(queue)

def empty():
    if queue:
        return 0
    else:
        return 1

def front():
    if queue:
        return queue[0]
    else:
        return -1

def back():
    if queue:
        return queue[-1]
    else:
        return -1

queue = []
for _ in range(int(sys.stdin.readline())):
    com = sys.stdin.readline()
    if com[:4] == 'push':
        push(com.split()[-1])
    else:
        print(eval(com)())