import requests
import json
enterKey = 'ENT629977eef48af869f07841c71bfc8620'
custKey = 'CUST629977eef48af869f07841c71bfc8620'
id1 = '54b604dfa520e02948a0f508'
id2 = '54b604dfa520e02948a0f50a'
id3 = '54b604dfa520e02948a0f50b'


billId1 = { "recurring": True, "status": "pending", "payment date": "1/1/15","upcoming payment date": "3/1/15", "payment amount": 150}
billId2 = { "recurring": True, "status": "pending", "payment date": "1/1/15","upcoming payment date": "3/1/15", "payment amount": 70}
billId3 = { "recurring": True, "status": "pending", "payment date": "1/1/15","upcoming payment date": "3/1/15", "payment amount": 50}

reqString = ('http://api.reimaginebanking.com/accounts?key=' + custKey)


#make a bill for every customer id's checking account only for ease
#iterate through all the accounts
for index in req.json():
	if(index["nickname"] == "Denny"):
		if(index["type"] == "checking"):
			addBillString = ('http://api.reimaginebanking.com/accounts/' + index["_id"] + '/bills?key=' + custKey)
			billAddition = requests.post(addBillString, headers={"content-type":"application/json"}, data=json.dumps(billId1))
			bill = requests.get(addBillString)
			print bill.text
	if(index["nickname"] == "Pedro"):
		if(index["type"] == "checking"):
			addBillString = ('http://api.reimaginebanking.com/accounts/' + index["_id"] + '/bills?key=' + custKey)
			billAddition = requests.post(addBillString, headers={"content-type":"application/json"}, data=json.dumps(billId2))
			bill = requests.get(addBillString)
			print bill.text
	if(index["nickname"] == "Steven"):
		if(index["type"] == "checking"):
			addBillString = ('http://api.reimaginebanking.com/accounts/' + index["_id"] + '/bills?key=' + custKey)
			billAddition = requests.post(addBillString, headers={"content-type":"application/json"}, data=json.dumps(billId3))
			bill = requests.get(addBillString)
			print bill.text








#print req.status_cod