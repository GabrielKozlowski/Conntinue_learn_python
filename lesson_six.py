# def show_progress(how_many,character='*'):
#     print(character * how_many)

# show_progress(10)
# show_progress(15)
# show_progress(30)
# show_progress(10, '-')
# show_progress(15, '+')


# def calculate_paint(efficency_ltr_per_m2=0.07, *args):
#     for arg in args:
#         paint_needed = arg * efficency_ltr_per_m2
#         print('You need {0:5.1f} liters paint for painting {1:5.1f}m2'.format(paint_needed,arg))
#     print('-' * 40)
    
# room_area = [20,25,30,50]

# calculate_paint(0.07,15,25,17)
# calculate_paint(0.07,*room_area)



# def log_it(*args):
#     plik = './log_it.txt'
#     data_file = open(plik, 'a')

#     for arg in args:        
#         with open('./log_it.txt') as f:
#             if arg in f.read():
#                 print('The "{0}" is allready in file'.format(arg))
#             else:
#                 data_file.write(arg + '\n')
#                 print('ok')

#     data_file.close
        
# log_it('Starting processing forecasting')
# log_it('ERROR', 'Not enough data', 'invoices', '2020')