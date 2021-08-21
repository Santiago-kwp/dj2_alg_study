'''
맨 위 버리고, 그 다음장 맨 밑으로
Ex. n = 6 인경우 -> 1, 2, 3, 4, 5, 6
1 버리고 2 맨밑 => 3, 4, 5, 6, 2
3 버리고 4 맨밑 => 5, 6, 2, 4
5 버리고 6 맨밑
2 버리고 4 맨밑
6 버리고 4 만 남음
'''
# 시간 초과 --> concatenate가 O(n) -> 루프문 돌면서 = O(n^2)
# _,*a = range(int(input())+1)
# for _ in range(a[-1]-1):
#     a = a[2:] + [a[1]]
# print(*a)

# 재귀로 풀시 -> 메모리 초과...
# _,*a = range(int(input())+1)
# def remain(a):
#     if len(a) == 1:
#        print(*a)
#     else:
#         remain(a[2:]+[a[1]]) 
# remain(a)

# list 자료형의 경우 pop() 이나 del() 에서 다시 순서 맞추는 작업으로 인해
# 시간복잡도 O(n)이 들어서 결국 deque 내장 함수를 활용

from collections import deque
queue = deque(range(1, int(input())+1))

for _ in range(queue[-1]-1):
    queue.popleft()                 # O(1)
    queue.append(queue.popleft())   # O(1) + O(1)
print(*queue)

'''
숏코딩 1: 규칙 활용
3일 때 : (3 - 2) * 2 = 2
4일 때 : (4 - 2) * 2 = 2
5일 때 : (5 - 4) * 2 = 2
6일 때 : (6 - 4) * 2 = 4
7일 때 : (7 - 4) * 2 = 6
8일 때 : (8 - 4) * 2 = 8
즉, (N - 2**n = (N보다 작은 2의 제곱수)) * 2
INPUT - 2**(INPUT>2의 제곱) ] * 2이다.


N에 2를 곱해서 이진수화 한다음 맨 앞 한자리 빼고
다시 10진수로 int 형변환 뒤 출력
-> (2*N - (2*N보다 작은 2의 제곱수))
6*2 = 12 -> bin(12) -> '0b1100'-> '100' -> 4
if N=1 -> 1*2 -> bin(2) -> '0b10` -> '0' -> 0 이라 False -> 1로 출력
'''
print(int(bin(int(i:=input())*2)[3:],2)or i)

'''
숏코딩 2 : 규칙 활용
'''
n,m=int(input()),1
while m<n:m*=2
print(n*2-m)

