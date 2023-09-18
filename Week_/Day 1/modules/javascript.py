# json module

import json

my_data = {
    'name': 'John',
    'age': 21,
    'city': 'New York',
    'school': None
}


# convert from python dict to json

json_data = json.dumps(my_data)
print(json_data)


# convert from json to python dict
our_data = json.loads(json_data)
print(our_data['name'])
