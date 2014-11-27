# Project Euler probelm #3,7,10
x = []
y = []
def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
for i in range(0,int(600851475143 **0.5)+1):
    if is_prime(i) == True:
        x.append(i)
for j in x:
    if 600851475143 %j == 0:
        y.append(j)
print(y.pop())
