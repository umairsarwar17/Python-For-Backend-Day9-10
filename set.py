'''
What is a Set?
A set is an unordered collection of unique items.
No duplicates, and elements can’t be accessed by index
'''
fruits = {"apple", "banana", "mango", "apple"}
print(fruits)   # {'apple', 'banana', 'mango'}  (duplicates removed)
#Common Set Operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))         # {1, 2, 3, 4, 5, 6}
print(A.intersection(B))  # {3, 4}
print(A.difference(B))    # {1, 2}
#Conversion from List to Set
nums = [1, 2, 2, 3, 4, 4]
unique_nums = set(nums)
print(unique_nums)  # {1, 2, 3, 4}
