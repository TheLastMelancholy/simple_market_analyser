import Terms
from Fetchers.LocalFetcher import *

# Probabaly would just extract some
# features and store them
# like
# parameter : rsi, value: 30, bullValue: 20, bearValue: 70
# and  some lambda parameter -> [0, 1] 

class FeatureExtracted():
	def __init__(self, value, knot1, knot2, binaryF):
		self.value = value
		self.knot1 = knot1
		self.knot2 = knot2
		self.binaryF = binaryF

class PreProcessor():
	def __init__(self, dataType, dataPath):
		#TODO write if and logics
		self.fetcher = LocalFetcher(dataPath)

	# Actually what to do with cummulative?
	# probably cache the prices that place
	# with some depth

	def prepareData(self):
		prepared = {}

		# TODO - Async

		newChunk = next(self.fetcher.dataReader)

		prepared[Terms.CLOSE] = newChunk.C

		return prepared
		
		#for bar in self.fetcher.dataReader:
		#	prepared[Terms.CLOSE] = bar.close
		#	yield prepared

			# There are supposed to take place rich feature extraction