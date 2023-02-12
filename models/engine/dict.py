#!/usr/bin/env python3

about = {'name': "Rashisky", 'age': 27, 'occupation': 'jobless'}

for elements, values in about.items():
    print(elements)

_dict = {"BaseModel.ee49c413-023a-4b49-bd28-f2936c95460d": {"my_number": 89, "__class__": "BaseModel", "updated_at": "2017-09-28T21:07:25.047381", "created_at": "2017-09-28T21:07:25.047372", "name": "My_First_Model", "id": "ee49c413-023a-4b49-bd28-f2936c95460d"}}

for keys, values in _dict.items():
    print(_dict[keys]["__class__"])
    
for keys in _dict.keys():
    print(_dict[keys]["my_number"])
