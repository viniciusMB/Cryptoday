from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cryptoday.db'

db = SQLAlchemy(app)

class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(50), nullable=False, unique=True)

class Currency2(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol2 = db.Column(db.String(50), nullable=False, unique=True)


def get_symbol_by():
    print('Get symbol by Currency')
    currency_symbols = []
    symbols = Currency.query.all()
    for element in symbols:
        print(element.symbol)
        currency_symbols.append(element.symbol)
    return currency_symbols


def get_symbol2_by():
    print('Get symbol2 by Currency2')
    currency2_symbols = []
    symbols2 = Currency2.query.all()
    for element in symbols2:
        print(element.symbol2)
        currency2_symbols.append(element.symbol2)
    return currency2_symbols

@app.route('/')
def index():

    url = "https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}"
    currencies = get_symbol_by()
    currencies2 = get_symbol2_by()
    exchange_data = [] 

    for currency in currencies:
        for currency2 in currencies2:
            r = requests.get(url.format(currency, currency2), headers={"Apikey": "a20bdd3b9112fef067edf5b314003ec6d508867b28e3958f0ac30d34f0e6a0c8"})
            response = r.json()                  

            exchange = {
                'symbol' : currency,
                'value' : response[currency2],
                'symbol2' : currency2,
            }

            exchange_data.append(exchange)
        
    
    print(Currency.symbol)
    return render_template('index.html', currency_data = exchange_data)
if __name__ == "__main__":
    app.run(debug=True)