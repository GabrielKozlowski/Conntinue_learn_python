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
# import os

# files_to_process = [
#     r"C:\Users\FiFka9\Desktop\Nauka IT\Udemy\py_dla_srednio_zaawansowanych\script_lab_one.py",
#     r"C:\users\fiFka9\Desktop\Nauka IT\Udemy\py_dla_srednio_zaawansowanych\script_lab_two.py"
#     ]



# for file_path in files_to_process:

#     with open(file_path, 'r') as f:
#         print('File: {}'.format(os.path.basename(file_path)))
#         source = f.read()
#         exec(source)

# #-----------------------------------------
# # compile function, 
# #-----------------------------------------

import math
import time

formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
    
argument_list = []

for i in range (10000):
    argument_list.append(i/10)


for formula in formulas_list:
    results_list = []
    print('Formula: {}'.format(formula))
    
    start = time.time()
    for x in argument_list:
        results_list.append(eval(formula))
    print('Minimum value: {}. Maxiumum value: {}'.format(min(results_list),max(results_list)))
    stop = time.time()
    print('Nie kompilowane zajęło: ', stop-start)
    print('\n')
print('*' * 40)
for formula in formulas_list:
    results_list = []
    print('Formula: {}'.format(formula))
    
    start = time.time()
    compiled_formula = compile(formula, formula, 'eval')
    for x in argument_list:
        results_list.append(eval(compiled_formula))
    print('Minimum value: {}. Maxiumum value: {}'.format(min(results_list),max(results_list)))
    stop = time.time()
    print('Nie kompilowane zajęło: ', stop-start)
    print('\n')





liczby = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]

nowa = [int(liczba) for liczba in liczby]

print(abs(nowa))