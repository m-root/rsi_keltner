from datetime import datetime
import pytz, time
import settings
from core import ticker
from engine import trading_logic
from payload.pl_tasks import telegram_message_relay
from core import log

####################################
#              PAYLOAD             #
####################################


settings.rest_client.place_active_order()


class Payload(object):

    def __init__(self, base_asset=None, cross_asset=None, chat_id=None, settings=None, time_frame=None):
        self.settings = settings
        self.base_asset = base_asset
        self.cross_asset = cross_asset
        self.pair = self.base_asset + self.cross_asset
        self.chat_id = chat_id
        self.time_frame = time_frame
        self.rest_client = settings.rest_client
        self.log = log
        self.log.debug_info(self.pair)

    '''

    Long Entry
    RSI 10 Oversold RSI Crossing Up Above 31 on close of candle period (ie 1 hour, 4 hour etc.)
    1. Check if there is any open trade, if any do not close 
    2. if price is below mid_KC enter in the next candle
    3. if price>mid_KC then place buy limit at mid_kc and update price 

    Cancel order 
    1. after 7 candles

    Stop Order
    stop_loss = Lowest_price in 48 candles - 15
    if stop_loss > Entry_price
    	stop_loss - 150

    Adjust_stop
    1. After profit target 2 has been hit

    Profit Targets
    Target 1
    70% If Candle Closing price Below Mid Keltner (Basis): Profit target is mid keltner line if greater than 10 point distance from entry to mid keltner (basis), If below 10 points then set take profit order at 10 pts.

    Target 2
    Profit Target 2: Recalculate P2 each new candle 20% of active order 20% Calculate Profit Target 2: (Upper Keltner - Mid Keltner Basis)/2 + Entry Price

    Target 3
    Profit Target 3: 10% of active order 10%
    When Lower Keltner line is higher than break even stop price move stop every
    period (1 hour) until stopped out. Stop can only move up not down.

    Break Even 
    ***After Profit Target 2 hit move stop price to breakeven**





    Short Entry
    RSI 10 Overbought RSI Crossing Down Below 69 on close of candle period (ie 1 hour, 4 hour etc.)
    1. Check if price is above mid keltner set entry at close price of candle.
    2. if price is below mid_KC enter in the next candle
    3. if price>mid_KC then place buy limit at mid_kc and update price 

    Cancel order 
    1. after 7 candles

    Stop Order
    stop_loss = Lowest_price in 48 candles - 15
    if stop_loss > Entry_price
    	stop_loss - 150

    Adjust_stop
    1. After profit target 2 has been hit

    Profit Targets
    Target 1
    70% If Candle Closing price Below Mid Keltner (Basis): Profit target is mid keltner line if greater than 10 point distance from 
    entry to mid keltner (basis), If below 10 points then set take profit order at 10 pts.

    Target 2
    Profit Target 2: Recalculate P2 each new candle 20% of active order 20% Calculate Profit Target 2: (Upper Keltner - Mid Keltner Basis)/2 + Entry Price

    Target 3
    Profit Target 3: 10% of active order 10%
    When Lower Keltner line is higher than break even stop price move stop every
    period (1 hour) until stopped out. Stop can only move up not down.

    Break Even 
    ***After Profit Target 2 hit move stop price to breakeven**

    '''

    def buy_logic(self):

        '''

            RSI 10 Oversold RSI Crossing Up Above 31 on close of candle period (ie 1 hour, 4 hour etc.)
            1. Check if there is any open trade, if any do not close
            2. if price is below mid_KC enter in the next candle
            3. if price>mid_KC then place buy limit at mid_kc and update price

        :return:
        '''

        if trading_logic.rsi_band(self.pair, settings.rsi_interval, self.rest_client,
                                  settings.rsi_period) > settings.buy_rsi:
            if self.settings.trade:

                balance = self.rest_client.get_wallet_fund_records()  # todo

                if balance > self.settings.min_order_val:
                    price = ticker.ticker(self.pair)[2]  # todo
                    # minPricedp = self.exchangeInfo.minPricedp() #todo
                    # minQtydp = self.exchangeInfo.minQtydp() #todo
                    quantity = self.rest_client.getCrossBalanceConv(balance=balance)  # todo
                    # price = round(price - 1 / 10 ** minPricedp, minPricedp) #todo
                    # quantity = round(quantity - 1 / 10 ** minQtydp, minQtydp) #todo

                    log.debug_info(
                        'Buy Attempt : Pair : {}, Price : {}, Quantity : {}'.format(self.pair, price,
                                                                                    quantity))

                    log.debug_info('********** MARKER 5 *****************')

                    if ticker.ticker(self.pair)[2] < trading_logic.mid_ki_band(self.pair,
                                                                               settings.mkb_interval,
                                                                               self.rest_client,
                                                                               settings.mkb_period):

                        self.trade_execution(
                            side='Buy',
                            price=ticker.ticker(self.pair)[2],
                            qty='',
                            stop_loss='',
                            take_profit='',
                        )


                    elif ticker.ticker(self.pair)[2] > trading_logic.mid_ki_band(self.pair,
                                                                                 settings.mkb_interval,
                                                                                 self.rest_client,
                                                                                 settings.mkb_period):
                        self.trade_execution(
                            side='Buy',
                            price=ticker.ticker(self.pair)[2],
                            qty='',
                            stop_loss='',
                            take_profit='',
                        )

    ####################################
    #          SELL ENTRY LOGIC        #
    ####################################
    def sell_logic(self):

        '''
        RSI 10 Overbought RSI Crossing Down Below 69 on close of candle period (ie 1 hour, 4 hour etc.)
        1. Check if price is above mid keltner set entry at close price of candle.
        2. if price is below mid_KC enter in the next candle
        3. if price>mid_KC then place buy limit at mid_kc and update price
        '''
        if trading_logic.rsi_band(self.pair, settings.rsi_interval, self.rest_client,
                                  settings.rsi_period) < settings.sell_rsi:
            if self.settings.trade:
                auth = settings.rest_client

                balance = auth.get_wallet_fund_records()  # todo

                if balance > self.settings.min_order_val:
                    price = auth.getTickerPrice()  # todo
                    # minPricedp = self.exchangeInfo.minPricedp() #todo
                    # minQtydp = self.exchangeInfo.minQtydp() #todo
                    quantity = auth.getCrossBalanceConv(balance=balance)  # todo
                    # price = round(price - 1 / 10 ** minPricedp, minPricedp) #todo
                    # quantity = round(quantity - 1 / 10 ** minQtydp, minQtydp) #todo

                    log.debug_info(
                        'Sell Attempt : Pair : {}, Price : {}, Quantity : {}'.format(self.pair, price,
                                                                                     quantity))

                    log.debug_info('********** MARKER 5 *****************')

                    if ticker.ticker(self.pair)[2] < trading_logic.mid_ki_band(self.pair,
                                                                               settings.mkb_interval,
                                                                               self.rest_client,
                                                                               settings.mkb_period):
                        self.trade_execution(
                            side='Sell',
                            price=ticker.ticker(self.pair)[2],
                            qty='',
                            stop_loss='',
                            take_profit='',
                        )


                    elif ticker.ticker(self.pair)[2] > trading_logic.mid_ki_band(self.pair,
                                                                                 settings.mkb_interval,
                                                                                 self.rest_client,
                                                                                 settings.mkb_period):
                        self.trade_execution(
                            side='Sell',
                            price=ticker.ticker(self.pair)[2],
                            qty='',
                            stop_loss='',
                            take_profit='',
                        )

    def trade_execution(self, side, price, qty, stop_loss, take_profit):
        try:
            trade_details = settings.rest_client.place_active_order(
                side=side,
                price=price,
                qty=qty,
                stop_loss=stop_loss,
                take_profit=take_profit,
                order_type='Limit'
            )

            try:
                telegram_message_relay(
                    settings=self.settings,
                    telegram_message=trade_details
                )
                try:
                    log.debug_info('Trade ID is : {}'.format(trade_details))
                except Exception as e:
                    log.debug_error('Error Exception at line 106 : {}'.format(e))
            except Exception as e:
                log.debug_error('Error Exception at line 108 : {}'.format(e))

            # log.debug_info(sett.cancelAllOrders(symbol=self.pair, orderId=trade_details['orderId']))
            time.sleep(1)

        except Exception as e:
            log.debug_error('Error Exception at line 106 : {}'.format(e))

        log.debug_info('********** MARKER 6 *****************')

        telegram_message = 'BINANCE SIGNAL : {} : {} Price : {}  Time {} Asia/Hong_Kong time ' \
            .format(
            side,
            self.pair,
            float(price),
            str(datetime.now(pytz.timezone('Asia/Hong_Kong'))

                )
        )
        log.debug_info('{}'.format(telegram_message))

        try:
            telegram_message_relay(
                settings=self.settings,
                telegram_message=telegram_message
            )
        except Exception as e:
            log.debug_error('Error Exception at line 143 : {}'.format(e))


