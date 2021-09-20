import telegram
from binance.client import Client


from celery import Celery
# app = Celery('tasks', broker='amqp://')
app = Celery('tasks', backend='amqp', broker='amqp://')

'''
API Key:
3mKx3sYqRQiQYkyk1dFBoAPA3eTheusjcc6MltQZUomCDOyUhWRtsqWBSe1IYYza
Secret Key:  
uTCZwTldXb69MeSuH2uGFfCKQnnsscPn1yPxzBkJsrqLaIKaQ9RUVKpnKfo1r8vh
'''

api_key = '5VZvJtVXldnFwgpnYvNxPShSHJdGY4089ShThzLCi8IsGkPckmhTBFLJTwDSucKW'
secret_key = 'YPqJXjRp7ynsBiYIcYD6cTSInZp58Pn5XcZjeFzDuDSDDHFkTpJMRQfCg73w3VPX'
requests_params=None
rest_client = Client(api_key, secret_key, requests_params)
print(rest_client.get_asset_balance(asset='USDT'))
print(rest_client.get_asset_balance(asset='BTC'))
trade = True
period='15m'
limit=100
eq_pc = 50
min_order_val = 10
tFrame = ['15m','30m']
firstSmooth = 178
rateSmooth = 5
chat_id = "-282619797"
bot = telegram.Bot(token='620369180:AAF58K-FUyB1E5L-AwEdp6D7GFciRNxEYJw')
break_even_after = 35
tracker = 20
stop_loss = 35


##########################################################
#########         BUY ENTRY SETTINGS            ##########
##########################################################
macd_short_period = 50
buy_entry_rsi = 50
entry_atr_period = 21


##########################################################
#########                HA SETTINGS            ##########
##########################################################
low_time_frame='15m'
higher_time_frame='2h'
slow_ma=30
fast_ma= 1

sleep_time = 2

##########################################################
#########              MACD SETTINGS            ##########
##########################################################
macd_short_period = 10
macd_long_period = 21
macd_signal_length = 69


#########         BUY EXIT SETTINGS             ##########
buy_exit_cci = 50
buy_exit_momentum = -5

##########################################################
#########         SELL ENTRY SETTINGS            #########
##########################################################
sell_ema = 50
sell_entry_rsi = 50
sell_entry_atr = 40


#########         SELL EXIT SETTINGS            ##########



#########         BUY KEY LEVELS             ##########
cci_kl_ema = 14


#########         SELL KEY LEVELS             ##########

cci_period = 14
ema_period = 50
rsi_period = 14
ndi_period = 14
pdi_period = 14
moment_period = 14
atr_period = 21
atrp_period =14


