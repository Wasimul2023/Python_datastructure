#Normal way:
""""
numbers=[]
for i in range(5):
    numbers.append(i)
print(numbers)
"""
#List comprehension:
""""
numbers=[i for i in range(5)]
print(numbers)
"""

numbers = [i*2 for i in range(5)]

print(numbers)
