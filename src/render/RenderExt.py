from TDStoreTools import StorageManager
import TDFunctions as TDF


ctrl_callbacks = op('replicator_callbacks_ctrl1')
viz_callbacks = op('replicator_callbacks_viz1')
geo_callbacks = op('replicator_callbacks_geo1')
renderpass_callbacks = op('replicator_callbacks_renderpass1')
geo_out_callbacks = op('replicator_callbacks_geo_out1')

class Render:

	"""
	CLASS VARS
	"""
	ReplOps = ['ctrl', 'viz']

	NumVizIndex = 20



	def __init__(self, ownerComp):
		self.ownerComp = ownerComp

		TDF.createProperty(self, 'NumGeo', value=1, dependable=True,
						   readOnly=False)

		TDF.createProperty(self, 'NumViz', value=1, dependable=True,
						   readOnly=False)

		self.Initialize()



	"""
	UNPROMOTED TOOLS
	"""

	def createAttr(self):

		for i in range(self.NumViz):
			TDF.createProperty(self, 'Viz'+str(i+1), value=1, dependable=True,
						   readOnly=False)
		for i in range(self.NumGeo):
			TDF.createProperty(self, 'Geo'+str(i+1), value=1, dependable=True,
						   readOnly=False)

	def lockUnlock(self, operator=None):
		if operator != None:
			operator.lock = True
			operator.lock = False
		else:
			passe

	"""
	PROMOTED TOOLS
	"""

	def Reset(self):

		"""
		Initialize RenderExt with NumViz=1 and NumGeo=1
		"""

		self.NumViz = 1
		self.NumGeo = 1
		self.createAttr()

	def Initialize(self, NumViz=6, NumGeo=2):

		"""
		Custom NumViz and NumGeo Setup
		"""

		self.NumViz = NumViz
		self.NumGeo = NumGeo
		self.createAttr()


	def InitRepl(self):
		"""

		"""
		# WIP
		op('replicator_viz1').par.recreateall.pulse()
		op('replicator_geo1').par.recreateall.pulse()
		op('replicator_renderpass1').par.recreateall.pulse()
		op('replicator_null_geo1').par.recreateall.pulse()
		op('replicator_render_out1').par.recreateall.pulse()

	def ReloadCallbacks(self):





	"""
	CAMERA
	"""

	def CamPreset(self):

		"""
		lmao
		"""

		pass


	"""
	DEBUGGING
	"""


	def DebugOwner(self):

		"""
		Prints info about the Render COMP
		"""

		print('name: ', self.ownerComp.name)

	def DebugRender(self):

		"""
		Prints RenderExt properties
		"""

		print('NumViz: ',self.NumViz)
		for i in range(self.NumViz):
			print('\tViz'+str(i+1)+': ', str(eval('self.Viz'+str(i+1))))
		print('NumGeo: ',self.NumGeo)
		for i in range(self.NumGeo):
			print('\tGeo'+str(i+1)+': ', str(eval('self.Geo'+str(i+1))))
