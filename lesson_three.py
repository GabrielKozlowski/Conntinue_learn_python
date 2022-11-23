# import os, urllib.request

# date_dir = './strony_www/'

# pages = [ 
#     {'name': 'mobilo',     'url': 'http://www.mobilo24.eu/' },
#     {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
#     {'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'}
# ]



# for page in pages:
#     try:
#         file_name = page['name'] + '.html'
#         path = os.path.join(date_dir,file_name) 
#         urllib.request.urlretrieve(page['url'],path)
#         print('Added site "{}" to Your dict'.format(page['url']))

#     except urllib.error.URLError:
#         print('\nError with adding site {}'.format(page['url']))
#         print('Stopping the process')
#         break

# else:
#     print('All pages added successfully')


# #-----------------------------------------------------------
# colors = ["red", "orange", "green", "violet", "blue", "yellow"]



# def numbersOfColors(colors,n):
#     colors = colors.copy()
#     return colors[:n]


# i = 0
# while i < len(colors):
#     numbersOfColors(colors,i+1)
#     i += 1


# for j in range(1,len(colors)+1):
#     numbersOfColors(colors,j)


# text = ''' 
#     Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia
#     biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości 
#     jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.
# '''

# print(text[text.index('(')+1:text.index(')')])


# #-----------------------------------------------
# projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
# leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']


# for i in list(zip(leaders,projects)):
#     print("The leader of '",i[1],"' is ", i[0])


# print('-'*50)

# dates = ['2016-06-23', '2016-08-29', '1994-01-01']

# for d, j in zip(dates,zip(leaders,projects)):
#     print("The leader of '",j[1],"' started ",d, " is ", j[0])

# print('-'*50)

# for n, (d,j) in enumerate(zip(dates,zip(leaders,projects))):
#     print(n+1,"- The leader of '",j[1],"' started ",d, " is ", j[0])

