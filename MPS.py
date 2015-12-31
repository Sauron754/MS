#prototype module launcher
#!main launcher module!#
#!---need to add leftover parameters---!#
def MPS(precision, time_total, object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov):
	import MPS_modules
	import MPS_object
	global precision_global
	global time_total_global
	global object_1
	global sequence_time
	global runthrough_number
	#--globalises parameters--#
	time_total_global = time_total
	precision_global = precision
	#-----------#
	#--defines object--#
	object_1 = MPS_object.object_class(object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov)
	#-----------#
	#--calculates time per runthroug according to precision
	negative_precision = 0-precision
	sequence_time = 10**negative_precision
	#-----------#
	#--calculates numbers of runthroughs--#
	runthrough_number = time_total / sequence_time
	#-----------#
	#!---calculation process---!
	for process_number in range(int(runthrough_number)):
		#**linear movement module**#
		new_coordinates = MPS_modules.lin_mov(1)
		object_1.x_pos = new_coordinates[0]
		object_1.y_pos = new_coordinates[1]
		object_1.z_pos = new_coordinates[2]
		output = [object_1.x_pos , object_1.y_pos, object_1.z_pos]
		print("After process:", process_number, "\n object 1 is at: ", output)
		#**linear movement module end**#
	#-----------#