#!/usr/bin/env python3

import calculator
from calculator import add, subtract, multiply, divide


def get_integer(prompt):
    while True:
        number = input(f'{prompt:>22}')
        try:
            number = int(number)
            break
        except ValueError:
            print("Try integer again")

    return(number)


def get_operation(prompt, operators):
    while True:
        operation = input(f'{prompt:>22}')

        if len(operation) != 1:
            print("Try operator again")
            continue 

        if operation in operators:
           break

        print("Try operator again")

    return(operation)


operations = {'+' : add,
              '-' : subtract,
              '*' : multiply,
              '/' : divide,
             } 

number_1  = get_integer("Enter first integer: ")
operation = get_operation("Enter operation: ", "+-*/")
number_2  = get_integer("Enter second integer: ")

result = operations[operation](number_1, number_2)

print(f'{"Result: ":>22}{result}')

