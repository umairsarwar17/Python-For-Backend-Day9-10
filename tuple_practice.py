'''
Project 1: City Info
Project 2: Student Marks
Project 3: Coordinates Storage
Project 4: Product Info Viewer
Project 5: Tuple Methods Demo
'''
#.........Store information in an immutable structure..........
city = ("Lahore", "Punjab", 11000000)
print("City Name:", city[0])
print("Province:", city[1])
print("Population:", city[2])
#.......Find average marks using a tuple.......................
marks = (78, 85, 90, 67, 88)
average = sum(marks) / len(marks)
print("Average Marks:", average)
print("Highest:", max(marks))
print("Lowest:", min(marks))
#.............Store fixed coordinates (like map points)..............
coordinates = ((33.6844, 73.0479), (24.8607, 67.0011), (31.5820, 74.3296))
for i, city in enumerate(coordinates):
    print(f"City {i+1} Coordinates:", city)
#...........Represent each product as a tuple...................
product = ("Laptop", 150000, "Dell", "Available")
print("Name:", product[0])
print("Price:", product[1])
print("Brand:", product[2])
print("Status:", product[3])
#..........Tuple Methods Demo....................
nums = (1, 2, 2, 3, 4, 2)
print("Count of 2:", nums.count(2))
print("Index of 3:", nums.index(3))
