#append()
#insert()
#extend()

#append() নতুন element কে list এর শেষে যোগ করে।
students = ["Rahim","Karim","Sofiq"]
students.append("Jamal")
print(students)

#insert() নির্দিষ্ট index এ element যোগ করে।

students = ["Rahim","Karim","Jamal"]
students.insert(1,"Hassan")
print(students)

#extend()একসাথে অনেক element যোগ করতে ব্যবহার হয়।
a = [1,2,3]
a.extend([4,5,6,7])
print(a)

"""
Practice 5:
numbers = [10,20,30]
 40 শেষে যোগ করো
 5 index 0 তে যোগ করো
 [60,70] একসাথে যোগ করো
"""
numbers=[10,20,30]
numbers.append(40)
numbers.insert(0,5)
numbers.extend([60,70])
print(numbers)