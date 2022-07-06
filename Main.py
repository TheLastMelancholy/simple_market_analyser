from Reporter import Reporter
from Analyzer import Analyzer
from Updater import Updater
from Visualiser import Visualiser
import os

currFolder = os.getcwd()
assetsDescriptorsFolder = os.path.join(currFolder, "SelectedAssets")
assetsFeaturesFolder = os.path.join(currFolder, "AssetsReportsData")

updater = Updater(assetsDescriptorsFolder())
updater.revalidateData()

analyzer = Analyzer(assetsDescriptorsFolder, assetsFeaturesFolder)
analyzer.extractFeatures()

visualiser = Visualiser(assetsDescriptorsFolder, assetsFeaturesFolder)
visualiser.prepareGraphs()

reporter = Reporter(assetsFeaturesFolder)
reporter.prepareReport()
