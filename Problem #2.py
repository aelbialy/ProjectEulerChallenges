# Project Euler #2 Solution
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
y = []
for i in range(35):
    y.append(fib(i))
f = []
for i in y:
    if (i%2 == 0) and (i<6000000):
        f.append(i)

print(sum(f))

