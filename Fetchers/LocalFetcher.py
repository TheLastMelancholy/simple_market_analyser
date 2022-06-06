from Fetchers.IFetcher import IFetcher
from csv import DictReader
from Fetchers.DataModel import Bar

class LocalFetcher(IFetcher):
    def __init__(self, dataSheetPath):
        super().__init__(dataSheetPath)
        self.dataReader = None
        self.processConfig()

    def processConfig(self):
        self.dataReader = self.dataGenerator()
        next(self.dataReader)

    def dataGenerator(self):
        with open(self.configPath) as csvfile:
           # TODO - exceptions processing or
           # data pre-validation

           linesProcessor = DictReader(csvfile)#, fields=["Date",
                                                #         "Open",
                                                 #        "High",
                                                  #        "Low",
                                                   #       "Close",
                                                    #      "Adj Close",
                                                     #     "Volume"])
           for line in linesProcessor:
               # TODO - Decide on how to deduce
               # fields meaning
               # config, convection or
               # belief in headers consistency
               # FOR NOW - use yfinance schema

               priceBar = Bar()
               priceBar.O = line["Open"]
               priceBar.C = line["Close"]
               priceBar.H = line["High"]
               priceBar.L = line["Low"]
               priceBar.Volume = line["Volume"]

               yield priceBar
