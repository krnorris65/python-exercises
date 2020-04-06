import random
"""
Print a message to the console indicating whether each value of
`number` is in the `my_randoms` list.
"""

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6, 1))

# Generate a list of numbers 1..10
numbers_1_to_10 = range(1, 10)

# Iterate from 1 to 10
for number in numbers_1_to_10:
    the_numbers_match = False

    # Iterate your random number list here
    for ran_num in my_randoms:
        # Do the two numbers match? Change the boolean.
        if ran_num == number:
            the_numbers_match = True

    if the_numbers_match:
        print(f'{number} is in the random list')
    else:
        print(f'{number} is NOT in the random list')

# Alternate Way
# # Iterate from 1 to 10
# for number in numbers_1_to_10:
#     the_numbers_match = False

#     # How many times does my_randoms contain number
#     num = my_randoms.count(number)
#     # if the number is greater than 0 then it is in the random list
#     if num != 0:
#         print(f'{number} is in the random list')
#     else:
#         print(f'{number} is NOT in the random list')
