from pyti import relative_strength_index as rsi, keltner_bands as ki
from core.candle import candles
from core import ticker
import settings

def rsi_band(pair, interval, rest_client, period):
    data = candles(symbol=pair, interval=interval, rest_client=rest_client)
    return rsi.relative_strength_index(data=data[3], period=period)


def upper_ki_band(pair, interval, rest_client, period):
    data = candles(symbol=pair, interval=interval, rest_client=rest_client)
    return ki.upper_band(close_data=data[3], high_data=data[1], low_data=data[2], period=period)


def mid_ki_band(pair, interval, rest_client, period):
    data = candles(symbol=pair, interval=interval, rest_client=rest_client)
    return ki.center_band(close_data=data[3], high_data=data[1], low_data=data[2], period=period)


def lower_ki_band(pair, interval, rest_client, period):
    data = candles(symbol=pair, interval=interval, rest_client=rest_client)
    return ki.lower_band(close_data=data[3], high_data=data[1], low_data=data[2], period=period)


def buy_stop_loss(pair, interval, rest_client):
    data = candles(symbol=pair, interval=interval, rest_client=rest_client)
    stop_loss = data[2][-40:]
    entry_price = ticker.ticker(pair)[-1]

    if entry_price < float(min(stop_loss)):
        return float(min(stop_loss)) - 15
    else:
        return entry_price - 150









###################################### LONG #########################################################


'''RSI 10 Overbought RSI Crossing Down Below 69 on close of candle period (ie 1 hour, 4 hour etc.)'''


def longEntry(entry_order_amount, entry_order_amount_init, entryOrderSpread):
    if rsi_band(pair=, interval=, rest_client=, period=) < cross_level:

        '''Price above mid keltner(basis). Entry Condition: If price is above mid keltner set entry at close price of candle'''
        if ticker.ticker(pair)[-1] > mid_ki_band():
            '''
            If parameter equals 1 then one entry order is placed. If Entry order amount is
            greater than 1 then multiple equal sized limit orders placed according to the Entry
            order Spread Parameter. Example: If Entry Order Amount is 3 and Entry Order
            Spread is .5 then If Short Entry Price is 3800 then first order is 3800, second order
            is 3800.5, third 3801 and so on.
            '''
            if entry_order_amount <= 1:
                settings.rest_client.place_active_order()  # todo close price of candle

            elif entry_order_amount >= 1:
                for

        '''
        Price below mid keltner(basis). Entry Condition: If price is below mid keltner(basis) then set sell limit order at mid 
        kelter. Each new candle at end of period (ie hour) update order to new mid kelter(basis) price until filled.
        '''
        if ticker.ticker(pair)[-1] < mid_ki_band():
            '''
            If parameter equals 1 then one entry order is placed. If Entry order amount is
            greater than 1 then multiple equal sized limit orders placed according to the Entry
            order Spread Parameter. Example: If Entry Order Amount is 3 and Entry Order
            Spread is .5 then If Short Entry Price is 3800 then first order is 3800, second order
            is 3800.5, third 3801 and so on.
            '''
            entry_price = mid_ki_band()
            if entry_order_amount <= 1:
                while entry_order_amount_init < entry_order_amount:
                    settings.rest_client.place_active_order(price=entry_price)  # todo  sell limit order at mid kelter
                    entry_price = entry_price + entryOrderSpread
                    entry_order_amount = entry_order_amount + 1


'''If order does not fill for 7 bars after entry signal then cancel order.'''


def cancelLongEntry():
    for order in settings.rest_client.get_active_order(price=entry_price):  # todo  sell limit order at mid kelter
        if order:  # ToDo if order time is past 7 bars after entry signal then cancel order
            pass


def longStopLoss(pair, interval, rest_client):
    data = candles(symbol=pair, interval=interval, rest_client=rest_client)
    stop_loss = data[1][-40:]
    entry_price = ticker.ticker(pair)[-1]

    if entry_price > float(max(stop_loss)):
        return float(max(stop_loss)) + 15
    else:
        return entry_price + 150


