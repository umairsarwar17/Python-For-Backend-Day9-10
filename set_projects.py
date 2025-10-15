'''
Project 1: Unique Numbers
Project 2: Common Languages
Project 3: Students in Events
Project 4: Convert List to Set
Project 5: Set Operations Practice
'''
#...Remove duplicates from a list using sets
numbers = [1, 2, 2, 3, 4, 4, 5]
unique = set(numbers)
print("Unique Numbers:", unique)
#...Find common languages known by two people
person1 = {"Python", "C++", "Java"}
person2 = {"Python", "C#", "JavaScript"}
common = person1.intersection(person2)
print("Common Languages:", common)
#......Find students attending both events.
event_A = {"Ali", "Sara", "Ahmed", "Zara"}
event_B = {"Sara", "Usman", "Ahmed"}
print("Both Events:", event_A & event_B)
print("Only in A:", event_A - event_B)
print("All Students:", event_A | event_B)
#....Show how set removes duplicates automatically.
items = ["pen", "pencil", "pen", "eraser", "book", "book"]
unique_items = set(items)
print("Unique Items:", unique_items)
#...Practice all set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A - B):", A - B)
print("Symmetric Difference:", A ^ B)
