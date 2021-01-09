from decimal import Decimal


def add(a, b):
    return Decimal(a) + Decimal(b)


def subtract(a, b):
    return Decimal(a) - Decimal(b)


def multiply(a, b):
    return Decimal(a) * Decimal(b)


def divide(a, b):
    try:
        return Decimal(a) / Decimal(b)
    except ZeroDivisionError:
        return 0
