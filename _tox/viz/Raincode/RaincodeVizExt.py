
from TDStoreTools import StorageManager
import TDFunctions as TDF

class RaincodeVizExt:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

		TDF.createProperty(self, 'Index', value=1, dependable=True,
						   readOnly=False)

		"""
		GEOMETRY
		"""
		self.Geo_out = 'viz4/null_geo'


		"""
		RENDER
		"""
		
		self.Render_camera = 'cam1'
		self.Render_lights = ''
		
		"""
		MATERIAL
		"""
		
		self.Mat = 'constant1'
		self.Mat_color = ''
		
		"""
		INSTANCES
		"""
		
		self.Inst_state = 0