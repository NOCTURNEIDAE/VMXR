# me - this DAT
# 
# channel - the Channel object which has changed
# sampleIndex - the index of the changed sample
# val - the numeric value of the changed sample
# prev - the previous sample value
# 
# Make sure the corresponding toggle is enabled in the CHOP Execute DAT.

def onOffToOn(channel, sampleIndex, val, prev):
	return

def whileOn(channel, sampleIndex, val, prev):
	return

def onOnToOff(channel, sampleIndex, val, prev):
	return

def whileOff(channel, sampleIndex, val, prev):
	return

def onValueChange(channel, sampleIndex, val, prev):
	if channel.name == 'viz1_i':
		op.Viz.Viz1Index = int(val)
	elif channel.name == 'viz2_i':
		op.Viz.Viz2Index = int(val)
	elif channel.name == 'viz3_i':
		op.Viz.Viz3Index = int(val)
	elif channel.name == 'viz4_i':
		op.Viz.Viz4Index = int(val)
	elif channel.name == 'viz5_i':
		op.Viz.Viz5Index = int(val)
	elif channel.name == 'viz6_i':
		op.Viz.Viz6Index = int(val)
	else:
		pass
	return
	