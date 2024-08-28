def int_to_digit_list(number):
"""int_to_digit_list transforms an integer into a list of it digits"""
    list_of_digits = []
    while number > 0:
        list_of_digits.insert(0, number % 10)
        number = (int)(number/10)
    return list_of_digits

def digit_list_to_int(list_of_digits):
"""digit_list_to_int transforms a list of it digits into a number"""
    number = 0
    mul = 1
    for i in range (len(list_of_digits)):
        number += list_of_digits[-1-i] * mul
        mul *= 10
    return number
