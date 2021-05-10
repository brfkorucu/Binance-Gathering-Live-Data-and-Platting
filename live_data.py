from binance.client import Client
from binance.websockets import BinanceSocketManager
from binance.enums import *
from datetime import datetime
from csv import writer
import pprint
from itertools import count

client = Client() ####    


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, "a+", newline="") as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


closes_btc = []
closes_eth = []
closes_doge = []


def process_message(msg):
    # print("received message")
    # pprint.pprint(msg)

    ticker = msg["s"]
    candle = msg["k"]
    is_candle_closed = candle["x"]
    open_p = candle["o"]
    close_p = candle["c"]
    high_p = candle["h"]
    low_p = candle["l"]
    volume = candle["v"]
    q_volume = candle["q"]
    time = candle["T"]
    date_time = datetime.fromtimestamp(int(time) / 1000)

    if ticker == "BTCTRY":
        if is_candle_closed:
            # print("Candle close at {}".format(close))
            append_list_as_row(
                r"C:\Users\HOPE\Desktop\TradingBot\btc.csv",
                [
                    # float(open_p),
                    # float(high_p),
                    # float(low_p),
                    float(close_p),
                    # float(volume),
                    # float(q_volume),
                    # date_time,
                ],
            )
            # print("writed btc")
            # print("Data for 1MİN-K BTC : ", closes_btc)

    if ticker == "ETHTRY":
        if is_candle_closed:
            # print("Candle close at {}".format(close))
            append_list_as_row(
                r"C:\Users\HOPE\Desktop\TradingBot\eth.csv",
                [
                    # float(open_p),
                    # float(high_p),
                    # float(low_p),
                    float(close_p),
                    # float(volume),
                    # float(q_volume),
                    # date_time,
                ],
            )
            # print("writed eth")
            # print("Data for 1MİN-K ETH: ", closes_eth)

    if ticker == "DOGETRY":
        if is_candle_closed:
            # print("Candle close at {}".format(close))
            append_list_as_row(
                r"C:\Users\HOPE\Desktop\TradingBot\doge.csv",
                [
                    # float(open_p),
                    # float(high_p),
                    # float(low_p),
                    float(close_p),
                    # float(volume),
                    # float(q_volume),
                    # date_time,
                ],
            )
            # print("writed doge")
            # print("Data for 1MİN-K DOGE : ", closes_doge)

    print("Processing...", end="\r")


bm = BinanceSocketManager(client, user_timeout=60)
# start any sockets here, i.e a trade socket
conn_key_btc = bm.start_kline_socket(
    "BTCTRY", process_message, interval=KLINE_INTERVAL_1MINUTE
)
conn_key_eth = bm.start_kline_socket(
    "ETHTRY", process_message, interval=KLINE_INTERVAL_1MINUTE
)
conn_key_eth = bm.start_kline_socket(
    "DOGETRY", process_message, interval=KLINE_INTERVAL_1MINUTE
)
# then start the socket manager
bm.start()