...
 Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
...
CODE
...
n = int(input("Enter the number of tuple elements: "))
tuple_elements = []
for i in range(n):
    element = float(input(f"Enter element {i+1}: "))   
    tuple_elements.append(element)
tuple_data = tuple(tuple_elements)
max_value = max(tuple_data)
print("The maximum value of the tuple elements:", max_value)
...
OUTPUT
Enter the number of tuple elements: 4
Enter element 1: 1
Enter element 2: 2
Enter element 3: 3
Enter element 4: 4
The maximum value of the tuple elements: 4.0
