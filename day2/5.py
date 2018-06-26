global coins;
def combo(amount,currentcoin):
	if(amount ==0):
		return 1;
	if(amount < 0):
		return 0;
	ncombos =0;
	for coin in range(currentcoin,len(coins),1):
		ncombos+=combo(amount-coins[coin],coin)


	return ncombos;

coins=[int(x) for x in input().split(",")]
amount=int(input("enter the amount "))
print(combo(amount,0))