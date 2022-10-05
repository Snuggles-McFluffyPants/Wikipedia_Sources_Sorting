import json


from Text_Input_Window import *

items = string.split("\n")

with open('testcase.json','w') as write_file:
    json.dump(items, write_file,indent=4)

json_str = json.dumps(items, indent=4)

print(json_str)
print(type(json_str))