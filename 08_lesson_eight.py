# import time


# # **Tworzenie wrappera dla każdej funkcji wpisanej w argument **

# def wrapper_time(a_function):
#     def a_wrapped_function(*args, **kwargs):
#         time_start = time.time()
#         v = a_function(*args, **kwargs)
#         time_stop = time.time()
#         print("Function {} was done in time {}".format(a_function.__name__, (time_stop-time_start)))
#         return v
#     return a_wrapped_function




# def get_sequence(n):
    
#     if n <= 0:
#         return 1
#     else:
#         v = 0
#         for i in range(n):
#             v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
#         return v


# wrapper_get_sequence = wrapper_time(get_sequence)

# print(wrapper_get_sequence(5))


#** Użycie dekoratora do wrappera dla funkcji  **

# import time
# import functools


# def wrapper_time(a_function):
#     def a_wrapped_function(*args, **kwargs):
#         time_start = time.time()
#         v = a_function(*args, **kwargs)
#         time_stop = time.time()
#         print("Function {} was done in time {}".format(a_function.__name__, (time_stop-time_start)))
#         return v
#     return a_wrapped_function



# @wrapper_time
# def get_sequence(n):
    
#     if n <= 0:
#         return 1
#     else:
#         v = 0
#         for i in range(n):
#             v += 1 + (get_sequence(i - 1) + get_sequence(i))/2
#         return v

# print(get_sequence(2))


# # Tworzenie wrappera z parametrem 

import os
import functools
from datetime import datetime as dt


def wrapper_with_log_file(logged_action,log_file_path):
    def wrapper_with_log_to_known_file(func):
        def the_real_wrapper(path):
            with open(log_file_path, 'a') as f:
                f.write('Action {} executed on {} on {}\n'.format(logged_action, path, dt.now().strftime("%Y-%m-%d %H:%M:%S")))               
            return func(path)
        return the_real_wrapper
    return wrapper_with_log_to_known_file
    

@wrapper_with_log_file('FILE_CREATE', r'C:/Users/FiFka9/Desktop/Nauka IT/Udemy/Py_dla_srednio_zaawansowanych/file_create.txt')
def create_file(path):
    print('creating file {}'.format(path))
    open(path,"w+")
 

@wrapper_with_log_file('FILE_DELETE', r'C:/Users/FiFka9/Desktop/Nauka IT/Udemy/Py_dla_srednio_zaawansowanych/file_delete.txt')
def delete_file(path):
    print('deleting file {}'.format(path))
    os.remove(path)        



create_file(r'C:/Users/FiFka9/Desktop/Nauka IT/Udemy/Py_dla_srednio_zaawansowanych/test.txt')
delete_file(r'C:/Users/FiFka9/Desktop/Nauka IT/Udemy/Py_dla_srednio_zaawansowanych/test.txt')
create_file(r'C:/Users/FiFka9/Desktop/Nauka IT/Udemy/Py_dla_srednio_zaawansowanych/test.txt')
delete_file(r'C:/Users/FiFka9/Desktop/Nauka IT/Udemy/Py_dla_srednio_zaawansowanych/test.txt')


