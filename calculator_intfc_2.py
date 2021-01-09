#!/usr/bin/env python3

import calculator
import decimal
from decimal import Decimal

from calculator import add, subtract, multiply, divide


def get_decimal(prompt):
    while True:
        number = input(f'{prompt:>22}')
        try:
            number = Decimal(number)
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


def prompt_yn(prompt, values):
    while True:
        value = input(f'{prompt:>22}')

        if len(value) != 1:
            print("Try answer again")
            continue

        if value in values:
           break

        print("Try answer again")

    return(value)


operations = {'+' : add,
              '-' : subtract,
              '*' : multiply,
              '/' : divide,
             } 

while True:
    number_1  = get_decimal("Enter first integer: ")
    operation = get_operation("Enter operation: ", "+-*/")
    number_2  = get_decimal("Enter second integer: ")

    result = operations[operation](number_1, number_2)

    print(f'{"Result: ":>22}{result}')

    answer = prompt_yn("Do another (y/n):", "yn")

    if answer == 'n':
        break