# import functools
# import time

# @functools.lru_cache(maxsize=100)
# def fib(n):
    
#     if n < 2:
#         result = n
#     else:
#         result = fib(n-1) + fib(n-2)
        
#     return result



# start = time.time()
# for i in range(1,33):
#     fib(i)
#     stop = time.time()
#     timeRemind = stop-start
#     print('Number :{} it tooks {} s'.format(i,timeRemind))

# print(fib.cache_info())


text_list = ['x','xxx','xxxxx','xxxxxxx','']


f = lambda x: len(x)

print(f('this is test text'))

print(list(map(f,text_list)))

print(list(map(lambda x: len(x),text_list)))