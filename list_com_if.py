# Normal Way : 
"""
even=[]
numbers=[1,2,3,4,5,6,7,8,9,10]
for n in numbers:
    if n%2==0:
        even.append(n)
        print(even)
        """
numbers=[1,2,3,4,5,6,7,8,9,10]
even=[n for n in numbers if n%2==0]
print(even)

odd = [n for n in range(1,10)if n%2!=0]
print(odd)