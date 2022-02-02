# me - this DAT
# 
# comp - the replicator component which is cooking
# allOps - a list of all replicants, created or existing
# newOps - the subset that were just created
# template - table DAT specifying the replicator attributes
# master - the master operator
#

def debug_newops(newOp, index):
	print('-----')
	print('name: ',newOp.name)
	print('index: ',index)
	print(op.Render.Geo1Index)




def onRemoveReplicant(comp, replicant):

	replicant.destroy()
	return

def onReplicate(comp, allOps, newOps, template, master):

	for i, c in enumerate(newOps, 1):
		stri = str(eval("op.Render.Geo"+str(i)))
		c.display = True
		c.render = True
		#c.par.display = 1
		#c.par.clone = comp.par.master
		c.allowCooking = True

		"""
		SETTING UP ./select1
		"""


		c.op('./select_geo').par.sop.expr = exec("op('viz_list')[1,1]")

		pars_expr = "getattr(op.Render.Geo"+str(eval("op.Render.Geo"+str(i)))+",me.curPar.name.capitalize(),1)"

		c.par.instancing.expr = pars_expr
		c.par.instancetop.expr = ''
		c.par.instancetx.expr = ''
		c.par.instancety.expr = ''
		c.par.instancetz.expr = ''
		c.par.instancerop.expr = ''
		c.par.instancerx.expr = ''
		c.par.instancery.expr = ''
		c.par.instancerz.expr = ''
		c.par.instancesop.expr = ''
		c.par.instancesx.expr = ''
		c.par.instancesy.expr = ''
		c.par.instancesz.expr = ''
		c.par.instancepop.expr = ''
		c.par.instancepx.expr = ''
		c.par.instancepy.expr = ''
		c.par.instancepz.expr = ''


		#debug_newops(c,i)

		print(pars_expr)


		pass

	return
