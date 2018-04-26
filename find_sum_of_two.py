def find_sum_of_two(list_of_numbers = None, sum_of_two = None):
    first_number_for_sum = 0
    second_number_for_sum = 0
    sum_of_two_number = 0
    if list_of_numbers != None and sum_of_two != None:
        for index, number in enumerate(list_of_numbers):
            if index < (len(list_of_numbers) -1):
                for second_index, second_number in enumerate(list_of_numbers[index + 1:]):
                    sum_of_two_number = number + second_number
                    if sum_of_two_number == sum_of_two:
                        first_number_for_sum = number
                        second_number_for_sum = second_number
        if first_number_for_sum != 0 and second_number_for_sum != 0 and sum_of_two_number != 0:
            print("Both {} and {} sums to {}".format(first_number_for_sum, second_number_for_sum, sum_of_two))
        else:
            print("No matching numbers found in the list for the sum {}".format(sum_of_two))
    else:
        print("List of numbers and sum of two values is required to check.")


find_sum_of_two()
find_sum_of_two([3, 10, 45, 15, 8], 18)
find_sum_of_two([10, 3, 45, 15, 7], 13)
find_sum_of_two([10, 3, 45, 15, 7], 22)
