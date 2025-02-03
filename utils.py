import math

def is_odd(number):
    if number % 2 == 0:
        return False
    return True

def is_prime(number):
    if number <=1:
        return False

    for num in range(2, int(math.sqrt(number)) + 1):
        if number % num == 0:
            return False
    return True

def is_armstrong(number):
    if number < 0:
        return False

    length = len(str(number))
    digit_sum = 0

    for i in range(length):
        digit = str(number)[i]
        digit_sum += int(digit) ** length

    return digit_sum == number

def is_perfect(number):
    if number <= 1:
        return False

    num_sum = 1
    for num in range(2, int(math.sqrt(number)) + 1):
        if number % num == 0:
            num_sum += num
            if num != number//num:
                num_sum += number//num

    if num_sum == number and num_sum != 1:
        return True
    return False

def sum_digit(number):
    digit_sum = 0
    for num in str(abs(number)):
        digit_sum += int(num)

    return digit_sum

def find_property(number):
    num_property = []
    if is_armstrong(number):
        num_property.append("armstrong")
    if is_odd(number):
        num_property.append("odd")
    else:
        num_property.append("even")

    return num_property
