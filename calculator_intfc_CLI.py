#!/usr/bin/env python3

import decimal
from decimal import Decimal
from calculator import add, subtract, multiply, divide
import array as arr
from calculator_db_funcs_postgresql import db_postgresql_connect
import psycopg2


def get_decimal(prompt):
    while True:
        number = input(f'{prompt:>22}')
        try:
            number = Decimal(number)
            break
        except decimal.InvalidOperation:
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


operations_array_total = arr.array('i', [0, 0, 0, 0])
operations_array_session = arr.array('i', [0, 0, 0, 0])

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


db_conn = db_postgresql_connect()

name = input(f'{"Enter name: ":>22}')

cur = db_conn.cursor()
the_sql = "SELECT addition, subtraction, multiplication, division FROM calculator WHERE user_name = '" + name + "';"
try:
    cur.execute(the_sql)
except psycopg2.Error as error:
    print(error)
rows = cur.fetchall()
db_conn.commit()


for x in range(4):
    operations_array_total[x-1] = rows[0][x-1]

print("Name: " + name
      + ", Add: " + str(operations_array_total[0])
      + ", Sub: " + str(operations_array_total[1])
      + ", Mult: " + str(operations_array_total[2])
      + ", Div: " + str(operations_array_total[3]))

while True:
    print("This Session:"
          + ": Add: " + str(operations_array_session[0])
          + ", Sub: " + str(operations_array_session[1])
          + ", Mult: " + str(operations_array_session[2])
          + ", Div: " + str(operations_array_session[3]))

    number_1 = get_decimal("Enter first integer: ")
    operation = get_operation("Enter operation: ", "+-*/")
    number_2 = get_decimal("Enter second integer: ")

    result = operations[operation](number_1, number_2)
    operations_array_session[operations_index[operation]] += 1

    print(f'{"Result: ":>22}{result}')

    answer = prompt_yn("Do another (y/n):", "yn")

    if answer == 'n':
        break

print("This Session:"
      + ": Add: " + str(operations_array_session[0])
      + ", Sub: " + str(operations_array_session[1])
      + ", Mult: " + str(operations_array_session[2])
      + ", Div: " + str(operations_array_session[3]))

operations_array_total[0] += operations_array_session[0]
operations_array_total[1] += operations_array_session[1]
operations_array_total[2] += operations_array_session[2]
operations_array_total[3] += operations_array_session[3]


print("Name: " + name
      + ", Add: " + str(operations_array_total[0])
      + ", Sub: " + str(operations_array_total[1])
      + ", Mult: " + str(operations_array_total[2])
      + ", Div: " + str(operations_array_total[3]))

cur = db_conn.cursor()

the_sql = "UPDATE calculator SET addition = addition + " + str(operations_array_session[0]) \
          + ", subtraction = subtraction + " + str(operations_array_session[1]) \
          + ", multiplication = multiplication + " + str(operations_array_session[2]) \
          + ", division = division + " + str(operations_array_session[3]) + ";"

cur.execute(the_sql)
db_conn.commit()
cur.close()

# Close postgesql database connection
db_conn.close()
