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


	for i,c in enumerate(newOps):
		viz_name = str(op('viz_list')[c.digits,0])
		path_viz = 'D:/VMXR/Vizbank/' + viz_name +'/'+ viz_name + '.tox'
		c.allowCooking = True
		c.par.externaltox = path_viz
		c.par.subcompname = 'ctrl'
		c.par.reinitnet.pulse()
		
	return