def longExitFirstLogic(pair, interval, rest_client, side, period):
    entry_price = ticker.ticker(pair)
    mid_kb = mid_ki_band(pair=pair, interval=interval, rest_client=rest_client, period=period)
    diff = 10
    first_offset = 0.7
    trade_qty = settings.rest_client.get_active_order()
    '''
    70%
    If Candle Closing price Above Mid Keltner (Basis): Profit target is mid keltner line if
    greater than 10 point distance from entry to mid keltner (basis), If below 10 points
    then set take profit order at 10 pts.
    '''
    if mid_ki_band(pair=pair, interval=interval, rest_client=rest_client, period=period) < ticker.ticker(pair)[
        -1] and mid_kb - entry_price >= diff:

        settings.rest_client.market_close(side=side, qty=trade_qty * first_offset,
                                          price=)  # price should be at mid_K price

    elif mid_ki_band(pair=pair, interval=interval, rest_client=rest_client, period=period) < ticker.ticker(pair)[
        -1] and entry_price - mid_kb <= diff:
        settings.rest_client.market_close(side=side, qty=trade_qty * first_offset,
                                          price=)  # price should be at entry_price + 10


def longExitSecondLogic(pair, interval, rest_client, side, period):
    entry_price = ticker.ticker(pair)
    mid_kb = mid_ki_band(pair=pair, interval=interval, rest_client=rest_client, period=period)
    diff = 10
    first_offset = 0.7
    trade_qty = settings.rest_client.get_active_order()
    balance =  # todo balance of the remaining coinstock
    '''
    Profit Target 2: Recalculate P2 each new candle 20% of active order 20% Calculate Profit Target 2: Entry Price - (Mid Keltner Basis - Lower Keltner)/2

    '''
    if (entry_price - (mid_ki_band() - lower_ki_band()) / 2) > candles()[-2]:
        settings.rest_client.market_close(side=side, qty=2 / 3 * balance,
                                          price=)  # todo price should be at mid_K price and the


def longExitThirdLogic(pair, interval, rest_client, side, period):
    entry_price = ticker.ticker(pair)
    mid_kb = mid_ki_band(pair=pair, interval=interval, rest_client=rest_client, period=period)
    diff = 10
    first_offset = 0.7
    trade_qty = settings.rest_client.get_active_order()
    '''
    Profit Target 3: 10% of active order 10%
    When Upper Keltner line is lower than break even stop price move stop every
    period (1 hour) until stopped out. Stop can only move down not up during short.
    '''
    if upper_ki_band() > entry_price:
        settings.rest_client.market_close(side=side, qty=2 / 3 * balance,
                                          price=)  # todo Edit stopLoss












###################################### SHORT #########################################################




'''RSI 10 Overbought RSI Crossing Down Below 69 on close of candle period (ie 1 hour, 4 hour etc.)'''
def short_entry(entry_order_amount, entry_order_amount_init, entryOrderSpread):
    if rsi_band(pair=,interval=,rest_client=,period=) < cross_level:

        '''Price above mid keltner(basis). Entry Condition: If price is above mid keltner set entry at close price of candle'''
        if ticker.ticker(pair)[-1] > mid_ki_band():
            '''
            If parameter equals 1 then one entry order is placed. If Entry order amount is
            greater than 1 then multiple equal sized limit orders placed according to the Entry
            order Spread Parameter. Example: If Entry Order Amount is 3 and Entry Order
            Spread is .5 then If Short Entry Price is 3800 then first order is 3800, second order
            is 3800.5, third 3801 and so on.
            '''
            if entry_order_amount <= 1:
                settings.rest_client.place_active_order() #todo close price of candle

            elif entry_order_amount >= 1:
                for

        '''
        Price below mid keltner(basis). Entry Condition: If price is below mid keltner(basis) then set sell limit order at mid 
        kelter. Each new candle at end of period (ie hour) update order to new mid kelter(basis) price until filled.
        '''
        if ticker.ticker(pair)[-1] < mid_ki_band():
            '''
            If parameter equals 1 then one entry order is placed. If Entry order amount is
            greater than 1 then multiple equal sized limit orders placed according to the Entry
            order Spread Parameter. Example: If Entry Order Amount is 3 and Entry Order
            Spread is .5 then If Short Entry Price is 3800 then first order is 3800, second order
            is 3800.5, third 3801 and so on.
            '''
            entry_price = mid_ki_band()
            if entry_order_amount <= 1:
                while entry_order_amount_init < entry_order_amount:
                    settings.rest_client.place_active_order(price=entry_price) #todo  sell limit order at mid kelter
                    entry_price = entry_price + entryOrderSpread
                    entry_order_amount = entry_order_amount + 1


