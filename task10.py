import math


def find_absolute_value(number):
    absolute_value = abs(number)
    return absolute_value


if __name__ == '__main__':
    while True:
        try:
            your_number = int(input("Give a number "))
            print(f'{find_absolute_value(your_number)}')
        except ValueError:
            print("You inserted not a number!")
        else:
            break








