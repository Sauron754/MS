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
def lin_mov(x_pos, y_pos, z_pos, x_movement, y_movement, z_movement):
	import MPS
	MPS.object_interstage[0] = x_pos + x_movement * MPS.sequence_time
	MPS.object_interstage[1] = y_pos + y_movement * MPS.sequence_time
	MPS.object_interstage[2] = z_pos + z_movement * MPS.sequence_time
	return True