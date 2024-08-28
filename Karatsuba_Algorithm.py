
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

# PART 1

def downstream_simple (number_1, number_2):
    split_index = int(len(int_to_digit_list(number_1))/2)
    list_1 = int_to_digit_list (number_1)
    list_2 = int_to_digit_list (number_2)
    list_1_front, list_1_back = list_1[:-split_index], list_1[-split_index:]
    list_2_front, list_2_back = list_2[:-split_index], list_2[-split_index:]
    number_1_front, number_1_back = digit_list_to_int(list_1_front), digit_list_to_int(list_1_back)
    number_2_front, number_2_back = digit_list_to_int(list_2_front), digit_list_to_int(list_2_back)
    return [number_1_front, number_2_front, number_1_back, number_2_back, number_1_front+number_1_back, number_2_front+number_2_back]

def downstream_list (list_in):
    list_out = []
    for k in range (0, len(list_in), 2):
        list_out.extend (downstream_simple(list_in[k],list_in[k+1]))
    return list_out

def downstream_recursive (list_in):
    list_processed = list_in
    while list_processed[0] >= 10:
        list_processed = downstream_list(list_processed)
    list_out = list_processed
    return list_out

# PART 2

def upstream_base (list_in):
    list_out = []
    for k in range (0, len(list_in), 2):
        list_out.append (list_in[k] * list_in[k+1])
    return list_out

# PART 3

def upstream_simple (level, triple):
    product = pow(10,2*level)*triple[0] + pow(10,level)*(triple[2]-triple[0]-triple[1]) + triple[1]
    return product

def upstream_list (level, list_in):
    product_list = []
    for k in range (0, len(list_in), 3):
        processed_items = list_in[k:k+3]
        product_list.append (upstream_simple (level, processed_items))
    return product_list

def upstream_recursive (list_in):
    level = 1
    list_processed = list_in
    while len(list_processed) != 1:
        list_processed = upstream_list (level, list_processed)
        level = 2*level
    final_product = list_processed[0]
    return final_product

# KARATSUBA ALGORITHM

def input_numbers(number1, number2):
    input_list = [number1,number2]
    return input_list


def karatsuba_algorithm (number1, number2):
    """KARATSUBA Algorithm (KA)
    KA makes multiplication of integers. Numbers to be multiplied have equal number of digits and the number of digits is a power of 2
    KA is described in the book: Algorithms Illuminated Part 1, section 1.3
    In the Karatsuba multiplication there are two stages:
    1) downstream stage - the output are numbers half the length of the original numbers
    2) upstream stage - the operation that involoves multiplication of items of the output of the downstream; the output of the upstream is the final product.
    In case of numbers longer than 2 digits, Karatsuba multiplication is to be performed recursively. Karatsuba Algorithm consists of three parts:
    PART 1 - the downstream part: it is downstream stage performed recursively
    PART 2 - the firs upstream step: the upstream stage for the case where numbers are one digit long or one and two digit long
    PART 3 - the recursive upstream part: the upstraem stage for longer input numbers applied recursively

    PART 1
    The downstream part consists of three main functions:
    1) downstream_simple - downstream stage for two numbers (i.e. 1234, 5678 -> 12, 34, 56, 78, 46, 134)
    2) downstream_list - downstream_simple applied to pairs of numbers on the list (i.e. [12, 34, 56, 78, 46, 134] -> [1,5,2,6,3,11,3,7,4,8,7,15,4,13,6,4,10,17]
    3) downstream_recursive - the recursive application of the above two

    PART 2
    The first upstream step as prescribed by the algorithm performed on one digit numbers or one and two digit numbers.

    PART 3
    The upstream part consists of three main functions:
    1) upstream_simple - upstream stage for three numbers
    2) upstream_list - upstream_simple applied to triples of numbers on the list
    3) upstream_recursive - the recursive application of the above two
    """
    step1 = downstream_recursive (input_numbers(number1, number2))
    step2 = upstream_base (step1)
    step3 = upstream_recursive (step2)
    return step3

if __name__ == "__main__":
    number1 = int(input("Enter the first number for the multiplication: "))
    number2 = int(input("Enter the second number for the multiplication: "))
    print (karatsuba_algorithm (number1, number2))
