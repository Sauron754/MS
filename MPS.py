#main module launcher module
#
#
#
#
#
#
#
#
#
def MPS(precision, time_total, object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov):
	import MPS_object
	import MPS_modules
	import decimal 
	#creates needed presets for MPS to work
	decimal.getcontext().prec = 28
	assigned_objects = 0
	negative_precision = 0 - precision
	sequence_time = 10**negative_precision
	runthrough_count =  int(time_total / sequence_time)
	#!
	#actual launcher module
	object_1 = MPS_object.object_class(object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov)
	for current_runthrough in runthrough_count:
		MPS_modules.lin_mov(1)
		object_1_output = [object_1.x_pos, object_1.y_pos, object_1.z_pos]
		print("After process number: ", current_runthrough, "object 1 is at ", object_1_output)