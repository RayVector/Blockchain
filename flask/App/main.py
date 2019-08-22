from flask import Flask
from flask import render_template, redirect, url_for
from flask import request
from blockchain import genesis_create, write_block, check_int


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        lender = request.form['lender']
        amount = request.form['amount']
        borrower = request.form['borrower']
        write_block(lender, amount, borrower)

        return redirect(url_for('index'))

    return render_template('index.html')


@app.route('/checking', methods=['GET'])
def check():
    results = check_int()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    genesis_create()
    app.run(debug=True)
