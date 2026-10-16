student={
    "student1":{
        "name":"Rahim",
        "age":20
},
"student2":{
    "name":"Karim",
    "age":22

},
}
#print(student["student1"]["name"])
for key , value in student.items():
    print(key,value)
# inner data print : 

for student_id , info in student.items():
    print(student_id)
    for key,value in info.items():
        print(key,value)
"""
Practice 🔥
employees = {    "emp1": {        "name": "Hasan",        "salary": 30000    },    "emp2": {        "name": "Rafi",        "salary": 35000    }}
Task:
1. Hasan print করো
2. Rafi-এর salary print করো
3. Hasan-এর salary 30000 থেকে 32000 করো
4. emp2-এর city "Dhaka" add করো
5. পুরো dictionary print করো
"""
employees = {
    "emp1": {
        "name": "Hasan",
        "salary": 30000
    },
    "emp2": {
        "name": "Rafi",
        "salary": 35000
    }
}
print(employees["emp1"]["name"])
print(employees["emp2"]["salary"])

employees["emp1"]["salary"]=3200
print(employees["emp1"]["salary"])
employees["emp2"]["city"]="Dhaka"
for key , value in employees.items():
    print(key,value)

for emp_id,emp_info in employees.items():
    print(emp_id)
    for key , value in emp_info.items():
        print(key,value) 

