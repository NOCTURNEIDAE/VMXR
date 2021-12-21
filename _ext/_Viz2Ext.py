
from TDStoreTools import StorageManager
import TDFunctions as TDF

class Viz2Ext:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

		TDF.createProperty(self, 'Index', value=1, dependable=True,
						   readOnly=False)

		"""
		GEOMETRY
		"""
		self.Geo_out = 'viz1/null_geo'

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
		
		self.Inst_tra = 'viz2/null_tra'
		self.Inst_tx = 'r'
		self.Inst_ty = 'g'
		self.Inst_tz = 'b'
		
		self.Inst_rot = 'viz2/null_rot'
		self.Inst_rx = 'r'
		self.Inst_ry = 'g'
		self.Inst_rz = 'b'
		
		self.Inst_sca = 'viz2/null_sca'
		self.Inst_sx = 'r'
		self.Inst_sy = 'g'
		self.Inst_sz = 'b'
		
		self.Inst_piv = ''
		self.Inst_sx = 'r'
		self.Inst_sy = 'g'
		self.Inst_sz = 'b'
		
		self.Inst_col = 'viz2/null_col'
		self.Inst_r = 'r'
		self.Inst_g = 'g'
		self.Inst_b = 'b'
		self.Inst_a = 'a'
		
		self.Inst_texs = ''
		self.Inst_texindexop = ''
		self.Inst_texindex = ''