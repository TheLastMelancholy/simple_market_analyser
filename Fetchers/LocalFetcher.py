from IFetcher import IFetcher
from csv import reader

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
           linesProcessor = reader(csvfile)
           for line in linesProcessor:
               # TODO - Decide on how to deduce
               # fields meaning
               # config, convection or
               # belief in headers consistency
               # FOR NOW - use yfinance schema
               yield line
