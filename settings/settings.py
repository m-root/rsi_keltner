import telegram
from binance.client import BinanceRESTAPI, BinanceWebSocketAPI


# api_key = 'FUB0rd7Xsw8riKvXEaRlf3REvJaLZXF8UyKWQLafu6Jp3ejaEoMF8xEMeIYhHeaj'
# secret_key = '3XIF3YBI0yzA3J4RLnbDrrqoxZjc3MnF72jex3bOPeif2dvAk1ipeZTHwFpfb1GV'

#
api_key = 'kRP2gqXjlH75rUt9BG07ZlgvsQA47U3rEKPBziyjWJJBhy70SmKoQnPAoPnhfdsS'
secret_key = '3XIF3YBI0yzA3J4RLnbDrrqoxZjc3MnF72jex3bOPeif2dvAk1ipeZTHwFpfb1GV'
#

rest_client = BinanceRESTAPI(api_key, secret_key)
ws_client = BinanceWebSocketAPI(api_key)




chat_id = "-1001238068408"
bot = telegram.Bot(token='620369180:AAF58K-FUyB1E5L-AwEdp6D7GFciRNxEYJw')
# bot.send_message(
#             chat_id=self.chat_id,
#             text=telegram_message,
#             parse_mode=telegram.ParseMode.HTML
#         )



break_even_after = 35
tracker = 20
stop_loss = 35


##########################################################
#########         BUY ENTRY SETTINGS            ##########
##########################################################
buy_ema = 21
buy_entry_rsi = 50
entry_atr_period = 21



#########         BUY EXIT SETTINGS             ##########
buy_exit_cci = 50
buy_exit_momentum = -5

##########################################################
#########         SELL ENTRY SETTINGS            #########
##########################################################
sell_ema = 21
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

pairs=[
    'BTCUSDT','ETHUSDT','EOSUSDT',
    'ONTUSDT','NEOUSDT',
    'BCCUSDT','VETUSDT','ETCUSDT',
    'TRXUSDT','ADAUSDT','LTCUSDT',
    'IOTAUSDT','ICXUSDT','XLMUSDT']

period=['5m', '15m', '30m','1h' ]



limit=100