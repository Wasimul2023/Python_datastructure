# Set Add 
fruits={ "Apple","Banana"}
fruits.add("Mango")
print(fruits)
# Multipule add
fruits.update(["Grape","Orange","Woodapple"])
print(fruits)
# Remove operation 
fruits.remove("Apple")
print(fruits)
# Mathematical operation 
A={1,2,3,4}

B={3,4,5,6}
# Union(|) 
print(A|B)
#Intersection(&)
print(A&B)
# Deference(-)
print(A-B)
#Symmetric Difference(^):(common gula bad )
print(A^B)

#Practice:
"""
Code লিখো:
একটা set বানাও:
Apple
Banana
Mango
তারপর:
1. Orange add করো
2. Banana remove করো
3. Set print করো
"""
exam = {"Apple","Banana","Mango"}
exam.add("Orange")
exam.remove("Banana")
print(exam)
