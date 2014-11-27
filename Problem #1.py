# Project Euler problem #1 solution 
x = []
for i in range(1,1000):
    if (i%3 == 0 or i%5 == 0):
        x.append(i)
print(sum(x))
