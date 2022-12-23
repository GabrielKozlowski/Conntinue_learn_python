

# class Cake:

#     """
#     Cake - class operating on cakes available in bakery
#     """
 
#     bakery_offer = []
 
#     def __init__(self, name, kind, taste, additives, filling):
               
#         """
#             init - arguments accepted:
#             name - the name of the cake
#             kind - the kind of the cake
#             taste - the taste of the cake
#             additives - the cake additives
#             filling - the filling of the cake
#             bakery_offer - list of all cakes 
#         """

#         self.name = name
#         self.kind = kind
#         self.taste = taste
#         self.additives = additives.copy()
#         self.filling = filling
#         self.bakery_offer.append(self)
 
#     def show_info(self):
#         print("{}".format(self.name.upper()))
#         print("Kind:        {}".format(self.kind))
#         print("Taste:       {}".format(self.taste))
#         if len(self.additives) > 0:
#             print("Additives:")
#             for a in self.additives:
#                 print("\t\t{}".format(a))
#         if len(self.filling) > 0:
#             print("Filling:     {}".format(self.filling))
#         print('-'*20)
 
#     @property
#     def full_name(self):
#         """ return name upper and kind of cake """
       
#         return "--== {} - {} ==--".format(self.name.upper(), self.kind)

# help(Cake)
# help(Cake.full_name)
# # *******************************************************************************************************************

# import requests
# import os
# import shutil
 
# def save_url_to_file(url, file_path):
        
#     r = requests.get(url, stream = True)     
#     with open(file_path, "wb") as f: 
#         f.write(r.content)
 
# url = 'http://www.mobilo24.eu/spis/'
# dir = 'c:/temp/'
# tmpfile = 'download.tmp'
# file = 'spis.html'
 
# tmpfile_path = os.path.join(dir, tmpfile)
# file_path = os.path.join(dir, file)


# try:
#     if os.path.exists(tmpfile_path):
#         print(f"Removing {tmpfile_path}")
#         os.remove(tmpfile_path)
#     else:
#         print(f"-Downloading url {url}")
#         save_url_to_file(url, tmpfile_path)

#         print(f"-Copying file {tmpfile_path} - {file_path}")
#         shutil.copy(tmpfile_path, file_path)

# except requests.exceptions.ConnectionError as e:
#     print(f"Error: The url is incorrect ({url}) ")

# except PermissionError as e:
#     print(f"Error: File {file_path} must by open with write opsions")

# except FileNotFoundError as e:
#     print(f"Error: Canot copy, file {tmpfile} does not exist")

# except Exception as e:
#     print(f"Error details: {e}")

# else:
#     print(f"-Succesfull Download url and copy files")

# finally:
#     if os.path.exists(tmpfile_path):
#         print(f"-Final removal of the file {tmpfile_path}")
#         os.remove(tmpfile_path)

#******************************************************************************************


# import datetime as dt
 
# class Trip:
#     def __init__(self, symbol, title, start, end):
#         self.symbol = symbol
#         self.title = title
#         self.start = start
#         self.end = end
 
#     def check_data(self):
#         if len(self.title) == 0:
#             raise Exception("Title is empty!")
#         if self.start > self.end:
#             raise ValueError("Start date is later than end date!")
 
#     @classmethod
#     def publish_offer(cls, trips):
#         list_of_errors = []

#         for trip in trips:

#             try:
#                 trip.check_data()
#             except ValueError as e:
#                 list_of_errors.append(f"{trip.symbol} : {str(e)}")
#             except Exception as e:
#                 list_of_errors.append(f"{trip.symbol} : {str(e)}")


#         if len(list_of_errors) > 0:
#             raise Exception(f"The list of trips has errors:\n{list_of_errors}")
#         else:
#             print("The offer will be published...")


# trips = [
#             Trip('IT-VNC', 'Italy-Venice', dt.date(2023, 6, 1), dt.date(2023, 6, 12)),
#             Trip('SP-BRC', 'Spain-Barcelona', dt.date(2023, 6, 12), dt.date(2023, 5, 22)),
#             Trip('IT-ROM', 'Italy-Rome', dt.date(2023, 6, 21), dt.date(2023, 6, 12))
#         ]

# try:
#     print("Start checking trips ")
#     Trip.publish_offer(trips)
#     print("Done.")

# except Exception as e:
#     print(f"There is an error with trips \nError:\n{e}")

# #***********************************************************************************************************

