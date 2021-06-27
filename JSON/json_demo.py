import json

data = {"name":"Gaurav","roll":102 ,"lucky_num":[0,7,11]}
#data = (15,"adsads",4654)

print(data)
json_data = json.dumps(data)
print(json_data)
#{"name": "Gaurav", "roll": 102}

original_data = json.loads(json_data)
print(original_data)