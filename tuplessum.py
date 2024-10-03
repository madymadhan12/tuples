...
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
...
tuple_input = input("Enter tuple elements separated by spaces: ")
tuple_data = tuple(map(int, tuple_input.split()))  
total_sum = 0
for element in tuple_data:
    total_sum += element
print("The sum of the tuple elements is:", total_sum)
...
Enter tuple elements separated by spaces: 10 20 30 40
The sum of the tuple elements is: 100
