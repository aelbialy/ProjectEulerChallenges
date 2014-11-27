# Project Euler #6 
x = 0

for i in range(1,101):
    x += i**2
print(x)

y = []
for i in range(1,101):
    y.append(i)
    
print(sum(y)**2)