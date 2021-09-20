from core.db_handler import lastOrder, Executions
# from .settings import conn
from m_run.novatron.settings import conn, pairs


for pair in pairs:
    # execu = Executions(pair,  0.0, 'sell', 0.0, 4700, conn)
    # execu.execution()
    print(lastOrder(conn, pair))