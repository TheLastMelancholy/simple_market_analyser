from Config import DataModel, DataPath
from PreProcessor import *
from PostProcessor import *

class Manager():

	def __init__(self):
		# Now kind of hardcoding for
		# local data model
		self.preProcessor  = PreProcessor(DataModel, DataPath)
		self.postProcessor = PostProcessor(DataModel, DataPath)