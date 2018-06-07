"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from math_calc import *

print("Welcome to our calculator. Enter an operand followed by the number(s) you want to perform operations on.")
print("Addition: +")
print("Subtraction: -")
print("Multiplication: *")
print("Division: /")
print("Remainder: mod")
print("Square: square")
print("Cube: cube")
print("Power: pow")
print("Add and multiply: +*")
print("Add cubes: +**")
print("To exit the calculator, enter 'q' or 'quit'")

allowed_operands = ["+", "-", "*", "/", "mod", "square", "cube", "pow", "+*", "+**"]
playing = True
while playing:
    input_string = input("> ")
    if input_string == "q" or input_string == "quit":
        playing = False

    tokens = input_string.split(" ")

    operand = tokens[0]
    
    if operand not in allowed_operands:
        print("That operand is not allowed, please try again")
    else:
        for token in tokens(1: len(tokens)):
            if token.isdigit() is False:
                print("Please enter valid numbers")
            else:
                num1 = int(tokens[1])

                if len(tokens) > 2:
                    num2 = int(tokens[2])
                    if len(tokens) > 3:
                        num3 = int(tokens[3])

                if operand == "+":
                    result = add(num1, num2)
                elif operand == "-":
                    result = subract(num1, num2)
                elif operand == "*":
                    result = multiply(num1, num2)
                elif operand == "/":
                    result = divide(num1, num2)
                elif operand == "square":
                    result = square(num1)
                elif operand == "cube":
                    result = cube(num1)
                elif operand == "pow":
                    result = power(num1, num2)
                elif operand == "mod":
                    result = mod(num1, num2)
                elif operand == "+*":
                    result = add_mult(num1, num2, num3)
                elif operand == "+**":
                    result = add_cubes(num1, num2)

print(result)
