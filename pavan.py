number = int(input())
total = 0

for value in range(1, number + 1):
    total = total + value

print("{1}".format(number, total))
