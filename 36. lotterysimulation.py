import random
bet=int(input("Your bet"))
lucky_draw=random.randint(1,10)
print(lucky_draw)
account=0
if bet==lucky_draw:
    account=account+900-100
else:
    account=account-100
print(account)

    
    