def buyLogic(pair, tFrame, settings):
    log.debug_info('Buy test on payload : {}'.format(pair))
    trade_logic = trading_logic_trd.rate_Diff_Tradelogic(
        pair=pair[0] + pair[1],
        tFrame=tFrame,
        firstSmooth=settings.firstSmooth,
        # secondSmooth=settings.secondSmooth,
        rateSmooth=settings.rateSmooth,
        restClient=settings.rest_client
    )
    log.debug_info('trade_logic is : {} | buy is : {}'.format(trade_logic[-5:],
                                                              trade_logic[-2] > (trade_logic[-3] > trade_logic[-4] or
                                                                                 trade_logic[-2] > trade_logic[-3] <
                                                                                 trade_logic[-4])))

    if trade_logic[-2] > trade_logic[-3] > trade_logic[-4] or \
            trade_logic[-2] > trade_logic[-3] < trade_logic[-4]:

        return True
    else:
        return False


def sellLogic(pair, tFrame, settings):
    log.debug_info('Sell test on payload : {}'.format(pair))
    trade_logic = trading_logic_trd.rate_Diff_Tradelogic(
        pair=pair[0] + pair[1],
        tFrame=tFrame,
        firstSmooth=settings.firstSmooth,
        # secondSmooth=settings.secondSmooth,
        rateSmooth=settings.rateSmooth,
        restClient=settings.rest_client
    )
    log.debug_info('trade_logic is : {}  | Sell is : {}'.format(trade_logic[-5:],
                                                                trade_logic[-2] < trade_logic[-3] < trade_logic[-4] or
                                                                trade_logic[-2] < trade_logic[-3] > trade_logic[-4]))
    if trade_logic[-2] < trade_logic[-3] < trade_logic[-4] or \
            trade_logic[-2] < trade_logic[-3] > trade_logic[-4]:

        return True
    else:
        return False
