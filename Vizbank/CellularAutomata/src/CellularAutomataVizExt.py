
from TDStoreTools import StorageManager
import TDFunctions as TDF

class CellularAutomataVizExt:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

		TDF.createProperty(self, 'Index', value=1, dependable=True,
						   readOnly=False)

		"""
		GEOMETRY
		"""
		self.Geometry = 'viz2/null_geo'

		"""
		RENDER
		"""
		
		self.Render_camera = 'cam1'
		self.Render_lights = ''
		
		"""
		MATERIAL
		"""
		
		self.Mat = ''
		self.Mat_color = ''
		
		"""
		INSTANCES
		"""
		
		self.Instancing = 1
		
		self.Inst_tra = 'viz2/null_tra'
		self.Instancetx = 'r'
		self.Instancety = 'g'
		self.Instancetz = 'b'
		
		self.Inst_rot = 'viz2/null_rot'
		self.Instancerx = 'r'
		self.Instancery = 'g'
		self.Instancerz = 'b'
		
		self.Inst_sca = 'viz2/null_sca'
		self.Instancesx = 'r'
		self.Instancesy = 'g'
		self.Instancesz = 'b'
		
		self.Inst_piv = ''
		self.Instancesx = 'r'
		self.Instancesy = 'g'
		self.Instancesz = 'b'
		
		self.Inst_col = 'viz2/null_col'
		self.Instancer = 'r'
		self.Instanceg = 'g'
		self.Instanceb = 'b'
		self.Inst_a = 'a'
		
		self.Inst_texs = ''
		self.Inst_texindexop = ''
		self.Inst_texindex = ''