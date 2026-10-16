""""
name print করো
age 21 → 22 update করো
city = "Dhaka" add করো
department remove করো
Updated dictionary print করো
"""
"""
student = {
    "name": "Rahim",
    "age": 21,
    "department": "CSE"
}
print(student["name"])
student["age"]=23
student["city"]="Dhaka"
student.pop("department")
print(student)
"""
"""
product = {
    "name": "Laptop",
    "price": 80000,
    "brand": "Dell",
    "ram": "16GB"
}
for key , value in product.items():
    print(key, value)
  """
"""
Code লিখে:
- Nabil-এর নাম print করো
- Rafi-এর salary print করো
- Hasan-এর salary 30000 → 32000 করো
- emp3-এর city = "Chittagong" add করো
- পুরো dictionary print করো
"""
"""
employees = {
    "emp1": {
        "name": "Hasan",
        "salary": 30000
    },
    "emp2": {
        "name": "Rafi",
        "salary": 35000
    },
    "emp3": {
        "name": "Nabil",
        "salary": 40000
    }
}
print(employees["emp3"]["name"])
print(employees["emp2"]["salary"])
employees["emp1"]["salary"]=32000
employees["emp3"]["City"]="Chittagong"
print(employees)
"""
"""
employees = {
    "emp1": {
        "name": "Hasan",
        "salary": 32000
    },
    "emp2": {
        "name": "Rafi",
        "salary": 35000
    },
    "emp3": {
        "name": "Nabil",
        "salary": 40000,
        "City" : "Chittagong"
       
    }
}
for emp_id , emp_info in employees.items():
    print(emp_id)
  
    for key , value in emp_info.items():
        print( key,value)
"""

employees = {
    "E101": {
        "name": "Rahim",
        "department": "IT",
        "salary": 50000
    },
    "E102": {
        "name": "Karim",
        "department": "HR",
        "salary": 45000
    },
    "E103": {
        "name": "Nabil",
        "department": "IT",
        "salary": 60000
    }
}
for emp_id , emp_info in employees.items():
        if emp_info["department"] == "IT":
            #print(emp_id)
            emp_info.pop("department")
             
            for key , value in emp_info.items():
               print(value)
               

"""
users = {
    "u101": {
        "name": "Rahim",
        "email": "rahim@gmail.com",
        "city": "Dhaka"
    },
    "u102": {
        "name": "Karim",
        "email": "karim@gmail.com",
        "city": "Chittagong"
    }
}
for u_id , u_info in users.items():
    print(u_id)
    for key , value in u_info.items():
        print(key , value )
        """