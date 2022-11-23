import os, urllib.request

date_dir = './strony_www/'

pages = [ 
    {'name': 'mobilo',     'url': 'http://www.mobilo24.eu/' },
    {'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    {'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'}
]



for page in pages:
    try:
        file_name = page['name'] + '.html'
        path = os.path.join(date_dir,file_name) 
        urllib.request.urlretrieve(page['url'],path)
        print('Added site "{}" to Your dict'.format(page['url']))

    except urllib.error.URLError:
        print('\nError with adding site {}'.format(page['url']))
        print('Stopping the process')
        break

else:
    print('All pages added successfully')



