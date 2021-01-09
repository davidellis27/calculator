#!/usr/bin/env python3

from decimal import Decimal
from calculator import add, subtract, multiply, divide
import array as arr


def get_decimal(prompt):
    while True:
        number = input(f'{prompt:>22}')
        try:
            number = Decimal(number)
            break
        except ValueError:
            print("Try integer again")

    return number


def get_operation(prompt, operators):
    while True:
        operator = input(f'{prompt:>22}')

        if len(operator) != 1:
            print("Try operator again")
            continue

        if operator in operators:
            break

        print("Try operator again")

    return operator


def prompt_yn(prompt, values):
    while True:
        value = input(f'{prompt:>22}')

        if len(value) != 1:
            print("Try answer again")
            continue

        if value in values:
            break

        print("Try answer again")

    return value


operations_array = arr.array('i', [0, 0, 0, 0])

operations = {'+': add,
              '-': subtract,
              '*': multiply,
              '/': divide,
              }

operations_index = {'+': 0,
                    '-': 1,
                    '*': 2,
                    '/': 3,
                    }

name = input(f'{"Enter name: ":>22}')

while True:
    print("Add: " + str(operations_array[0])
          + ", Sub: " + str(operations_array[1])
          + ", Mult: " + str(operations_array[2])
          + ", Div: " + str(operations_array[3]))

    number_1 = get_decimal("Enter first integer: ")
    operation = get_operation("Enter operation: ", "+-*/")
    number_2 = get_decimal("Enter second integer: ")

    result = operations[operation](number_1, number_2)
    operations_array[operations_index[operation]] += 1

    print(f'{"Result: ":>22}{result}')

    answer = prompt_yn("Do another (y/n):", "yn")

    if answer == 'n':
        break

print("Name: " + name
      + ", Add: " + str(operations_array[0])
      + ", Sub: " + str(operations_array[1])
      + ", Mult: " + str(operations_array[2])
      + ", Div: " + str(operations_array[3]))
