import telegram
from binance.client import BinanceRESTAPI, BinanceWebSocketAPI
import sqlite3
from core.db_handler import Executions,lastOrder
# api_key = 'FUB0rd7Xsw8riKvXEaRlf3REvJaLZXF8UyKWQLafu6Jp3ejaEoMF8xEMeIYhHeaj'
# secret_key = '3XIF3YBI0yzA3J4RLnbDrrqoxZjc3MnF72jex3bOPeif2dvAk1ipeZTHwFpfb1GV'

api_key = 'MjzBAT8ZTX2pYlsQn2E1QUa5pGSuL8oU9rUMDkVCDnjjN8lXg1CSyhLUPChso8WC'
secret_key = 'l89UK6PhefYRupj2if9YbqpjJCOXOOT3L2X5mzt7BS9OK4ri55rRLv642e5yZ4kP'
rest_client = BinanceRESTAPI(api_key, secret_key)
ws_client = BinanceWebSocketAPI(api_key)
trade = True
pair = 'BTCUSDT'
period='15m'
limit=100

#
# rest_client.new_order(
# symbol="ETHUSDT", side="SELL", type="LIMIT", time_in_force="GTC", quantity=0.3, price=118
# )


conn = sqlite3.connect('novatron.db')
Execution = Executions
# last_order = lastOrder(connect=conn, pair=None)
con_cur = conn.cursor()

asset = [
    ['BTCUSDT', ],
    ['ETHUSDT', ]
]


chat_id = "-282619797"
bot = telegram.Bot(token='620369180:AAF58K-FUyB1E5L-AwEdp6D7GFciRNxEYJw')


base_asset = 'BTC'
cross_asset = 'USDT'
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
min_order_val = 10
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




# '''
# (current price - purchase price) x (number of outstanding shares purchased today).
# '''
# from datetime import datetime
# import pytz
# d = ['EOSUSDT', 'ETHUSDT', 'TRXUSDT', 'BTTBTC']
#
# for pair in d:
#     wakati = str(datetime.now(pytz.timezone('Africa/Nairobi')))
#     Execution(pair = pair,  price = 20, side= 'buy', amt_base=20, amt_usd = 200, conn = conn).db_creator()
#     print(lastOrder(connect=conn.cursor(),pair=pair))
#     Execution(pair = pair,  price = 20, side= 'buy', amt_base=20, amt_usd = 200, conn = conn).execution()
#