#!/usr/bin/env python3

import decimal
from decimal import Decimal
from calculator import add, subtract, multiply, divide
import array as arr
from calculator_db_funcs_postgresql import db_postgresql_connect, db_postgresql_select, \
    db_postgresql_update, db_postgresql_insert


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


def prompt_single(prompt, values):
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

while True:
    name = input(f'{"Enter name: ":>22}')

    the_sql = "SELECT addition, subtraction, multiplication, division FROM calculator WHERE user_name = '" + name + "';"
    rows = db_postgresql_select(db_conn, the_sql)

    if not rows:
        print("I've not seen {} before".format(name))

        answer = prompt_single("Is that name correct? (y/n):", "yn")

        if answer == 'y':
            the_sql = "INSERT INTO calculator(user_name) " \
                      "VALUES('" + name + "') " \
                      "RETURNING addition, subtraction, multiplication, division"
            rows = db_postgresql_insert(db_conn, the_sql)

            if rows:
                break
            else:
                print("Something went wrong very wrong.")
                break
        else:
            pass
    else:
        for x in range(4):
            operations_array_total[x-1] = rows[0][x-1]
        break

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

    answer = prompt_single("Do another (y/n):", "yn")

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


the_sql = "UPDATE calculator SET addition = addition + " + str(operations_array_session[0]) \
          + ", subtraction = subtraction + " + str(operations_array_session[1]) \
          + ", multiplication = multiplication + " + str(operations_array_session[2]) \
          + ", division = division + " + str(operations_array_session[3]) + ";"
rowcount = db_postgresql_update(db_conn, the_sql)

if not rowcount:
    print("nothing updated")


# Close postgesql database connection
db_conn.close()
