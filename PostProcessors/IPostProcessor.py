# draw, genetate pdf's, send data to some server
# or store pictures
# or write about signals
# whatsoever
# on this step data already labeled and validated


# There are were be a lot of them
# Probably in plugin-like structure


class IPostProcessor():

    def __init__(self):
        self.configPath = None

    def configurate(self, configPath):
        self.configPath = configPath

    def utilizeData(self, data):
        return NotImplemented("must be defined in child classes")
