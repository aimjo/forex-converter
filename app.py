from flask import Flask, render_template, request, flash, redirect
from flask_debugtoolbar import DebugToolbarExtension
from utility import is_valid_currency, convert_currency, get_currency_symbol

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretsecret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/', methods=['GET', 'POST'])


def currency_converter():
    if request.method == 'POST':
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

        if not is_valid_currency(from_currency) or not is_valid_currency(to_currency):
            flash('Invalid currency code')
            return render_template('currency_converter.html')
        
        try:
            amount = float(amount)
        except ValueError:
            flash('Invalid amount')
            return render_template('currency_converter.html')

        converted_amount = convert_currency(amount, from_currency, to_currency)
        if converted_amount is not None:
            currency_symbol = get_currency_symbol(to_currency)
            if currency_symbol:
                formatted_amount = f"{currency_symbol} {converted_amount:.2f}"  # Format to two decimal places
                
            flash(f'Converted amount: {formatted_amount}')
        else:
            flash('Currency conversion failed')

    return render_template('currency_converter.html')