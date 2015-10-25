import requests
from flask import Flask, url_for, request, render_template, send_file
app = Flask(__name__)

api_key = 'e7bff3ff405d7b4e32cc80be8a8f1d37'

@app.route('/')
def home():
	return render_template('homepage.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/bill')
def bill():
    return render_template('bill.html')

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

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/purchase')
def purchase():
    return render_template('purchase.html')

@app.route('/withdrawl')
def withdrawl():
    return render_template('withdrawl.html')

@app.route('/pokemon')
def pokemon():
    return 'See Pokemon Here'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()