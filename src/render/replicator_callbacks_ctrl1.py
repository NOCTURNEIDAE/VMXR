# me - this DAT
# 
# comp - the replicator component which is cooking
# allOps - a list of all replicants, created or existing
# newOps - the subset that were just created
# template - table DAT specifying the replicator attributes
# master - the master operator
#

def viz_list_gen(numViz):
	for i in range(numViz):
		pass
		

def onRemoveReplicant(comp, replicant):

	replicant.destroy()
	return

def onReplicate(comp, allOps, newOps, template, master):
	path = op('null_path')

	for c in newOps:
		#c.display = True
		#c.render = True
		#c.par.display = 1
		#c.par.clone = comp.par.master
		c.allowCooking = True
		c.par.externaltox = 'D:/VMXR/Vizbank/'+str(op('null_path')[c.digits,0]) + '/ctrl.tox'
		c.par.reinitnet.pulse()
		
		
		pass

	return
