import json 
 
with open('./json/data.json', 'r') as file: 
    data = json.load(file) 
 
# Print the data 
print(data)