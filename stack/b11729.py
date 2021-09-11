def hanoi(N, start, temp, end):
    if N == 1:
        print('{} {}'.format(start, end))
    else:
        hanoi(N-1, start, end, temp)
        print('{} {}'.format(start, end))
        hanoi(N-1, temp, start, end)

N = int(input())
print('{}'.format(2**N-1))
if N<= 20:
    hanoi(N, 1, 2, 3)
