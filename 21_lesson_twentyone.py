
# class HtmlCM:

#     def __init__(self):
#         pass

#     def __enter__(self,):
#         print('<TABLE>')
#         print('<TR>')
#         print('\t<TH>Number</TH><TH>Description</TH>')
#         print('</TR>')
#         return self

#     def __exit__(self, type, value, traceback):
#         print('</TABLE>')

# with HtmlCM() as html:
    
#     print('<TR>')
#     print('\t<TD>1</TD><TD>Say hello!</TD')
#     print('</TR>')
#     print('<TR>')
#     print('\t<TD>2</TD><TD>Say good bye!</TD')
#     print('</TR>')

# #*****************************************************************

import os
import zipfile
import requests

class FileFromWeb():

    def __init__(self, url, tmp_file):

        self.url = url
        self.tmp_file = tmp_file


    def __enter__(self):
        response = requests.get(self.url)
        with open(self.tmp_file, 'wb') as file:
            file.write(response.content)
        return self

    
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass



with FileFromWeb('https://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip', './euroxref.zip' ) as f:
    with zipfile.ZipFile(f.tmp_file, "r") as z:
        a_file = z.namelist()[0]
        print(a_file)
        os.chdir('./new_dir/')
        z.extract(a_file, '.', None)





