# Create a function called calc_dollars. In the function body, define a dictionary and store it in a variable named piggyBank. The dictionary should have the following keys defined.

# quarters
# nickels
# dimes
# pennies

# expected output 7.07

piggy_bank = {
    "pennies": 342,
    "nickels": 9,
    "dimes": 32
}

def calc_dollars(bank):
    total_amount = 0
    for (coin, value) in bank.items():
        if(coin == "pennies"):
            total_amount += value*.01
        elif(coin == "nickels"):
            total_amount += value*.05
        elif(coin == "dimes"):
            total_amount += value*.10
        elif(coin == "quarters"):
            total_amount += value*.25
    print(total_amount)
    


calc_dollars(piggy_bank)
