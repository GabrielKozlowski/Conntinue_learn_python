import functools
import time

@functools.lru_cache(100)
def fib(n):
    
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
        
    return result



start = time.time()
for i in range(1,33):
    fib(i)
    stop = time.time()
    timeRemind = stop-start
    print('Number :{} it tooks {} s'.format(i,timeRemind))

print(fib.cache_info())
