"""
এই dictionary:
student = {    "name": "Karim",    "age": 22,    "department": "EEE"}
Task:
1. Karim print করো
2. age 22 থেকে 23 করো
3. নতুন key "city" add করো, value "Dhaka"
4. department remove করো
5. final dictionary print করো
"""
student = {
    "name": "Karim",
    "age": 22,
    "department": "EEE"
}
print(student["name"])
student["age"]=23
student["City"]="Dhaka"
student.pop("department")
print(student)
"""
এই dictionary:
product = {    "name": "Laptop",    "price": 80000,    "brand": "Dell"}
1. keys() দিয়ে সব key print করো
2. values() দিয়ে সব value print করো
3. items() + for loop দিয়ে এমন output করো:
"""
product = {
    "name": "Laptop",
    "price": 80000,
    "brand": "Dell"
}
print(product.keys())
print(product.values())
for key , value in product.items():
    print(key,value)
    


