
from TDStoreTools import StorageManager
import TDFunctions as TDF

class CellularAutomataCtrlExt:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

		TDF.createProperty(self, 'Index', value=9, dependable=True,
						   readOnly=False)