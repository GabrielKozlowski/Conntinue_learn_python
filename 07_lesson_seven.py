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

# def double(x):
#     return 2 *x
 
# def square(x):
#     return x**2
 
# def negative(x):
#     return -x
 
# def div2(x):
#     return x/2

# def generate_values(func,numbers):
#     values_list = []
#     for number in numbers:
#         values_list.append(func(number))
#     return values_list

# numbers_list = [1,2,3,4,5,6,7]

# print(generate_values(double,numbers_list))
# print(generate_values(square,numbers_list))
# print(generate_values(negative,numbers_list))
# print(generate_values(div2,numbers_list))

# #--------------------------------------------------------
from datetime import datetime

def whatTime(chose = 'f_minutes'):
    if chose == 'f_minutes':
        def f_minutes(date1,date2):  
            score = date2 - date1
            result = int(score.total_seconds() / 60)
            return ('Difference between dates in minutes: {0:5d}'.format(result))
        return f_minutes
    elif chose == 'f_hours':
        def f_hours(date1,date2):
            score = date2 - date1
            result = int(score.total_seconds() /60 /60)
            return ('Difference between dates in hours: {0:4d}'.format(result))
        return f_hours
    elif chose == 'f_days':
        def f_days(date1,date2):
            score = date2 - date1
            result = int(score.total_seconds() /60 /60 / 24)
            return ('Difference between dates in days: {0:3d}'.format(result))
        return f_days
    
minutes = whatTime('f_minutes')
hours = whatTime('f_hours')
days = whatTime('f_days')

date1 = datetime(2022,10,28)
date2 = datetime(2022,11,29)


print(minutes(datetime(2022,10,28),datetime(2022,11,29)))
print(hours(date1,date2))
print(days(date1,date2))


print(days(datetime(1989,1,30),datetime.now()))
print(days(datetime(1990,8,26),datetime(2023,7,4)))