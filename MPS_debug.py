#prototype module launcher#
#!main launcher module!#
#!---need to add leftover parameters---!#
def MPS(precision, time_total, object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov):
	from MPS_modules_debug import lin_mov
	from MPS_object_debug import object_class
	from MPS_base_functions_debug import coordinate_assign
	from MPS_base_functions_debug import export_values
	from MPS_base_functions_debug import glob_var
	global precision_global
	global time_total_global
	global object_1
	global sequence_time
	global runthrough_number
	global object_properties
	global assigned_objects
	global test_namespaces
	#creates variable for testing global namespaces
	test_namespaces = True
	#-----------#
	#testes own global access
	if glob_var == True:
		print("namespaces valid")
	else:
		#defined error needs to be implemented
		raise(OSError("global namespaces invalid"))
	#-----------#
	#MPS_base_functions#
	#def coordinate_assign(new_coordinates, object_number):
	#	global output
	#	if object_number == 1:
	#		object_1.x_pos = new_coordinates[0]
	#		object_1.y_pos = new_coordinates[1]
	#		object_1.z_pos = new_coordinates[2]
	#		output = [object_1.x_pos, object_1.y_pos, object_1.z_pos]
	#	elif object_number == 2:
	#		object_2.x_pos = new_coordinates[0]
	#		object_2.y_pos = new_coordinates[1]
	#		object_2.z_pos = new_coordinates[2]
	#		output = [object_2.x_pos, object_2.y_pos, object_2.z_pos]
	#	elif object_number == 3:
	#		object_3.x_pos = new_coordinates[0]
	#		object_3.y_pos = new_coordinates[1]
	#		object_3.z_pos = new_coordinates[2]
	#		output = [object_3.x_pos, object_3.y_pos, object_3.z_pos]
	#	elif object_number == 4:
	#		object_4.x_pos = new_coordinates[0]
	#		object_4.y_pos = new_coordinates[1]
	#		object_4.z_pos = new_coordinates[2]
	#		output = [object_4.x_pos, object_4.y_pos, object_4.z_pos]
	#	elif object_number == 5:
	#		object_5.x_pos = new_coordinates[0]
	#		object_5.y_pos = new_coordinates[1]
	#		object_5.z_pos = new_coordinates[2]
	#		output = [object_5.x_pos, object_5.y_pos, object_5.z_pos]
	#	else:
	#		print("You should never see this. I use this to stop unstable versions from crashing completely")

	#def export_values(object_number):
	#	if object_number > 5:
	#		#--again OSError is just temporary--#
	#		raise OSError("Object number bejond possibility")
	#	else:
	#		object_index = object_number * 17
	#		if object_number == 1:
	#			data = object_1.data
	#		elif object_number == 2:
	#			data = object_2.data
	#		elif object_number == 3:
	#			data = object_3.data
	#		elif object_number == 4:
	#			data = object_4.data
	#		elif object_number == 5:
	#			data = object_5.data
	#		for variable in range(17):
	#			index_number = variable + object_index
	#			object_properties[index_number] = data[variable]
	#-----------#
	#-creates list with placeholders for 5 objects and import object_class--#
	object_properties = [False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False, False]
	#-----------#
	assigned_objects = [False, False, False, False, False]
	#--globalises parameters--#
	time_total_global = time_total
	precision_global = precision
	#-----------#
	#--defines object--#
	object_1 = object_class(object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov)
	assigned_objects[0] = True
	#-----------#
	#exports data of objects to object_properties cluster#
	if assigned_objects[0] == True:
		export_values(1)
	if assigned_objects[1] == True:
		export_values(2)
	if assigned_objects[2] == True:
		export_values(3)
	if assigned_objects[3] == True:
		export_values(4)
	if assigned_objects[4] == True:
		export_values(5)
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
	for object_constant in range(5):
		if assigned_objects[object_constant] == True:
			assigned_objects_number = assigned_objects_number + 1
		else:
			pass
	#-----------#
	#!---calculation process---!
	for process_number in range(int(runthrough_number)):
		#**linear movement module**#
		for object_number in range(1, assigned_objects_number + 1):
			new_coordinates = lin_mov(object_number)
			coordinate_assign(new_coordinates, object_number)
			#creates coordinate lists
			object_1_coordinates = [object_1.x_pos, object_1.y_pos, object_1.z_pos]
			#object_2_coordinates = [object_2.x_pos, object_2.y_pos, object_2.z_pos]
			#object_3_coordinates = [object_3.x_pos, object_3.y_pos, object_3.z_pos]
			#object_4_coordinates = [object_4.x_pos, object_4.y_pos, object_4.z_pos]
			#object_5_coordinates = [object_5.x_pos, object_5.y_pos, object_5.z_pos]
			#-----------#
		print("After process:", process_number, "\n object 1 is at: ", object_1_coordinates)
		#print("After process:", process_number, "\n object_2 is at: ", object_2_coordinates)
		#print("After process:", process_number, "\n object_3 is at: ", object_3_coordinates)
		#print("After process:", process_number, "\n object_4 is at: ", object_4_coordinates)
		#print("After process:", process_number, "\n object_5 is at: ", object_5_coordinates)
		#**linear movement module end**#
	#-----------#