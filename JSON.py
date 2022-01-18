
import json

#Convert from JSON to Python:

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("Convert from JSON to Python:", y["age"])

#Convert from Python to JSON

a = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
b = json.dumps(a)

# the result is a JSON string:
print("Convert from Python to JSON", b)