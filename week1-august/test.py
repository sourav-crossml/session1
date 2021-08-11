"""
Class based implementation of assignmnet.
"""


class JsonConverter(object):
    """
    Class to read data from file
    print users name from file and
    generate a JSON file.
    """

    def __init__(self, user_fldr):
        """
        Constructor to initialize the folder for files.
        """
        self.user_folder = user_fldr

    def read_from_file(self, file_name):
        """
        Read usernames from file and prints those user names.
        :return: None
        """
        with open(self.user_folder + file_name, 'r') as file:
            names_list = file.readlines()
            for name in names_list:
                print(name.strip())

    def generate_uuid(self, user_name):
        """
        generate a random UUID based on username.
        'Caroline Owen'	-->
        """
        import random
        uuid = ""
        first_name, last_name = user_name.split()
        uuid += first_name[0]

    def generate_random_uuid(self, user_name):
        """
        Generate and return a random UUID of format
        XYxxxx-xxxx-xxxx-xxxx
        :return: uuid for a user 'String'
        """
        import random
        first_name, last_name = user_name.split()
        uuid = first_name[0:1].upper() + last_name[0].upper()
        for _ in range(4):
            random_hex = str(hex(random.randint(10000, 99999)))
            hex_num = random_hex.strip('0x')
            # print(hex_num)
            uuid += hex_num
            uuid += "-"
        uuid = uuid.strip("-")
        return uuid

    def generate_email(self, user_name):
        """
        Generate a dummy email for a username passed
        :return: email for a user 'String'
        """
        first_name, last_name = user_name.split()
        return first_name.lower() + last_name.lower() + "@dummy.com"

    def generate_json_data(self, user_name, uuid, email):
        """
        generate a json data for user
        """
        return {uuid: {"name": name, "email": email}}


js_object = JsonConverter('users/')

import os

file_names = os.listdir('users/')
print(file_names)
for file in file_names:
    js_object.read_from_file(file)