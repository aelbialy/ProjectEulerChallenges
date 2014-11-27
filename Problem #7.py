# Project Euler probelm #3,7,10
x = []
n = 2
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

while True:
    if is_prime(n):
        x.append(n)
    n+=1
    if len(x) == 10001:
        print(x.pop())
        break