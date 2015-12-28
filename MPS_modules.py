#linear movement module for x,y,z dimensions without inbound collisions and multiple objects
def lin_mov(object_number):
	#---select object to call---#
	if object_number == 1:
		x_pos = object_1.x_pos
		y_pos = object_1.y_pos
		z_pos = object_1.z_pos
		xmov = object_1.x_movement
		ymov = object_1.y_movement
		zmov = object_1.z_movement
		coordinates = [x_pos, y_pos, z_pos]
		movement = [xmov, ymov, zmov]
		
	else:
		raise AttributeError("UNABLE TO FIND OBJECT!")