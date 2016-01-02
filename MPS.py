#prototype module launcher
#!main launcher module!#
#!---need to add leftover parameters---!#
def MPS(precision, time_total, object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov):
	from MPS_modules import lin_mov
	import MPS_object
	global precision_global
	global time_total_global
	global object_1
	global sequence_time
	global runthrough_number
	global object_properties
	global assigned_objects
	#--creates list with placeholders for 5 objects--#
	object_properties = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
	#-----------#
	assigned_objects = [False, False, False, False, False]
	#--globalises parameters--#
	time_total_global = time_total
	precision_global = precision
	#-----------#
	#--defines object--#
	object_1 = MPS_object.object_class(object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov)
	assigned_objects[0] = True
	#-----------#
	#--calculates time per runthroug according to precision
	negative_precision = 0-precision
	sequence_time = 10**negative_precision
	#-----------#
	#--calculates numbers of runthroughs--#
	runthrough_number = time_total / sequence_time
	#-----------#
	#checks how many objects there are#
	assigned_objects_number = 0
	for object_number in range(5):
		if assigned_objects[object_number] == True:
			assigned_objects_number = assigned_objects_number + 1
		else:
			pass
	else:
		del(object_number)
	#-----------#
	#!---calculation process---!
	for process_number in range(int(runthrough_number)):
		#**linear movement module**#
		for object_number in range(1, assigned_objects_number + 1):
		object_1.export_values(object_number)
		new_coordinates = lin_mov(object_number)
		if object_number = 1:
			object_1.xpos = new_coordinates[0]
			object_1.ypos = new_coordinates[1]
			object_1.zpos = new_coordinates[2]
			output = [object_1.x_pos , object_1.y_pos, object_1.z_pos]
		else:
			print("You should never get this message. This is only a way for me to prevent unstable versions to crash completely")
		print("After process:", process_number, "\n object 1 is at: ", output)
		#**linear movement module end**#
	#-----------#