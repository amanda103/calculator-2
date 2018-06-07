"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from math_calc import *


def welcome_message():
    """ prints welcome message and instructions for calculator input"""

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


def split_input():
    input_string = input("> ")
    tokens = input_string.split(" ")
    return tokens


def interpret_operand():

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
    return result


welcome_message()

allowed_operands = ["+", "-", "*", "/", "mod", "square", "cube", "pow", "+*", "+**"]
playing = True
while playing:

    tokens = split_input()
    operand = tokens[0]
    if operand == "q" or operand == "quit":
        break

    nums = tokens[1:]

    if operand not in allowed_operands:
        print("Please enter an allowed operand")
    else:
        for num in nums:
            if num.isdigit() is False:
                print("Please enter valid numbers")
            else:
                num1 = int(nums[0])

                if len(nums) > 1:
                    num2 = int(nums[1])
                    if len(nums) > 2:
                        num3 = int(nums[2])
    print(interpret_operand())
