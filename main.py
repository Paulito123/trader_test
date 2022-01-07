import backtrader as bt


class MyStrategy(bt.Strategy):
    def next(self):
        pass #Do something


class PrintClose(bt.Strategy):
    def __init__(self):
        #Keep a reference to the "close" line in the data[0] dataseries
        self.dataclose = self.datas[0].close


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Instantiate Cerebro engine
    cerebro = bt.Cerebro()

    # Add strategy to Cerebro
    cerebro.addstrategy(PrintClose)

    # Run Cerebro Engine
    cerebro.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
