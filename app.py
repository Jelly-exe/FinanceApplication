from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


# from dotenv import dotenv_values

# config = dotenv_values(".env")

@app.route('/')
def index():
    return redirect(url_for('overview'))


@app.route('/overview')
def overview(balance=200, sfe_amount=9000):  # put application's code here
    return render_template('overview.html', balance=balance, sfe_amount=sfe_amount)


if __name__ == '__main__':
    app.run()
