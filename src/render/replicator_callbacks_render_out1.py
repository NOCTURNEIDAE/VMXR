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

	for c in newOps:
		#c.display = True
		#c.render = True
		#c.par.display = 1
		#c.par.clone = comp.par.master
		c.dock = None
		d = str(c.digits)
		c.inputConnectors[0].connect(op('renderpass'+d).outputConnectors[0])

	return
