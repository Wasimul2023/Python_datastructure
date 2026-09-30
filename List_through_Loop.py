"""
numbers=[5,10,15,20,25]
Task:
1. for loop ব্যবহার করে সব number print করো।
2. সব number এর সাথে 10 যোগ করে print করো।
"""
numbers=[5,10,15,20,25]
for n in numbers:
    n+=10
    print(n)
print(numbers)

#যদি আসল list পরিবর্তন করতে চাও:
""""
numbers=[5,10,15,20,25]
for i in range(len(numbers)):
    numbers[i]+=10
print(numbers)
"""

