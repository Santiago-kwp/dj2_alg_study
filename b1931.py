import sys
meets = []
for _ in range(int(sys.stdin.readline())):
    meets.append(list(map(int,sys.stdin.readline().split())))
#끝나는 시간으로 오름차순 정렬 후, 시작시간으로 정렬하는 방법    
meets.sort(key=lambda x: (x[1], x[0]))

cnt = last = 0
for start, end in meets:
    if start >= last:
        cnt +=1
        last = end

print(cnt)
