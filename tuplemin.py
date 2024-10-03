...
Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
...
PROGRAM
...
n = int(input("Enter the number of elements: "))
elements = []
for i in range(n):
    element = float(input(f"Enter element {i+1}: "))  
    elements.append(element)
tuple_data = tuple(elements)
min_value = min(tuple_data)
print("The minimum value of the tuple elements:", min_value)
...
OUTPUT
...
Enter the number of elements: 5
Enter element 1: 1
Enter element 2: 2
Enter element 3: 3
Enter element 4: 4
Enter element 5: 5
The minimum value of the tuple elements: 1.0
