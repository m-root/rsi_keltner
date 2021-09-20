import time
from m_run.crypto_signals.m_core import logic
from datetime import datetime
from m_run.crypto_signals.settings import pairs

def main():


    while True:

        for pair in pairs:
            try:
                logic.delay(pair)
                time.sleep(1)

            except Exception as e:
                print(e)
                time.sleep(15)

            while float(datetime.utcnow().strftime("%M.%S")) % 15 != 0:
                time.sleep(1)


# if __name__ == '__main__':
#     main()


main()