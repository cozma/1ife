import requests
import json
enterKey = 'ENT629977eef48af869f07841c71bfc8620'
custKey = 'CUST629977eef48af869f07841c71bfc8620'
id1 = '54b604dfa520e02948a0f508'
id2 = '54b604dfa520e02948a0f50a'
id3 = '54b604dfa520e02948a0f50b'

acct1Total = 0
acct2Total = 0
acct3Total = 0

getAccounts = ('http://api.reimaginebanking.com/accounts?key=' + custKey)

accountData = requests.get(getAccounts)
print accountData.text	
print "\n"

#doing calculations for how budget is;I figure its total amount in bank (savings+checking) then
#subtract their recuring bills for like say rent, then also subtract a standard amount of living is
#for one person in this case

for index in accountData.json():
	if(index["nickname"] == "Denny"):
		if(index["type"] == "checking"):
			acct1Total = acct1Total + index["balance"]
			billAcct1 = ('http://api.reimaginebanking.com/accounts/' + index["_id"] + '/bills?key=' + custKey)
		else:
			acct1Total = acct1Total + index["balance"]

	if(index["nickname"] == "Pedro"):
		if(index["type"] == "checking"):
			acct2Total = acct2Total + index["balance"]
			billAcct2 = ('http://api.reimaginebanking.com/accounts/' + index["_id"] + '/bills?key=' + custKey)
		else:
			acct2Total = acct2Total + index["balance"]

	if(index["nickname"] == "Steven"):
		if(index["type"] == "checking"):
			acct3Total = acct3Total + index["balance"]
			billAcct3 = ('http://api.reimaginebanking.com/accounts/' + index["_id"] + '/bills?key=' + custKey)
		else:
			acct3Total = acct3Total + index["balance"]

print acct1Total
print acct2Total
print acct3Total

moneyVal1 = requests.get(billAcct1)
moneyVal2 = requests.get(billAcct2)
moneyVal3 = requests.get(billAcct3)
#subtracting "pending" bill amounts

acct1Total = acct1Total - moneyVal1.json()[0]["payment amount"]
acct2Total = acct2Total - moneyVal2.json()[0]["payment amount"]
acct3Total = acct3Total - moneyVal3.json()[0]["payment amount"]

print "\n"
print "Remaining Amount for each account after bills"
print acct1Total 
print acct2Total
print acct3Total

#given final amounts provide reasonable grocery list/budget of each account for possible spending and saving techniques
#say each person may have personal money for random events/food/emergency/etc
#this is where I guess Bloombergs API comes in generates these things for each account



