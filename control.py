# I've updated this comment.

def comparison_demo(num1, num2):
    """
    :param num1: number
    :param num2: number
    :return: Prints a string stating whether num1 is greater than, equal to, or less than num2
    """
    if num1 > num2:
        print(num1, 'is greater than', num2)
    elif num1 == num2:
        print(num1, 'and', num2, 'are equal')
    else:
        print(num1, 'is less than', num2)


comparison_demo(3, 4)
comparison_demo(3, 3)


def while_demo(input_int):
    """
    :param input_int: integer
    :return: returns the first multiple of 10 that is greater than or equal to input_int
    """
    multiple = input_int

    # Increment multiple until it is a multiple of 10
    while multiple % 10 != 0:
        multiple = multiple + 1

    return multiple

print('Smallest multiple of 10 at least as big as 10:', while_demo(10))
print('Smallest multiple of 10 at least as big as 11:', while_demo(11))



def for_demo(input_int):
    """
    :param input_int: integer
    :return: sum of all integers from 1 to input_int, inclusive
    """
    sum = 0
    for current_int in range(1, input_int + 1):
        sum = sum + current_int

    return sum

sum = for_demo(3)
print('Sum of integers from 1 to 3:', sum)



def is_prime(input_int):
    """
    :param input_int: integer
    :return: True if test_int is prime. False, otherwise.
    """
    for test_divisor in range(2, input_int):
        if input_int % test_divisor == 0:
            return False

    return True

print('10 is prime:', is_prime(10))
print('5 is prime:', is_prime(5))
