from PySide import QtCore

angleRot = 0
varRod = 0
escapeRot = 0
 
def update():
	global angleRot, varRod, escapeRot
	#rod animation, the motor driving the anchor in the master sketch
	FreeCAD.getDocument('escapmentAnim').getObject('Variables').angleRot = varRod*5

	#best valuefor stop and go, got 6 degree of motion, no drift 145, 54  and 325 234
	varRod+=1
	#reset value after one full rotation of rod, so can use value to start and stop anchor motion
	if FreeCAD.getDocument('escapmentAnim').getObject('Variables').angleRot ==360:
		varRod = 0
	
	#for one rotation of rod, ther is two motion of anchor	
	#first motion
	if 145 > FreeCAD.getDocument('escapmentAnim').getObject('Variables').angleRot > 54:
		FreeCAD.getDocument('escapmentAnim').getObject('escapeWheel').AttachmentOffset = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),-escapeRot/3))
		escapeRot+=1
	#second motion
	if 325 > FreeCAD.getDocument('escapmentAnim').getObject('Variables').angleRot > 234:
		FreeCAD.getDocument('escapmentAnim').getObject('escapeWheel').AttachmentOffset = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),-escapeRot/3))
		escapeRot+=1

	App.getDocument('escapmentAnim').recompute()

timer = QtCore.QTimer()
timer.timeout.connect(update)

timer.start(1)
# press enter to start
#type following to stop
timer.stop()