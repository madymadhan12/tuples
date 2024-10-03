...
 Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple
...
tuple_input = input("Enter tuple elements separated by spaces: ")
tuple_data = tuple(tuple_input.split())
x = input("Enter the value to count its occurrences: ")
count_x = tuple_data.count(x)
print(f"The value '{x}' appears {count_x} times in the tuple.")
...
Enter tuple elements separated by spaces: 3
Enter the value to count its occurrences: 2
The value '2' appears 0 times in the tuple.
