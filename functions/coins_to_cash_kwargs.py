def calc_dollars(**coins):
    total_amount = 0
    for (key, value) in coins.items():
        if(key == "pennies"):
            total_amount += value*.01
        elif(key == "nickels"):
            total_amount += value*.05
        elif(key == "dimes"):
            total_amount += value*.10
        elif(key == "quarters"):
            total_amount += value*.25
    print(total_amount)
    

# expected output 8.07
calc_dollars(pennies= 342, nickels=9, dimes=32, quarters=4)
