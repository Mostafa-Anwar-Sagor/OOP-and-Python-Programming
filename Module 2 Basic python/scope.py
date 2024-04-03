balance =300

def buy_things(item,price):
    balance=balance-price
    print(f'balace after buying {item}',balance)
    

buy_things('sunglass',100)