# var_x = 10

# password = 'My super secred password'   

# source = 'var_x + 3'

# globals = globals().copy()
# del globals['password']

# result = eval(source, globals)

# print(result)


# #---------------------------------------------------------------
# import math

# argument_list = []

# for q in range(101):
#     argument_list.append(q/10)

# formula = input('Please write a mathematical formula: ')


# for x in argument_list:
#     print("For number: %4.1f, result is %6.2f " %  (x, eval(formula)))


# #----------------------------------------------
# var_x = 10

# source = '''
# new_var = 1
# for i in range(var_x):
#     print('-' * i)
#     new_var += i
# '''

# result = exec(source)

# print(result)

# print(new_var)
# #----------------------------------------------
import os

files_to_process = [
    r"C:\Users\FiFka9\Desktop\Nauka IT\Udemy\py_dla_srednio_zaawansowanych\script_lab_one.py",
    r"C:\users\fiFka9\Desktop\Nauka IT\Udemy\py_dla_srednio_zaawansowanych\script_lab_two.py"
    ]



for file_path in files_to_process:

    with open(file_path, 'r') as f:
        print('File: {}'.format(os.path.basename(file_path)))
        source = f.read()
        exec(source)