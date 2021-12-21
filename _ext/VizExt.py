
from TDStoreTools import StorageManager
import TDFunctions as TDF

class VizExt:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

		TDF.createProperty(self, 'Geo1', value=3, dependable=True,
						   readOnly=False)

		TDF.createProperty(self, 'Geo2', value=4, dependable=True,
						   readOnly=False)

		TDF.createProperty(self, 'Viz1Index', value=1, dependable=True,
						   readOnly=False)

		TDF.createProperty(self, 'Viz2Index', value=1, dependable=True,
						   readOnly=False)

		TDF.createProperty(self, 'Viz3Index', value=1, dependable=True,
						   readOnly=False)

		TDF.createProperty(self, 'Viz4Index', value=1, dependable=True,
						   readOnly=False)

		TDF.createProperty(self, 'Viz5Index', value=1, dependable=True,
						   readOnly=False)

		TDF.createProperty(self, 'Viz6Index', value=1, dependable=True,
						   readOnly=False)

