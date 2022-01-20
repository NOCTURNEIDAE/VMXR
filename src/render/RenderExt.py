from TDStoreTools import StorageManager
import TDFunctions as TDF

class Render:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
						   
		

		TDF.createProperty(self, 'NumViz', value=6, dependable=True,
						   readOnly=False)

		TDF.createProperty(self, 'NumGeo', value=2, dependable=True,
						   readOnly=False)

		num_viz = self.NumViz
		num_geo = self.NumGeo

		for i in range(num_viz):
			name = 'Viz'+str(i+1)+'Index'
			TDF.createProperty(self, name=name, value=1, dependable=True,
							   readOnly=False)
		for i in range(num_geo):
			name = 'Geo'+str(i+1)
			TDF.createProperty(self, name=name, value=1, dependable=True,
							   readOnly=False)


	"""
	DEBUG TOOLS
	"""

	def DebugAttr(self):
		num_viz = self.NumViz
		num_geo = self.NumGeo
		print('')
		print('----------------------------------------')
		print('VizCOMP Attributes:')
		print('')
		print('NumViz: '+str(num_viz))
		print('NumGeo: '+str(num_geo))
		print('----------------------------------------')

	def DebugViz(self):

		print('----------------------------------------')
		print('Viz Info')
		for i in range(self.NumViz):

			i+=1
			print('Viz'+str(i)+': '+op('null_path')[i,'name'])

			index_ext = 'print(op.Viz.Viz'+str(i)+'Index)'
			exec(index_ext)
			index_tox = 'print(op._viz'+str(i)+'.Index)'
			exec(index_tox)

		print('----------------------------------------')

	def DebugGeo(self):

		print('----------------------------------------')
		num_geo = self.NumGeo
		print('Geo Info')
		print('')
		print('Geo1: '+str(self.Geo1))
		print('Geo2: '+str(self.Geo2))

		print('----------------------------------------')

	def DebugAll(self):
		self.DebugAttr()
		self.DebugViz()
		self.DebugGeo()



	"""
	HELP
	"""

	def Help(self):
		print('')
		print('----------------------------------------')
		print('''VizCOMP Methods. They must be called manually 
in this exact order to initialize the Viz COMP''')
		print('')
		print('1: op.Viz.InitViz()')
		print('2: op.Viz.InitConnections()')
		print('----------------------------------------')



	"""
	INITIALIZE
	"""

	def InitRender(self):
		op('replicator_ctrl1').par.recreateall.pulse()
		op('replicator_viz1').par.recreateall.pulse()

		
	def InitConnections(self):
		op('viz1').inputConnectors[0].connect(op('ctrl1').outputConnectors[0])
		op('viz2').inputConnectors[0].connect(op('ctrl2').outputConnectors[0])
		op('viz3').inputConnectors[0].connect(op('ctrl3').outputConnectors[0])
		op('viz4').inputConnectors[0].connect(op('ctrl4').outputConnectors[0])
		op('viz5').inputConnectors[0].connect(op('ctrl5').outputConnectors[0])
		op('viz6').inputConnectors[0].connect(op('ctrl6').outputConnectors[0])


	def InitRenderPass(self):
		num_geo = self.NumGeo
		for i in range(num_geo):
			if i == 0:
				i+=1
				print('first')
				op('renderpass'+str(i)).inputConnectors[0].connect(op('render1'))

			elif i == num_geo-1:
				i+=1
				print('last')

				op('renderpass'+str(i-1)).outputConnectors[0].connect(op('renderpass'+str(i)).inputConnectors[0])

			elif 0 < i < num_geo:
				i+=1
				op('renderpass'+str(i-1)).outputConnectors[0].connect(op('renderpass'+str(i)).inputConnectors[0])

			else:
				pass

	def Init(self):
		self.InitViz()

	

	"""
	SETTER
	"""
	def SetViz(self):
		for i in enumerate(self.NumViz):

			out = 'op._viz'+str(i+1)+'.Index = '+'self.Viz'+str(i+1)+'Index'
			#exec(out)
			print(out)



	"""
	TESTER
	"""
	def TestAll(self):
		pass
		