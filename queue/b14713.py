'''
모든 앵무새의 문장들 중 맨 앞 값을 확인하면서 목적 문장의 앞과 같으면 하나씩 pop
cnt는 모든 앵무새의 문장이 다 소요된 경우에 하나씩 카운트를 해서 다 소요되었어야 가능한 경우...
근데 안 소요되도 가능한거 아닌가...;;
'''
def check():
    global cnt
    for w in words[N]:
        for n in range(N):
            if words[n] and words[n][0] == w:
                words[n].pop(0)
                if not words[n]: cnt +=1
                break
        else:
            return 'Impossible'
    return 'Possible' if cnt == N else 'Impossible'

N = int(input())
words = [0]*(N+1)
cnt = 0
for i in range(N+1):
    words[i] = input().split()

print(check())

'''
pop 안쓰고 인덱스 접근인데 오히려 소모시간은 더 느리네..?!
'''
def check():
    for w in words[-1]:
        for n in range(N):
            nind = idxs[n]
            if nind >= len(words[n]):
                if n == N-1: 
                    return 'Impossible'
                else: continue
            if words[n][nind] == w:
                idxs[n] += 1
                break
    return 'Possible' if idxs == length[:N] else 'Impossible'

N = int(input())
words = [0]*(N+1)
idxs = [0]*N
length = [0]*(N+1)
for i in range(N+1):
    words[i] = input().split(' ')
    length[i] = len(words[i])

print(check())