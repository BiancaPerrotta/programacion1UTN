def add_digits(number):
    add=0
    while number !=0:
        extNum = number % 10
        number //= 10
        add += extNum
    return add

def add_numbers(num):
    add_num = 0
    add_num += num
    return add_num

    