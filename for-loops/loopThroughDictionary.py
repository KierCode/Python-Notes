employee = {"name": "Katy", "age": 25, "city": "New York", "id": 0}
for key in employee:
    print(key)
'''
OUTPUT:
name
age
city
id
'''


for value in employee.values():
    print(value)
'''
Katy
25
New York
0
'''

for key, value in employee.items():
    print(f"{key}: {value}")
'''
OUTPUT:
name: Katy
age: 25
city: New York
id: 0
'''