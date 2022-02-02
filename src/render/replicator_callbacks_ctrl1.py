# me - this DAT
# 
# comp - the replicator component which is cooking
# allOps - a list of all replicants, created or existing
# newOps - the subset that were just created
# template - table DAT specifying the replicator attributes
# master - the master operator
#

def onRemoveReplicant(comp, replicant):

	replicant.destroy()
	return

def onReplicate(comp, allOps, newOps, template, master):
	path = op('null_path')

	for i, c in enumerate(newOps):

		viz_path = op('null_path')
		viz_name = str(viz_path[i,0])
		print('i: ',i)
		print('viz_path: ', viz_path, type(viz_path))
		print('viz_name: ', viz_name, type(viz_name))

		c.allowCooking = True
		c.par.externaltox = 'D:/VMXR/Vizbank/'+str(op('null_path')[c.digits,0])
		c.par.subcompname = 'ctrl'


		c.par.reinitnet.pulse()
		
		
		pass

	return
