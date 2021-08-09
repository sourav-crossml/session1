import unittest
import pathlib as p
from assigment1 import write_json as wj
json_string = None


class TestCase(unittest.TestCase):
    def TestUserName(self):
        self.assertTrue(wj(),'sourav')

class TestCase(unittest.TestCase):
    def test_json_file(self):
        path = p.Path('data.json')
        self.assertTrue(path.is_file())
unittest.main()










    # with open("data.json") as f:
    #     json_string = f.read()
    # try:
    #     parsed_json = json.loads(json_string)
    #     formatted_json = json.dumps(parsed_json, indent=4, sort_keys=True)
    #     with open("data.json", "w") as f:
    #         f.write(formatted_json)
    #     print(True)
    # except Exception as e:
    #     print(repr(e))
