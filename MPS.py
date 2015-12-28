#prototype module launcher
#!main launcher module!#
#!---need to add leftover parameters---!#
def MPS(precision, time_runthrough, runthrough_number, object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov):
	import MPS_modules
	import MPS_object
	global precision
	global time_runthrough
	global object_1
	global sequence_time
	#--defines object--#
	object_1 = MPS_object.object_class(object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov)
	#-----------#
	#--calculates time per runthroug according to precision
	negative_precision = 0-precision
	sequence_time = 10**negative_precision
	#-----------#
	#!---calculation process---!
	for process_number in range(runthrough_number):
		#**linear movement module**#
		new_coordinates = MPS_modules.lin_mov(1)
		object_1.x_pos = new_coordinates[0]
		object_1.y_pos = new_coordinates[1]
		object_1.z_pos = new_coordinates[2]
		#**linear movement module end**#
	#-----------#