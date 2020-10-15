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