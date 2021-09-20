from m_run.novatron import settings


class trails:

    def __init__(self, pair = "BTCUSD"):
        self.buy_entry = []
        self.buy_exit = []
        self.sell_entry = []
        self.sell_exit = []
        self.pair = pair

    def buy_entry_trail(self,org_pri,trail_start ):
        if org_pri - float(settings.public_auth.ticker(tpair=self.pair)['last']) > trail_start:
            trail = float(settings.public_auth.ticker(tpair=self.pair)['last']) + trail_start
            if len(self.buy_exit) == 0:
                self.buy_exit.append(trail)
            elif self.buy_exit[-1] > trail and self.buy_exit[-1] != trail:
                self.buy_exit.append(trail)
                settings.private_auth.cancel_orders(tpair=self.pair)
                # settings.private_auth.new_order(tpair=self.pair,transaction=,quantity=,price=,trade_type= )







    def buy_exit_trail(self,org_pri,trail_start ):

        if float(settings.public_auth.ticker(tpair=self.pair)['last']) - org_pri > trail_start:
            trail = float(settings.public_auth.ticker(tpair=self.pair)['last']) - trail_start
            if len(self.buy_entry) == 0:
                self.buy_entry.append(trail)
            elif self.buy_entry[-1] < trail and self.buy_entry[-1] != trail:
                self.buy_entry.append(trail)
                settings.private_auth.cancel_orders(tpair=self.pair)
                # settings.private_auth.new_order(tpair=,transaction=,quantity=,price=,trade_type= )



    def sell_entry_trail(self, org_pri,trail_start):
        if float(settings.public_auth.ticker(tpair=self.pair)['last']) - org_pri > trail_start:
            trail = float(settings.public_auth.ticker(tpair=self.pair)['last']) - trail_start
            if len(self.sell_entry) == 0:
                self.sell_entry.append(trail)
            elif self.sell_entry[-1] < trail and self.sell_entry[-1] != trail:
                self.sell_entry.append(trail)
                settings.private_auth.cancel_orders(tpair=self.pair)
                # settings.private_auth.new_order(tpair=,transaction=,quantity=,price=,trade_type= )




    def sell_exit_trail(self, org_pri,trail_start):
        if org_pri - float(settings.public_auth.ticker(tpair=self.pair)['last']) > trail_start:
            trail = float(settings.public_auth.ticker(tpair=self.pair)['last']) + trail_start
            if len(self.sell_exit) == 0:
                self.sell_exit.append(trail)
            elif self.sell_exit[-1] > trail and self.sell_exit[-1] != trail:
                self.sell_exit.append(trail)
                settings.private_auth.cancel_orders(tpair=self.pair)
                # settings.private_auth.new_order(tpair=,transaction=,quantity=,price=,trade_type= )




trial = trails()
org_pri = float(settings.public_auth.ticker(tpair=trial.pair)['last'])
trail_start = 2

while True:
    print(trial.buy_entry_trail(org_pri,trail_start))
    print(trial.buy_exit_trail(org_pri,trail_start))
    print(trial.sell_entry_trail(org_pri,trail_start))
    print(trial.sell_exit_trail(org_pri,trail_start))

    import time
    time.sleep(2)