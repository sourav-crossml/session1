import datetime
from hashlib import new
import uuid
import os,getpass
import json
import random

class UserData:
    """
    this class will print user current datetime , local user and output 
    from the text files and then save that output to json file with userid
    email and name
    """
    def __init__(self,user_fldr):
        """
        the init method will give path of user folder fromt he class object
        """
        self.user_folder = user_fldr
    def currenttime(self):
        """
        this method will give current datetime
        """
        now = datetime.datetime.now()
        current_date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
        print(current_date_time)

    def username(self):
        """
        this method will give local user name
        """
        print(getpass.getuser())

    def read_file(self, file_name):
        """
        this method will read text files from user folder
        """
        with open(self.user_folder + file_name, 'r') as file:
            names_list = file.readlines()
            for name in names_list:
                print(name.strip())

    def appending_data_to_new_list(self, file_name):
        """
        this method will genertae a new list with all names of all txt files in user folder
        """
        all_names = []
        with open(self.user_folder + file_name, 'r') as file:
            names_list = file.readlines()
            for name in names_list:
                all_names.append(name.strip())

        return all_names

    def gen_email(self,user_name):
        """
        this method will generate email
        """
        email_addrs=[]
        for name in user_name:
            first_name,last_name=name.split()
            email_addrs.append(first_name[0:3]+last_name[0:3]+"@sourav.com")
        return email_addrs

    def genrating_user_id(self,user_name):
        """
        this method will generate uuid
        """
        new_uudi=[]
        for names in user_name:
            b=random.randint(100000,99999999)
            first_name,last_name=names.split()
            new_uudi.append(str(b)+first_name[0:1]+last_name)
        return new_uudi
        
    
    def appending_data_to_json_file(self,user_name):
        self.username=user_name
        json_data=[]
        for user in user_name:
            json_data.append({self.genrating_user_id(user):{"Username":user,"email":self.gen_email(user)}})
        print(json_data)




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

# print(len(new_list))
# o.genrating_user_id(new_list)
# o.gen_email(new_list)
o.appending_data_to_json_file(new_list)