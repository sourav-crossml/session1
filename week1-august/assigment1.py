import datetime
import uuid
import os,getpass
import json
"""
     TODO:Create a function to print user name and datetime of the execution,  
          Function should have two variables to store datetime and username respectively.
"""
# current datetime
now = datetime.datetime.now()
# formating the output in human redable format
current_date_time = now.strftime("%d/%m/%Y, %H:%M:%S")
print(current_date_time)

# printing local user
print(getpass.getuser())

# Getting present working directory
"""
   TODO: file location should not be static location.Add input function to get folder location on runtime.
"""
PWD = os.getcwd()
users_folder = PWD+'/users/'

files_list = os.listdir(users_folder)
user_names_list = []

# creating function to read user names from user folder

def display_names(users_folder):
	files_list = os.listdir(users_folder)
	for file_name in files_list:
		# print(file_name)
		# file = open(users_folder+file_name,'r')
		with open(users_folder+file_name,'r') as file:
			user_names_list.extend(file.readlines())
			for user in user_names_list:
				print(user.strip())
display_names(users_folder)
user_names = [user.strip() for user in user_names_list]

# generating unique user id's
# this function will add 1st index value from the user name with uuid

def gen_UUID(user):
	return user[1]+str(uuid.uuid1())

# generating emails

def gen_email(user_name):
	first_name = user_name[0:2]
	last_name = user_name[6]
	return first_name+last_name+"@sourav.com"

user_info = []

for user_name in user_names:
	user_info.append({gen_UUID(user_name):{"name":user_name,"email":gen_email(user_name)}})


# print(json.dumps(user_info))
# this function will write data to data.json file

def write_json(data, filename='data.json'):
	with open(filename, 'w') as f:
		json.dump(data, f, indent=2)

# as soon as we call the function it will write data to json file
write_json(user_info)


"""
  TODO:Program should be able to execute from the shell script.
"""
# alldone
