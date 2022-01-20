
from TDStoreTools import StorageManager
import TDFunctions as TDF

class VmxrExt:


	def __init__(self, ownerComp):
		self.ownerComp = ownerComp


	def InitRender(self): 
		render = op.Render.ops('replicator*')
		for i in len(render):
			print(i)


	def InitVmxr(self):
		render = op.VMXR.op('render')
		render.InitRender