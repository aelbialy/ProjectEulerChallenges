# Project Euler #5

import timeit
start = timeit.default_timer()
n = 2520

while True:
    if n%11==0 and n%12==0 and n%13==0 and n%14==0 and n%15==0 and n%16==0 and n%17==0 and n%18==0 and n%19==0 and n%20 == 0:
        print(n)
        break
    else:
        n+=1
stop = timeit.default_timer()
print(stop-start)
