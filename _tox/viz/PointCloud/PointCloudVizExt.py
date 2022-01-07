
from TDStoreTools import StorageManager
import TDFunctions as TDF

class PointCloudVizExt:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		
		TDF.createProperty(self, 'Index', value=op.Viz.Viz1Index, dependable=True,
						   readOnly=False)

		"""
		GEOMETRY
		"""
		self.Geometry = 'viz1/null_geo'

		"""
		RENDER
		"""

		self.Render_camera = 'cam1'
		self.Render_lights = ''

		"""
		MATERIAL
		"""

		self.Mat = 'pointsprite1'
		self.Mat_color = ''

		"""
		INSTANCES
		"""

		self.Inst_state = 1

		self.Inst_tra = 'viz1/null_tra'
		self.Inst_tx = 'r'
		self.Inst_ty = 'g'
		self.Inst_tz = 'b'

		self.Inst_rot = ''
		self.Inst_rx = ''
		self.Inst_ry = ''
		self.Inst_rz = ''

		self.Inst_sca = ''
		self.Inst_sx = ''
		self.Inst_sy = ''
		self.Inst_sz = ''

		self.Inst_piv = ''
		self.Inst_sx = ''
		self.Inst_sy = ''
		self.Inst_sz = ''

		self.Inst_col = 'viz1/null_col'
		self.Inst_r = 'r'
		self.Inst_g = 'g'
		self.Inst_b = 'b'
		self.Inst_a = 'a'

		self.Inst_texs = ''
		self.Inst_texindexop = ''
		self.Inst_texindex = ''


		run(
			"args[0].PostInit() if args[0] and hasattr(args[0], 'PostInit') else None",
			self.ownerComp,
			endFrame=True,
			delayRef=op.TDResources
		)
