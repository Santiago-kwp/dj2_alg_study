'''
최대 인원 수 = 전체 인원 수 - 무조건 떨어지는 사람
무조건 떨어지는 사람 어떤 사람보다 서류, 면접 점수 둘 다 낮은 사람
서류 점수로 오름차순 정렬 후, 서류 1등을 기준으로 
1등의 면접 점수부터 아래 등수의 면접 등수를 비교하며 
등수가 높은(숫자가 낮은) 사람을 채택하고 해당 사람의 면접 등수를 갱신하며 계산
'''
import sys
for _ in range(int(input())):
    N = int(input())
    grades = []
    for _ in range(N):
        grades.append(list(map(int, sys.stdin.readline().split())))

    grades.sort()

    cnt = 1
    maxb = grades[0][1]
    for _, b in grades[1:]:
        if b < maxb:
            maxb = b
            cnt += 1
    print(cnt)
    