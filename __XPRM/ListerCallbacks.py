#Shared Use License: This file is owned by Derivative Inc. (â€œDerivativeï¿½) 
#and can only be used, and/or modified for use, in conjunction with 
#Derivativeâ€™s TouchDesigner software, and only if you are a licensee who 
#has accepted Derivativeâ€™s TouchDesigner license or assignment agreement 
#(which also governs the use of this file).  You may share a modified version 
#of this file with another authorized licensee of Derivativeâ€™s TouchDesigner 
#software.  Otherwise, no redistribution or sharing of this file, with or 
#without modification, is permitted.

"""
All callbacks for this lister go in this DAT. For a list of available callbacks,
see:

https://docs.derivative.ca/Palette:lister#Custom_Callbacks
"""

# def onSelectRow(info):
# 	print(info)

def onClick(info):
	out = info.get('colName')
	print(out)

	targetTable = op('../table_info')
 
def onClick(info):
	clickedRow = info.get('row')
	clickedCol = info.get('col')
	cellText = info.get('cellText')
 
	targetTable['row', 1] = clickedRow
	targetTable['col', 1] = clickedCol
	targetTable['text', 1] = cellText

	# find the intput table DAT
	inputTable =  info.get('ownerComp').par.Inputtabledat.eval()
	 
	# find the data from the column called 'state'
	stateCol = inputTable.col('Geo1')  
	 
	# replace the contents of the colum
	newStateData = [True if eachCell.row == info.get('row') else False for eachCell in stateCol[1:]]
	 
	# insert the header into the column
	newStateData.insert(0, 'Geo1')
	 
	# overwrite the column in the input table
	inputTable.replaceCol('Geo1', newStateData)