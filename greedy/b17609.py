for _ in range(int(input())):
    strs = input()
    i = chk = 0
    n = len(strs)

    while (i < len(strs)//2):
        if strs[i] == strs[n-i-1]:
            i += 1
        elif strs[i+1:n-i] == strs[n-i-1:i:-1]: # 왼쪽 한칸 띄고, 끝까지
            chk = 1
            break
        elif strs[i:n-i-1] == strs[n-i-2:i:-1]+strs[i]: # 오른쪽 한칸 띄고 끝까지인데 i=0 일 경우 고려하여
            chk = 1
            break
        else:
            chk = 2
            break
    print(chk)


'''
재귀에러 ... 5000번 재귀콜 넘어버림
왜냐면 3<= len(a) <= 100,000
'''
'''

def palindrome(a):
    if len(a) > 0:
        if a[0] == a[-1]:
            return palindrome(a[1:-1])
        elif a[1:] == a[:0:-1]:
            return 1
        elif a[:-1] == a[-2::-1]:
            return 1
        else:
            return 2
    else:
        return 0


for _ in range(int(input())):
    strs = input()
    print(palindrome(strs))
'''


'''
반례가 생김 Ex. abcddcdba 
왜냐 하면 elif 문 2개가 중첩되는 경우가 있으므로 논리적 오류 생김
c == d ? -> d == d (ok) -> 유사 회문도 안되게 되는 결과
c == d ? -> c == c (ok) -> 유사 회문이 되는 결과
적절한 elif 구조문이 아님

for _ in range(int(input())):
    strs = input()
    l = chk = 0
    r = len(strs)-1

    while (l < r):
        if chk:
            if strs[l] != strs[r]:
                chk = 2
                break
        if strs[l] == strs[r]:
            l += 1
            r -= 1
        elif strs[l+1] == strs[r]:
            l += 2
            r -= 1
            chk = 1
        elif strs[l] == strs[r-1]:
            l += 1
            r -= 2
            chk = 1
        else:
            chk = 2
            break
    print(chk)

'''            


'''
시간 초과 
for _ in range(int(input())):
    strs = input()
    if strs == strs[::-1]:
        print(0)
    else:
        for i in range(len(strs)):
            new_strs = strs[:i] + strs[i+1:] # O(n)
            if new_strs == new_strs[::-1]:   # O(n) 
                print(1)
                break
        else:
            print(2)
'''