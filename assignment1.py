
# 1. STRING CONCATENATI

name = input("Enter your Name: ")

string1 = "Hello "
string2 = name

result = string1 + string2

print("\nConcatenated String:")
print(result)

string3 = ", welcome to Python programming"

result = result + string3

print(result) 

# 2. STRING SLICING AND INDEXING
print("\n--- String Slicing and Indexing ---")

# a. First character
print("First character:", result[0])

# b. Last character
print("Last character:", result[-1])

# c. First 5 characters
print("First 5 characters:", result[:5])

# d. Last 11 characters
print("Last 11 characters:", result[-11:])

# e. Reverse the string
print("Reverse:", result[::-1])

# f. Print the word Python
print("Word Python:", result[17:23])

# 3. STRING METHODS

print("\n--- String Methods ---")

strM = "Python beginner tutorial"

# a. Convert to uppercase
print("Uppercase:", strM.upper())

# b. Convert to lowercase
print("Lowercase:", strM.lower())

# c. Capitalize
print("Capitalize:", strM.capitalize())

# d. Count character 't'
print("Number of 't' characters:", strM.count("t"))

# e. Replace Python with Machine Learning
print("After replacement:",
      strM.replace("Python", "Machine Learning"))

# 4. TUPLES

print("\n--- Tuples ---")

# Create two tuples
t1 = (10, 20, 30)
t2 = (40, 50, 60)

# a. Concatenate the tuples
t_combine = t1 + t2

print("Combined tuple:", t_combine)

# b. Repeat t_combine 3 times
t_repeat = t_combine * 3

print("Tuple repeated 3 times:", t_repeat)

# c. Access the 3rd element
print("3rd element:", t_combine[2])

# d. Access the first three elements
print("First three elements:", t_combine[:3])

# e. Access the last three elements
print("Last three elements:", t_combine[-3:])