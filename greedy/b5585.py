moneys = [500, 100, 50, 10, 5, 1]
cost= 1000 - int(input())
numbers = []
for money in moneys:
    numbers.append(cost//money)
    cost -= (cost//money) * money
    cost %= money
print(sum(numbers))