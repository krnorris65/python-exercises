stockDict = {
    "GM": "General Motors",
    "CAT":"Caterpillar",
    "EK":"Eastman Kodak",
    "GE": "General Electric"
}

purchases = [
    ( 'GE', 100, '10-sep-2001', 48 ),
    ( 'CAT', 100, '1-apr-1999', 24 ),
    ( 'GE', 200, '1-jul-1998', 56 )
]

for purchase in purchases:
    stock_abrv = purchase[0]
    stock_name = stockDict[stock_abrv]
    cost = purchase[1] * purchase[3]
    print(f"I purchased {stock_name} stock for ${cost}")


purchase_summary = dict()

for purchase in purchases:
    stock_abrv = purchase[0]
    if(stock_abrv in purchase_summary.keys()):
        purchase_summary[stock_abrv].append(purchase)
    else:
        purchase_summary[stock_abrv] = [purchase]

for (key, value) in purchase_summary.items():
    print()
    print(f"----{key}----")
    total_value = 0
    for purchase in value:
        shares = purchase[1]
        amount = purchase[3]
        date = purchase[2]
        total_value += shares*amount
        print(f"{shares} shares at {amount} dollars each on {date}")
    print()
    print(f"Total value of stock in portfolio: ${total_value}")