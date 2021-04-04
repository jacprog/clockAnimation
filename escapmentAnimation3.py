import FreeCAD
import FreeCADGui
from PySide import QtGui,QtCore

#optimized for animation #angle pallet width at 2.4 degree #rod lenght at 12 mm

angleRot = 0 #rod angle rotation for pendul motion in Sketch
varRod = 0 #counter to incremant angle rotation of rod in Python
escapeRot = 0 #angle rotation of escape wheel

#main loop to update values of variable 
def update():
	global angleRot, varRod, escapeRot
	#rod animation, the motor driving the anchor in the master sketch
	FreeCAD.getDocument('escapmentAnim').getObject('Variables').angleRot = varRod*5

	#incremant counter angle of rod
	varRod+=1
	#reset value after one full rotation of rod, so can use value to decide when to start and stop anchor motion
	if FreeCAD.getDocument('escapmentAnim').getObject('Variables').angleRot ==360:
		varRod = 0
		#print(varRod, angleRot)	
	#for one rotation of rod, there is two motion of anchor
	#best value for stop and go, got 6 degree of motion, no drift 145, 54  and 325 ,234	
	#first motion

	if 145 > FreeCAD.getDocument('escapmentAnim').getObject('Variables').angleRot > 54:
		FreeCAD.getDocument('escapmentAnim').getObject('escapeWheel').AttachmentOffset = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),-escapeRot/3))
		escapeRot+=1
	#second motion
	if 325 > FreeCAD.getDocument('escapmentAnim').getObject('Variables').angleRot > 234:
		FreeCAD.getDocument('escapmentAnim').getObject('escapeWheel').AttachmentOffset = App.Placement(App.Vector(0,0,0),App.Rotation(App.Vector(0,0,1),-escapeRot/3))
		escapeRot+=1

#update the output, reposition of anchor and escape wheel
	App.getDocument('escapmentAnim').recompute()
	

timer = QtCore.QTimer()
timer.timeout.connect(update)

timer.start(20)
 # press enter to start

#timer.stop()
 # type, press enter to stop