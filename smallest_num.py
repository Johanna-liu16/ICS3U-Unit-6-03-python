#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Dec 2022
# This program calculates the average

import random


def calculate_smallest_num(list_of_numbers):
    # This function identifies the largest integer
    min = list_of_numbers[0]

    for loop_counter in range(1, len(list_of_numbers)):
        if list_of_numbers[loop_counter] < min:
            min = list_of_numbers[loop_counter]

    return min


def main():
    # this function uses an array
    random_numbers = []

    # process
    for loop_counter in range(0, 10):
        a_random_number = random.randint(1, 100)  # a number between 1 and 100
        print("The random number is: {0}".format(a_random_number))
        random_numbers.append(a_random_number)
    print("")

    smallest_integer = calculate_smallest_num(random_numbers)
    print("The smallest random number is: {0}.".format(smallest_integer))


if __name__ == "__main__":
    main()
