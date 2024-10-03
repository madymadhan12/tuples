...
 Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
...
Sample Input:
3
10
20
30
Sample Output:
60
...
n = int(input("Enter the number of tuple elements: "))
tuple_elements = []
for i in range(n):
    element = float(input(f"Enter element {i+1}: "))  
    tuple_elements.append(element)
tuple_data = tuple(tuple_elements)
tuple_sum = sum(tuple_data)
print("Sum of the tuple elements:", tuple_sum)
...
Enter the number of tuple elements: 3
Enter element 1: 1
Enter element 2: 2
Enter element 3: 3
Sum of the tuple elements: 6.0
