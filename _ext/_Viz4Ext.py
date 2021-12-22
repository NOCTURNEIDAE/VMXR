
from TDStoreTools import StorageManager
import TDFunctions as TDF

class Viz4Ext:

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
		
		self.Inst_state = 1

		self.Inst_tra = 'viz4/null_tra'
		self.Inst_tx = 'tx'
		self.Inst_ty = 'ty'
		self.Inst_tz = 'tz'
		
		self.Inst_rot = 'viz4/null_rot'
		self.Inst_rx = 'rx'
		self.Inst_ry = 'ry'
		self.Inst_rz = 'rz'
		
		self.Inst_sca = 'viz4/null_sca'
		self.Inst_sx = 'r'
		self.Inst_sy = 'g'
		self.Inst_sz = 'b'
		
		self.Inst_col = 'viz4/null_col'
		self.Inst_r = 'r'
		self.Inst_g = 'g'
		self.Inst_b = 'b'
		self.Inst_a = 'a'
		
		self.Inst_texs = 'viz4/tex/tex*'
		self.Inst_texindexop = 'viz4/null_texindexop'
		self.Inst_texindex = 'b'
		