import requests
from flask import Flask, url_for, request, render_template, send_file
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('homepage.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/user/<username>')
def profile(username): pass

@app.route('/payment')
def payment():
    return render_template('payment.html')

@app.route('/accounts/<id>')
def accounts():
    return 'See Accounts Here'

@app.route('/pokemon')
def pokemon():
    return 'See Pokemon Here'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run()