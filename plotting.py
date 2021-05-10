import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate(i):
    data_btc = pd.read_csv(r"C:\Users\HOPE\Desktop\TradingBot\btc.csv")
    btc = data_btc["close_p"]
    # data_eth = pd.read_csv(r"C:\Users\HOPE\Desktop\TradingBot\eth.csv")
    # eth = data_eth["close_p"]
    # data_doge = pd.read_csv(r"C:\Users\HOPE\Desktop\TradingBot\doge.csv")
    # doge = data_doge["close_p"]

    plt.cla()
    plt.plot(btc, label="BTC Close Prices")
    # plt.plot(eth, label="ETH Close Prices")
    # plt.plot(doge, label="DOGE Close Prices")

    plt.legend(loc="upper left")
    plt.tight_layout()
    print("Processing...", end="\r")


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.style.use("ggplot")
plt.grid(True)
plt.tight_layout()
plt.show()
