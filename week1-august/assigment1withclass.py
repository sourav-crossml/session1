import datetime
import uuid
import os,getpass
import json
new_list=[]
print(new_list)
class UserData:

    def __init__(self,user_fldr):
        self.user_folder = user_fldr
    def currenttime(self):
        now = datetime.datetime.now()
        current_date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
        print(current_date_time)

    def username(self):
        print(getpass.getuser())

    def read_file(self, file_name):
        with open(self.user_folder + file_name, 'r') as file:
            names_list = file.readlines()
            for name in names_list:
                print(name.strip())

    def appending_data_to_new_list(self, file_name):
        all_names = []
        with open(self.user_folder + file_name, 'r') as file:
            names_list = file.readlines()
            for name in names_list:
                all_names.append(name.strip())

        return all_names
    def genrating_user_id(self,user_name):
        import random
        new_uudi=[]
        for names in user_name:
            first_name,last_name=names.split()
            new_uudi.append(first_name[0:1]+last_name)
        print(new_uudi)


PWD = os.getcwd()
users_folder = PWD+'/users/'
o=UserData(users_folder)
# o.currenttime()
# o.username()

files_list = os.listdir(users_folder)
# print(files_list)
new_list = []
for file in files_list:
    # o.read_file(file)
    new_list.extend(o.appending_data_to_new_list(file))

print(new_list)
o.genrating_user_id(new_list)