# For multiples of five (5, 10, 15, etc.) print "Chicken" instead of the number
# For the multiples of seven (7, 14, 21, etc.) print "Monkey".
# For numbers which are multiples of both five and seven print "ChickenMonkey".

list_of_numbers = range(1, 101)

for num in list_of_numbers:
    if(num % 5 == 0 and num % 7 == 0):
        print(f"{num} ChickenMonkey")
    elif(num % 5 == 0):
        print(f"{num} Chicken")
    elif(num % 7 == 0):
        print(f"{num} Monkey")
    else:
        print(num)