...
 Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
...
Sample Input:
10 20 30
Sample Output:
3
...
tuple_input = input("Enter tuple elements separated by spaces: ")
tuple_elements = tuple(tuple_input.split())
print("Number of elements in the tuple:", len(tuple_elements))
