from datetime import datetime
import pytz


class Executions(object):

    def __init__(self, pair, price, side, amt_base, amt_usd, conn):
        self.pair = pair
        self.exec_time = str(datetime.now(pytz.timezone('Africa/Nairobi')))
        self.price = price
        self.side = side
        self.amt_base = amt_base
        self.amt_usd = amt_usd
        self.conn = conn
        self.c = conn.cursor()

    def db_creator(self):

        self.c.execute(
            "CREATE TABLE IF NOT EXISTS '{}' (pair TEXT, exec_time TEXT, price REAL, side TEXT, amt_base REAL, amt_usd REAL,pnl REAL)".format(
                self.pair))

    def execution(self):
        self.db_creator()
        self.c.execute(
            "INSERT INTO {} VALUES (?,?,?,?,?,?,?)".format(self.pair),
            ((self.pair, self.exec_time, self.price, self.side, self.amt_base, self.amt_usd, self.pnlcalculation())))
        self.conn.commit()

    def pnlcalculation(self):
        last_order = self.last_Order(self.pair)
        # print(last_order)
        if last_order == 0 or last_order is None:
            return 0
        else:
            # print(last_order)
            return last_order[2] - self.price

    def last_Order(self, pair):

        c = self.c
        try:
            last_Orders = []
            c.execute('SELECT * FROM {tn} '.format(tn=pair))
            data1 = c.fetchall()
            if len(data1) == 0:
                return 0
            else:
                for pending in data1:
                    last_Orders.append(list(pending))
                return last_Orders[-1]

        except Exception as e:
            print(e)


'''  
 
c.execute('SELECT * FROM {tn} WHERE {cn}="Hi World"'.\
        format(tn=table_name, cn=column_2))
all_rows = c.fetchall() 
'''

'''
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

cursor.execute("SELECT * FROM table ORDER BY id DESC LIMIT 1")
result = cursor.fetchone()

'''


def lastOrder(connect, pair):
    c = connect.cursor()
    try:
        last_Orders = []
        # connect.execute('SELECT * FROM %s'.format(pair))
        c.execute('SELECT * FROM {tn} '.format(tn=pair))
        data1 = c.fetchall()
        print(data1)
        if len(data1) == 0:
            return 0
        else:
            for pending in data1:
                last_Orders.append(list(pending))
            return last_Orders[-1]

    except Exception as e:
        print(e)


'''
# "CREATE TABLE IF NOT EXISTS '{}' (id integer primary key autoincrement, pair TEXT, exec_time TEXT, price REAL, side TEXT, amt_base REAL, amt_usd REAL, pnl REAL)".format(self.pair))
'''
