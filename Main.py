from Reporter import Reporter
from Analyzer import Analyzer
from Updater import Updater
import os

currFolder = os.getcwd()
assetsDescriptorsFolder = os.path.join(currFolder, "SelectedAssets")
assetsFeaturesFolder = os.path.join(currFolder, "AssetsReportsData")


updater = Updater(assetsDescriptorsFolder())
updater.revalidateData()

analyzer = Analyzer(assetsDescriptorsFolder, assetsFeaturesFolder)
analyzer.extractFeatures()

reporter = Reporter(assetsFeaturesFolder)
reporter.prepareReport()
