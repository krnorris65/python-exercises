import math

dollar_amount = 8.69

piggy_bank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}
# calc_coins original
# def calc_coins (amount):
#     total_remaining = amount
#     while(total_remaining != 0):
#         if(total_remaining >= .25):
#             num_quarters = math.floor(total_remaining/.25)
#             piggy_bank["quarters"] = num_quarters
#             print(total_remaining%.25)
#             total_remaining -= num_quarters*.25
#         elif(total_remaining >= .10):
#             num_dimes = math.floor(total_remaining/.10)
#             piggy_bank["dimes"] = num_dimes
#             total_remaining -= num_dimes*.10
#         elif(total_remaining >= .05):
#             num_nickels = math.floor(total_remaining/.05)
#             piggy_bank["nickels"] = num_nickels
#             total_remaining -= num_nickels*.05
#         else: 
#             piggy_bank["pennies"] = math.ceil(total_remaining/.01)
#             total_remaining = 0

# calc_coins rewritten
def calc_coins (amount):
    total_remaining = amount
    while(total_remaining != 0):
        if(total_remaining >= .25):
            piggy_bank["quarters"] = int(total_remaining/.25)
            total_remaining = round(total_remaining%.25, 2)
        elif(total_remaining >= .10):
            piggy_bank["dimes"] = int(total_remaining/.10)
            total_remaining = round(total_remaining%.10, 2)
        elif(total_remaining >= .05):
            piggy_bank["nickels"] = int(total_remaining/.05)
            total_remaining = round(total_remaining%.05, 2)
        else: 
            piggy_bank["pennies"] = int(total_remaining/.01)
            total_remaining = 0

calc_coins(dollar_amount)
print(piggy_bank)
# { 'quarters': 34, 'nickels': 1, 'dimes': 1, 'pennies': 4 }