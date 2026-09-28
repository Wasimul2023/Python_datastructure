# in Operator ব্যবহার করে আমরা শুধু check করি data আছে কিনা।
#এটা result দেয়:
# True → data আছে
# False → data নেই

students = ["Rahim","Karim","Jamal","Sakib"]

print("Rahim" in students)

#index() দিয়ে আমরা জানতে পারি কোনো value কোন position এ আছে।
students = ["Rahim","Karim","Jamal","Sakib"]

x = students.index("Jamal")

print(x)

"""
Practice 7:
Check করো "Lion" আছে কিনা (in ব্যবহার করে)
Tiger এর index বের করো (index() ব্যবহার করে)
"Horse" আছে কিনা check করো
"""
animals=["Cat","Dog","Lion","Tiger","Elephant"]
print("Lion" in animals)
x = animals.index("Tiger")
print(x)
if "Horse" in animals:
    print(animals.index("Horse"))
else:
    print("Not Found")

