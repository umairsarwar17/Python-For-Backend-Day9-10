'''
What is a Tuple?
A tuple is like a list but immutable — once created, you cannot change its elements.
'''
countries = ("Pakistan", "USA", "UK", "Canada")
print(countries)
#Indexing & Slicing(you can access elements like a list.)
print(countries[0])      # Pakistan
print(countries[-1])     # Canada
print(countries[1:3])    # ('USA', 'UK')
#Tuple Methods(Tuples have only two main methods)
nums = (1, 2, 2, 3, 4)
print(nums.count(2))   # Counts how many times 2 appears
print(nums.index(3))   # Finds index of first 3
#Immutability Example
countries = ("Pakistan", "USA", "UK")
countries[1] = "China"    #  Error! Tuples cannot be changed
#
