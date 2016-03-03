#MPS module collection
#
#
#more loops for more objects will be added soon
#
#
#
#
#
#
def lin_mov(object_number):
	import MPS #might cause recursive error!
	if object_number == 1:
		object_1.x_pos = object_1.x_pos + (object_1.x_movement * MPS.sequence_time)
		object_1.y_pos = object_1.y_pos + (object_1.y_movement * MPS.sequence_time)
		object_1.z_pos = object_1.z_pos + (object_1.z_movement * MPS.sequence_time)
	return True