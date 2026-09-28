#remove()Value দিয়ে element remove করে।
numbers = [10,20,30,40]
numbers.remove(30)
print(numbers)

# pop()Index দিয়ে remove করে এবং সেই value return করে।
numbers = [10,20,30,40]
x = numbers.pop(2)
print(numbers)
print(x)

#del Index দিয়ে delete করে।
numbers=[10,20,30,40]
del numbers[1]
print(numbers)

"""
Practice 6:
এই list দেওয়া আছে:
Banana remove করো using remove()
Mango remove করো using pop()
Final list print করো
"""
fruits=["Apple","Banana","Mango","Orange"]
fruits.remove("Banana")
x= fruits.pop(1)
print(fruits)