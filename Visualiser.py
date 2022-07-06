from Visualisers import *


class Visualiser():
    def __init__(sefl, assetsDescriptorsPath, assetsFeaturesPath):
        self.assetsDescriptorsPath = assetsDescriptorsPath
        self.assetsFeaturesPath = passetsFeaturesPath
        self.activeVisualisers = Visualisers.processors

    def extractData(self, path):
        # Read data from some csv file

    def listDataSources(self):
        # return csv files from directory

    def createAssetsMapping(self):
        # create dictionary storing pairs
        # asset - list of all that is known about it
        # add later

    def prepareGraphs(self):
        # later for each asset separately
        # now there will be one test asset
        ochlLists = self.listDataSources()
        # now only ochl csv
        for file in ochlLists:
            self.extractData(file)

