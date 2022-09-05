# CHECK LINE 3 or NP5-ReadMe >>> for introduction of app

# Warning !!!
# REQUESTS LIBRARY MUST EXIST IN YOUR SYSTEM
# IF YOU DON'T HAVE IT, RUN THIS CODE :
# terminal@user     >>> python -m pip install requests
# cmd/folder        >>> python -m pip install requests
# powershell/folder >>> python -m pip install requests

# when you run app
# a window will open
# there are 3 columns
# left column is for name of monies
# middle column is for symbol of monies
# right column is for price of monies
# you don't need to do extra work
# you just need to run app to see price of monies

import requests
from tkinter import *

# printing version of app
print('NP5-ExchangeRateInToman V1.0 running...')


def formatter(price):
    price = str(price)
    price_list = []
    price_list.extend(price)
    price_list = price_list[::-1]
    counter = 0
    # bitcoin is very expensive (len > 5 in toman)
    # if len(price_list) > 3:
    #     price_list.insert(3, ',')
    for i in range(len(price_list)):
        # in debug mode I traced this for loop
        # for i == 0 bug founded so I added (i != 0) in if
        if i % 3 == 0 and i != 0:
            counter += 1
    for i in range(counter, 0, -1):
        i *= 3
        price_list.insert(i, ',')
    price_list = price_list[::-1]
    price = ''.join(price_list)
    price = price + ' Tomans'
    return price


respond = requests.get('http://api.navasan.tech/latest/?api_key=freelYB5CPuyt4j1pYffFCAyJudkVvbs')
data = respond.json()

nima_font = 'aria 16'

pad_x, pad_y = 20, 5
window = Tk()
window.title('Exchange Rate In Toman')

# title labels
label_money_title = Label(window, text='Monies Info', font=f'{nima_font} bold')
label_symbol_title = Label(window, text='Symbol', font=f'{nima_font} bold')
label_price_title = Label(window, text='Price in Toman', font=f'{nima_font} bold')
label_money_title.grid(row=0, column=0, sticky=W)
label_symbol_title.grid(row=0, column=1, padx=pad_x, pady=pad_y)
label_price_title.grid(row=0, column=2, sticky=W)
# usd
label_usd = Label(window, text='United States Dollar', font=f'{nima_font}')
label_usd_symbol = Label(window, text='( USD )', font=f'{nima_font} italic')
entry_usd = Entry(window, font=f'{nima_font}', fg='blue')
label_usd.grid(row=1, column=0, sticky=W)
label_usd_symbol.grid(row=1, column=1, pady=pad_y)
entry_usd.grid(row=1, column=2, sticky=W)
entry_usd.insert(END, formatter(data['usd']['value']))
# cad
label_cad = Label(window, text='Canadian Dollar', font=f'{nima_font}')
label_cad_symbol = Label(window, text='( CAD )', font=f'{nima_font} italic')
entry_cad = Entry(window, font=f'{nima_font}', fg='blue')
label_cad.grid(row=2, column=0, sticky=W)
label_cad_symbol.grid(row=2, column=1, pady=pad_y)
entry_cad.grid(row=2, column=2, sticky=W)
entry_cad.insert(END, formatter(data['cad']['value']))
# eur
label_eur = Label(window, text='Euro', font=f'{nima_font}')
label_eur_symbol = Label(window, text='( EUR )', font=f'{nima_font} italic')
entry_eur = Entry(window, font=f'{nima_font}', fg='blue')
label_eur.grid(row=3, column=0, sticky=W)
label_eur_symbol.grid(row=3, column=1, pady=pad_y)
entry_eur.grid(row=3, column=2, sticky=W)
entry_eur.insert(END, formatter(data['eur']['value']))
# gbp
label_gbp = Label(window, text='Pound Sterling', font=f'{nima_font}')
label_gbp_symbol = Label(window, text='( GBP )', font=f'{nima_font} italic')
entry_gbp = Entry(window, font=f'{nima_font}', fg='blue')
label_gbp.grid(row=4, column=0, sticky=W)
label_gbp_symbol.grid(row=4, column=1, pady=pad_y)
entry_gbp.grid(row=4, column=2, sticky=W)
entry_gbp.insert(END, formatter(data['gbp']['value']))
# btc
label_btc = Label(window, text='Bitcoin', font=f'{nima_font}')
label_btc_symbol = Label(window, text='( BTC )', font=f'{nima_font} italic')
entry_btc = Entry(window, font=f'{nima_font}', fg='blue')
label_btc.grid(row=5, column=0, sticky=W)
label_btc_symbol.grid(row=5, column=1, pady=pad_y)
entry_btc.grid(row=5, column=2, sticky=W)
entry_btc.insert(END, formatter(data['btc']['value']))
# eth
label_eth = Label(window, text='Ethereum', font=f'{nima_font}')
label_eth_symbol = Label(window, text='( ETC )', font=f'{nima_font} italic')
entry_eth = Entry(window, font=f'{nima_font}', fg='blue')
label_eth.grid(row=6, column=0, sticky=W)
label_eth_symbol.grid(row=6, column=1, pady=pad_y)
entry_eth.grid(row=6, column=2, sticky=W)
entry_eth.insert(END, formatter(data['eth']['value']))
# usdt
label_usdt = Label(window, text='Tether', font=f'{nima_font}')
label_usdt_symbol = Label(window, text='( USDT )', font=f'{nima_font} italic')
entry_usdt = Entry(window, font=f'{nima_font}', fg='blue')
label_usdt.grid(row=7, column=0, sticky=W)
label_usdt_symbol.grid(row=7, column=1, pady=pad_y)
entry_usdt.grid(row=7, column=2, sticky=W)
entry_usdt.insert(END, formatter(data['usdt']['value']))
# bnb
label_bnb = Label(window, text='Binance Coin', font=f'{nima_font}')
label_bnb_symbol = Label(window, text='( BNB )', font=f'{nima_font} italic')
entry_bnb = Entry(window, font=f'{nima_font}', fg='blue')
label_bnb.grid(row=8, column=0, sticky=W)
label_bnb_symbol.grid(row=8, column=1, pady=pad_y)
entry_bnb.grid(row=8, column=2, sticky=W)
entry_bnb.insert(END, formatter(data['bnb']['value']))

window.mainloop()
