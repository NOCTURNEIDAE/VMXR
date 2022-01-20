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

	for c in newOps:
		
		path_viz = 'D:/VMXR/_tox/viz/'+str(op('null_path')[c.digits,0])+'viz.tox'
		print(path_viz)
		#c.display = True
		#c.render = True
		#c.par.display = 1
		#c.par.clone = comp.par.master
		c.allowCooking = True
		c.par.externaltox = 'D:/VMXR/Vizbank/'+str(op('null_path')[c.digits,0]) + '/viz.tox'
		c.par.reinitnet.pulse()
		c.par.extension1 = ''
		
	return
