# Project Euler Problem #4

y = []
for i in range(900,1000):
    for j in range(900,1000):
        x = str(i*j)
        if x == x[::-1]:
            y.append(int(x))
y.sort()
print(y.pop())
