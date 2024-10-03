...
 Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
...
tuple_input = input("Enter tuple elements separated by spaces: ")
tuple_data = tuple(map(int, tuple_input.split()))
x = int(input("Enter the number to count its occurrences: "))
count_x = tuple_data.count(x)
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
factorial_of_count = calculate_factorial(count_x)
print(f"The number {x} appears {count_x} times in the tuple.")
print(f"The factorial of the count {count_x} is: {factorial_of_count}")
...
Enter tuple elements separated by spaces: 2 2 3 4 5
Enter the number to count its occurrences: 2
The number 2 appears 2 times in the tuple.
The factorial of the count 2 is: 2
