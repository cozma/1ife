from flask import Flask,render_template,request
import requests
import json

def accountTotals():
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
  
  acctTotal = []
  #doing calculations for how budget is;I figure its total amount in bank (savings+checking) then
  #subtract their recuring bills for like say rent, then also subtract a standard amount of living is
  #for one person in this case
  
  for index in accountData.json():
    if(index["nickname"] == "Denny"):
        acctTotal.append(index["nickname"])
        if(index["type"] == "checking"):
            acct1Total = acct1Total + index["balance"]
            billAcct1 = ('http://api.reimaginebanking.com/accounts/' + index["_id"] + '/bills?key=' + custKey)
            acctTotal.append(acct1Total)
        else:
            acct1Total = acct1Total + index["balance"]
            acctTotal.append(acct1Total)
  
    if(index["nickname"] == "Pedro"):
        acctTotal.append(index["nickname"])
        if(index["type"] == "checking"):
            acct2Total = acct2Total + index["balance"]
            billAcct2 = ('http://api.reimaginebanking.com/accounts/' + index["_id"] + '/bills?key=' + custKey)
            acctTotal.append(acct2Total)
        else:
            acct2Total = acct2Total + index["balance"]
            acctTotal.append(acct2Total)
  
    if(index["nickname"] == "Steven"):
        acctTotal.append(index["nickname"])
        if(index["type"] == "checking"):
            acct3Total = acct3Total + index["balance"]
            acctTotal.append(acct3Total)
            billAcct3 = ('http://api.reimaginebanking.com/accounts/' + index["_id"] + '/bills?key=' + custKey)
        else:
            acct3Total = acct3Total + index["balance"]
            acctTotal.append(acct3Total)
  
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
  
  acctTotal.append(acct1Total)
  acctTotal.append(acct2Total)
  acctTotal.append(acct3Total)
  return acctTotal
  
  #given final amounts provide reasonable grocery list/budget of each account for possible spending and saving techniques
  #say each person may have personal money for random events/food/emergency/etc
  #this is where I guess Bloombergs API comes in generates these things for each account




app_lulu = Flask(__name__)

app_lulu.vars={}

@app_lulu.route('/index',methods=['GET','POST'])
def index_lulu():
    nquestions=5
    tot=accountTotals()
    print tot
    accountTotalOne=tot[1]

    if request.method == 'GET':
      return render_template('steven.html',num=nquestions, account=accountTotalOne, Person=tot[0],Income=50,Checking=tot[1],Savings=tot[3])
    else:
        #request was a POST
        app_lulu.vars['name'] = request.form['name_lulu']
        app_lulu.vars['age'] = request.form['age_lulu']

        f = open('%s_%s.txt'%(app_lulu.vars['name'],app_lulu.vars['age']),'w')
        f.write('Name: %s\n'%(app_lulu.vars['name']))
        f.write('Age: %s\n\n'%(app_lulu.vars['age']))
        f.close()

        return render_template('layout_lulu.html',num=1,question='How many eyes do you have?',ans1='1',\
    ans2='2',ans3='3')

if __name__ == "__main__":
    app_lulu.run(debug=True)
