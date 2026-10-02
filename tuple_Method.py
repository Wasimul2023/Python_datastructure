#1. Count()
numbers=(10,20,30,10)
print(numbers.count(10))
#2. index()
print(numbers.index(20))

# conversion List to Tuple
numbers=[10,20,30]
t = tuple(numbers)
print(t)
# or Tuple to List
t=(10,20,30)
numbers=list(t)
print(numbers)

# Practice:1
#একটা tuple বানাও যেখানে থাকবে:Apple Banana Mango
#Banana print করো
#Mango এর index বের করো
Fruits =("Apple","Banana","Mango")
print(Fruits[1])
print(Fruits.index("Mango"))

