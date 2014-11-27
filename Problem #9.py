# Problem #9 Project Euler

for a in range(1,1001):
    for b in range(2,1001):
        c = 1000-a-b
        if (a**2 + b**2) == c**2 and (a+b+c == 1000):
            print(a)
            print(b)
            print(c)
print(200+375+425)
print(200*375*425)