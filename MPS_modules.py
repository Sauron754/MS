#linear movement module for x,y,z dimensions without inbound collisions and multiple objects
def lin_mov(object_number):
	#---select object to call---#
	if object_number < 5:
		object_index = object_number * 17
		x_pos = object_properties[0 + object_number]
		y_pos = object_properties[1 + object_number]
		z_pos = object_properties[2 + object_number]
		xmov = object_properties[3 + object_number]
		ymov = object_properties[4 + object_number]
		zmov = object_properties[5 + object_number]
		coordinates = [x_pos, y_pos, z_pos]
		movement = [xmov, ymov, zmov]
		sequence_movement = [False, False, False]
		#---!sets movement per calculation process according to precision!---#
		for i in range(3):
			sequence_movement[i] = movement[i] * sequence_time
		new_x_pos = x_pos + sequence_movement[0]
		new_y_pos = y_pos + sequence_movement[1]
		new_z_pos = z_pos + sequence_movement[2]
		new_coordinates = [new_x_pos, new_y_pos, new_z_pos]
		return new_coordinates
	else:
		#!-- OSError is just a placeholder for the upcoming selfdefined error --!#
		raise AttributeError("UNABLE TO FIND OBJECT!")