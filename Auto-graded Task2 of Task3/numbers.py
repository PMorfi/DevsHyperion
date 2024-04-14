"""Create a new Python file called numbers.py.
? Ask the user to enter three different integers.
? Then print out:
? The sum of all the numbers
? The first number minus the second number
? The third number multiplied by the first number
? The sum of all three numbers divided by the third number"""
# Ask the user to enter three different integers
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Calculate and print the sum of all the numbers
sum_of_numbers = num1 + num2 + num3
print("Sum of all the numbers:", sum_of_numbers)

# Calculate and print the result of the first number minus the second number
first_minus_second = num1 - num2
print("First number minus second number:", first_minus_second)

# Calculate and print the result of the third number multiplied by the first number
third_times_first = num3 * num1
print("Third number multiplied by the first number:", third_times_first)

# Calculate and print the result of the sum of all three numbers divided by the third number
sum_divided_by_third = sum_of_numbers / num3
print("Sum of all three numbers divided by the third number:", sum_divided_by_third)
