import matplotlib.pyplot as plt

DATE = 0
OPEN = 1
CLOSE = 2
HIGH = 3
LOW = 4
VOLUME = 5

class Processor():
    def __init__(self, dochlv, targetH = 720, targetW = 1080):
        self.dochlv = dochlv

    def extractFeature(self, featureNo):
        return [_[featureNo] for _ in sefl.dochlv]

    def extractDate(self):
        return self.extractFeature[DATE]

    def extractClose(self):
        return self.extractFeature[CLOSE]

    def produceChart(self, targetFilepath):

        datesRange = self.extractDate()
        closeValues = self.extractClose()

        plt.plot(datesRange, closeValues, color='red', marker='o')
        plt.title('Simple Line Chart', fontsize=14)
        plt.xlabel('Date', fontsize=14)
        plt.ylabel('Close value', fontsize=14)
        plt.grid(True)
        plt.savefig(targetFilepath)
