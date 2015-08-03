import requests
import json
enterKey = 'ENT629977eef48af869f07841c71bfc8620'
custKey = 'CUST629977eef48af869f07841c71bfc8620'
id1 = '54b604dfa520e02948a0f508'
id2 = '54b604dfa520e02948a0f50a'
id3 = '54b604dfa520e02948a0f50b'


body = {"type": "checking", "nickname": "Pedro", "rewards": 10, "balance": 20}

reqString = ('http://api.reimaginebanking.com/accounts?key=' + custKey)


#req = requests.post(reqString, headers={"content-type":"application/json"}, data=json.dumps(body))
req = requests.get(reqString)
print req.text

#name = req.json()[0]["nickname"]
#if name == "fjjfjf":
#	print "ok"
	





#print req.status_cod

