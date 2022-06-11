from Config import DataSourceType, DataPath
from PreProcessor import *
from PostProcessors.SimplePrinter import SimplePrinter

import os

# TODO - Read config files
# probably yaml from some dir and
# fetch options for data processors

class Configurator():

    def __init__(self):
        ...

    def listFiles(self):
        for _r, _d, _f in os.walk(DataPath):
            return [os.path.join(_r, f) for f in _f]

    def getTargets(self):

        filesWithData = self.listFiles()
        return filesWithData


class Pipeline():

    def __init__(self, preProcessor, postProcessor):
        self.preProcessor = preProcessor
        self.postProcessor = postProcessor

    def condition(self):
# TODO - Process on some trigger
        return True

    def tick(self):
        if self.condition():
            dataFetched = self.preProcessor.prepareData()
            self.postProcessor.utilizeData(dataFetched)





class Manager():

    def __init__(self):
# Now kind of hardcoding for
# local data model
#self.preProcessor  = PreProcessor(DataSourceType, DataPath)
        self.configProcessor = Configurator()
        self.processingPipelines = []

# TODO rename or make literary async
    def run(self):
# TODO  read frome some config file what
# to process and how

        for tokenSetupFile in self.configProcessor.getTargets():
            pre  = PreProcessor(DataSourceType, tokenSetupFile)
            post = SimplePrinter()

            self.processingPipelines.append(Pipeline(pre, post))

# TODO - change to some else
        while True:
            for pipeline in self.processingPipelines:
                pipeline.tick()











