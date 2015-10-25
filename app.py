import requests, json
from flask import Flask, url_for, request, render_template, send_file
app = Flask(__name__)

api_key = 'e7bff3ff405d7b4e32cc80be8a8f1d37'

@app.route('/')
def home():
	return render_template('homepage.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/bill', methods=['GET', 'POST', 'PUT', 'DELETE'])
def bill():
    if request.method == 'DELETE':
        bill_id = request.form['bill_id']
        r = requests.delete("http://api.reimaginebanking.com/accounts/delete", data = {'billId' : bill_id})
        r = r.json()
        print(r.text)
        return redirect('/')
    elif request.method == 'PUT':
        bill_id = request.form['bill_id']
        payee = request.form['payee']
        nickname = request.form['nickname']
        payment_date = request.form['payment_date']
        reocurring = request.form['reocurring']
        amount = request.form['amount']
        r = requests.put("http://api.reimaginebanking.com/accounts/put", data = {"status": "pending", "payee": payee, "nickname": nickname, "payment_date": "2015-10-25", "recurring_date": reocurring, "payment_amount": amount })
        r = r.json()
        return redirect('/')
    elif request.method == 'POST':
        bill_id = request.form['bill_id']
        payee = request.form['payee']
        nickname = request.form['nickname']
        payment_date = request.form['payment_date']
        reocurring = request.form['reocurring']
        amount = request.form['amount']
        r = requests.post("http://api.reimaginebanking.com/accounts/post", data = {"billId": bill_id, "status": "pending", "payee": payee, "nickname": nickname, "payment_date": "2015-10-25", "recurring_date": reocurring, "payment_amount": amount })
        r = r.json()
        return redirect('/')
    elif request.method == 'GET':
        account_id = request.form['account_id']
        bill_id = request.form['bill_id']
        customer_id = request.form['customer_id']
        get_id = 0
        id_name = "id"
        if account_id:
            get_id = account_id
        elif bill_id:
            id_name = "billId"
            get_id = bill_id
        elif customer_id:
            get_id = customer_id
        r = requests.get("http://api.reimaginebanking.com/accounts/get", data = {id_name : get_id})
        return redirect('/')
    print("damn it.")

@app.route('/branch')
def branch():
    return render_template('branch.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/deposit')
def deposit():
    return render_template('deposit.html')

@app.route('/merchant')
def merchant():
    return render_template('merchant.html')

@app.route('/purchase')
def purchase():
    return render_template('purchase.html')

@app.route('/withdrawal')
def withdrawal():
    return render_template('withdrawal.html')

@app.route('/pokemon')
def pokemon():
    return 'See Pokemon Here'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()