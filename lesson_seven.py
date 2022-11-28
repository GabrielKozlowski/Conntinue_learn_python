# def double(x):
#     return 2 *x
 
# def square(x):
#     return x**2
 
# def negative(x):
#     return -x
 
# def div2(x):
#     return x/2

# number = 8

# transformations = [double,square,div2,negative]
# transformations2 = [square,square,div2,double]


# tmp_return_value = number



# for transformation in transformations2:
#     print(transformation(tmp_return_value))
    
# #---------------------------------------------------

def double(x):
    return 2 *x
 
def square(x):
    return x**2
 
def negative(x):
    return -x
 
def div2(x):
    return x/2

def generate_values(func,numbers):
    values_list = []
    for number in numbers:
        values_list.append(func(number))
    return values_list

numbers_list = [1,2,3,4,5,6,7]

print(generate_values(double,numbers_list))
print(generate_values(square,numbers_list))
print(generate_values(negative,numbers_list))
print(generate_values(div2,numbers_list))


