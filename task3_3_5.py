x = [int(i) for i in input().split()]
a = x[::2]
x[::2] = a[::-1]

print(x)

