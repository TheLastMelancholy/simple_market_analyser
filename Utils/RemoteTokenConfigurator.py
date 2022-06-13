import json
import os


class TickersUpdater(self):
    def __init__(self, dirPath):
        self.dirPath = dirPath
        # CF-1 ToDict
        self.synchronizers = []

    def initializeSynchronizers(self):
        jsonFiles = filter(os.listdir(self.dirPath))

class TokenSynchronizer():
    def __init__(self, configPath):
        self.configPath = None
        self.pendingUpdateTime = None
        self.readConfig()

    def readConfig(self):
        with open(self.configPath) as jsonFile:

        ...

