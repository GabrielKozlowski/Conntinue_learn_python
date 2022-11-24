# banknotes_coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500]
# dict_denominations = {}


# for i in banknotes_coins:
#     dict_denominations.update({i:0})

# dict_denominations[100] += 1
# dict_denominations[20] += 1
# dict_denominations[5] += 1
# dict_denominations[0.5] += 1
 
# dict_denominations[50] += 1
# dict_denominations[20] += 2
# dict_denominations[5] += 1
# dict_denominations[2] += 2
 
# dict_denominations[100] += 1
# dict_denominations[50] += 1
# dict_denominations[2] += 1


# for k in dict_denominations:
#     print("Wartość nominału: %7.2f , Ilość: %1d, suma = %7.2f" % (k, dict_denominations[k], k * dict_denominations[k]))



# #-------------------------------------------------


# ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
#          'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

# lineOfFly = [(portStart,portStop) for portStart in ports for portStop in ports if portStart < portStop]

# print(len(lineOfFly))



ports = ['WAW', 'KRK', 'GDN', 'KTW', 'WMI', 'WRO', 'POZ', 'RZE', 'SZZ',
         'LUZ', 'BZG', 'LCJ', 'SZY', 'IEG', 'RDO']

gen = ((portStart,portStop) for portStart in ports for portStop in ports if portStart < portStop)

values = 0
while True: 
    try:
        print(next(gen))
        values += 1
    except StopIteration:
        print(f'All values in genration: {values}')
        break
