#!/usr/bin/env python3

from calculator import add, subtract, multiply, divide, operations


number_1 = input(f'{"Enter first integer: ":>22}')
operation = input(f'{"Enter operation: ":>22}')
number_2 = input(f'{"Enter second integer: ":>22}')

result = operations[operation](number_1, number_2)

print(f'{"Result: ":>22}{result}')
