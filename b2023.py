'''
재귀로 1의 자리 수부터 되는 소수 *10 + (1~9)까지 검사
'''
def check(n):
    for i in range(2, int(n**0.5)+1):
        if not n%i:
            return
    if n//(10**(N-1)):
        print(n)
    else:
        for j in range(1, 10):
            check(n*10+j)
    
N = int(input())
plist = [2, 3, 5 ,7]
for p in plist:
    check(p)

'''
Brute force 재귀로 접근하였으나 시간 초과...
'''
# import time
# start_time = time.time()
# def check(n):
#     if n:
#         if n==1:
#             return 0
#         for i in range(2, int(n**0.5)+1):
#             if not n%i:
#                 return 0
#         return check(n//10)
#     else:
#         return 1


# N = int(input())
# for n in range(10**(N-1), 10**N):
#     if check(n):
#         print(n)
# print("--- %s seconds ---" % (time.time() - start_time))