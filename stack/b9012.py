def check(arr):
    stack = []
    for p in arr:
        if stack:
            if stack[-1] == '(' and p == ')':
                stack.pop()
                continue
        stack += [p]
    return 'NO' if stack else 'YES'

for _ in range(int(input())):
    print(check(list(input())))