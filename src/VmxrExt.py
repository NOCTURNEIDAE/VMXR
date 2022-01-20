
from TDStoreTools import StorageManager
import TDFunctions as TDF

class VmxrExt:

	# render = op.Render

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp


	def InitRender(self, render): 
		print(op.Render.name)


	def InitVmxr(self):
		self.InitRender()
