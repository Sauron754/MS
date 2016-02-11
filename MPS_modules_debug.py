#linear movement module for x,y,z dimensions without inbound collisions and multiple objects
#MPS Modules debug mode
#
#
#
#
#
#debug mode prints every variable which is beeing modified
def lin_mov(object_number):
	#!-- test global namespace system --!#
	#print(test_namespaces)
	#-----------#
	#---select object to call---#
	from MPS_debug import object_properties
	from MPS_debug import sequence_time
	global object_properties
<<<<<<< HEAD
	print("object_properties:", object_properties)
	print("object_number:", object_number)
	print("initial x_pos:", object_properties[0])
	print("initial y_pos:", object_properties[1])
	print("initial z_pos:", object_properties[2])
	print("initial x_mov:", object_properties[3])
	print("initial y_mov:", object_properties[4])
	print("initial z_mov:", object_properties[5])

=======
	print("object_properties: ", object_properties)
>>>>>>> master
	if object_number < 5:
		object_index = object_number * 17
		x_pos = object_properties[0 + object_number]
		y_pos = object_properties[1 + object_number]
		z_pos = object_properties[2 + object_number]
		x_mov = object_properties[3 + object_number]
		y_mov = object_properties[4 + object_number]
		z_mov = object_properties[5 + object_number]
		coordinates = [x_pos, y_pos, z_pos]
<<<<<<< HEAD
		print("coordinates:", coordinates)
		movement = [x_mov, y_mov, z_mov]
		print("movement: ", movement)
=======
		print("initial coordinates: ", coordinates)
		movement = [xmov, ymov, zmov]
		print("initial movement:", movement)
>>>>>>> master
		sequence_movement = [False, False, False]
		#---!sets movement per calculation process according to precision!---#
		for i in range(3):
			sequence_movement[i] = movement[i] * sequence_time
<<<<<<< HEAD
		print(sequence_movement)
=======
		print("sequence_movement: ", sequence_movement)
>>>>>>> master
		new_x_pos = x_pos + sequence_movement[0]
		new_y_pos = y_pos + sequence_movement[1]
		new_z_pos = z_pos + sequence_movement[2]
		print("new_x_pos: ", new_x_pos)
		print("new_y_pos: ", new_y_pos)
		print("new_z_pos: ", new_z_pos)
		new_coordinates = [new_x_pos, new_y_pos, new_z_pos]
<<<<<<< HEAD
		print("new_coordinates: ", new_coordinates)
=======
		print("new_coordinates", new_coordinates)
>>>>>>> master
		return new_coordinates
	else:
		#!-- OSError is just a placeholder for the upcoming selfdefined error --!#
		raise AttributeError("UNABLE TO FIND OBJECT!")