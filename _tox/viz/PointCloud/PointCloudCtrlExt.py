from TDStoreTools import StorageManager
import TDFunctions as TDF

class PointCloudCtrlExt:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

		TDF.createProperty(self, 'Index', value=op.Viz.Viz1Index, dependable=True,
						   readOnly=False)
