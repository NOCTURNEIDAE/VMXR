
from TDStoreTools import StorageManager
import TDFunctions as TDF

# AY

class AsciiVizExt:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

		TDF.createProperty(self, 'Index', value=1, dependable=True,
						   readOnly=False)

		"""
		GEOMETRY
		"""
		self.Geomain = './null_geo'


		"""
		RENDER
		"""
		
		self.Pass_camera = 'cam1'
		self.Render_lights = ''
		
		"""
		MATERIAL
		"""
		
		self.Mat = 'constant1'
		self.Mat_color = ''
		
		"""
		INSTANCES
		"""
		
		self.Instancing = False
		#getattr(exec("op.Render.Geo"+str(me.digits),eval("me.curPar.name.capitalize()"))

		self.Instancetop = 'null_tra'
		self.Instancetx = 'tx'
		self.Instancety = 'ty'
		self.Instancetz = 'tz'
		
		self.Instancerop = 'null_rot'
		self.Instancerx = 'rx'
		self.Instancery = 'ry'
		self.Instancerz = 'rz'
		
		self.Instancesop = 'null_sca'
		self.Instancesx = 'r'
		self.Instancesy = 'g'
		self.Instancesz = 'b'
		
		self.Instancepop = 'null_col'
		self.Instancer = 'r'
		self.Instanceg = 'g'
		self.Instanceb = 'b'
		self.Instancea = 'a'
		
		self.Inst_texs = 'viz4/tex/tex*'
		self.Inst_texindexop = 'viz4/null_texindexop'
		self.Inst_texindex = 'b'
		