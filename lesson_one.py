a = b = c = 10

print(a,id(a),b,id(b),c,id(c))

a = 20

print(a,id(a),b,id(b),c,id(c))


a = b = c = [1,2,3]

print(a,id(a),b,id(b),c,id(c))

a.append(4)

print(a,id(a),b,id(b),c,id(c))

x = 10
y = 10

print(x,id(x),y,id(y))

y = y + 1 - 1

print(x,id(x),y,id(y))

y = y + 1234567890 - 1234567890

print(x,id(x),y,id(y))


days = ['mon','tue','wed','thu','fri','sat','sun']

worksday = days.copy()

worksday.remove('sun')
worksday.remove('sat')

print(days,'\n',worksday)


options = """
        1. load data
        2. export data
        3. analyze & predict
        4. exit
        """


while True:
    print(options)    
    try:
        choice = int(input('Chose number: '))
    except ValueError:
        print('Must write a number')
    else:   
        if choice == 1:
            print('You choice load data')
        elif choice == 2:
            print('You choice export data')
        elif choice == 3:
            print('You choice analyze & predict')
        elif choice == 4:
            print('Good bye')
            break
        else:
            print('You must choice a good number')