'''If order does not fill for 7 bars after entry signal then cancel order.'''
def cancelShortEntry():
    for order in settings.rest_client.get_active_order(price=entry_price):  # todo  sell limit order at mid kelter
        if order: #ToDo if order time is past 7 bars after entry signal then cancel order
            pass


def sell_stop_loss(pair, interval, rest_client):
    data = candles(symbol=pair, interval=interval, rest_client=rest_client)
    stop_loss = data[1][-40:]
    entry_price = ticker.ticker(pair)[-1]

    if entry_price > float(max(stop_loss)):
        return float(max(stop_loss)) + 15
    else:
        return entry_price + 150


def sellFirstLogic(pair,interval,rest_client,side, period):
    entry_price = ticker.ticker(pair)
    mid_kb = mid_ki_band(pair=pair, interval=interval, rest_client=rest_client, period=period)
    diff = 10
    first_offset = 0.7
    trade_qty = settings.rest_client.get_active_order()
    '''
    70%
    If Candle Closing price Above Mid Keltner (Basis): Profit target is mid keltner line if
    greater than 10 point distance from entry to mid keltner (basis), If below 10 points
    then set take profit order at 10 pts.
    '''
    if mid_ki_band(pair=pair, interval=interval,rest_client=rest_client, period=period ) < ticker.ticker(pair)[-1]  and mid_kb - entry_price >= diff:

        settings.rest_client.market_close(side=side, qty=trade_qty*first_offset, price=  ) #price should be at mid_K price

    elif mid_ki_band(pair=pair, interval=interval, rest_client=rest_client, period=period) < ticker.ticker(pair)[
            -1] and entry_price - mid_kb  <= diff:
            settings.rest_client.market_close(side=side, qty=trade_qty * first_offset, price=) #price should be at entry_price + 10


def sellSecondLogic(pair, interval, rest_client, side, period):
    entry_price = ticker.ticker(pair)
    mid_kb = mid_ki_band(pair=pair, interval=interval, rest_client=rest_client, period=period)
    diff = 10
    first_offset = 0.7
    trade_qty = settings.rest_client.get_active_order()
    balance = #todo balance of the remaining coinstock
    '''
    Profit Target 2: Recalculate P2 each new candle 20% of active order 20% Calculate Profit Target 2: Entry Price - (Mid Keltner Basis - Lower Keltner)/2
    
    '''
    if (entry_price - (mid_ki_band() - lower_ki_band()) / 2) > candles()[-2]:
        settings.rest_client.market_close(side=side, qty=2/3 * balance,
                                          price=)  #todo price should be at mid_K price and the

def sellThirdLogic(pair, interval, rest_client, side, period):
    entry_price = ticker.ticker(pair)
    mid_kb = mid_ki_band(pair=pair, interval=interval, rest_client=rest_client, period=period)
    diff = 10
    first_offset = 0.7
    trade_qty = settings.rest_client.get_active_order()
    '''
    Profit Target 3: 10% of active order 10%
    When Upper Keltner line is lower than break even stop price move stop every
    period (1 hour) until stopped out. Stop can only move down not up during short.
    '''
    if upper_ki_band() > entry_price :
        settings.rest_client.market_close(side=side, qty=2 / 3 * balance,
                                          price=)  # todo Edit stopLoss
















