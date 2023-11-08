import json
print(dir(json))
myInformation = {
    'name':'Amir Abbas',
    "Father Name":'Abdul Majeed'
}

i = json.dump(myInformation)
with open('a.json','w') as f:
    f.write(i)