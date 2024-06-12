import json

x =  '{ "name":"Arya", "age":25}'
y = json.loads(x)

print(y)
print(y["name"])


z = {
  "name": "Jees",
  "age": 23
}

a = json.dumps(z)
print(a)