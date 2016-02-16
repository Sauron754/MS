#prototype module launcher#
#!main launcher module!#
#!---need to add leftover parameters---!#
def MPS(precision, time_total, object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov):
	from MPS_modules import lin_mov
	from MPS_object import object_class
	from MPS_base_functions import coordinate_assign
	from MPS_base_functions import export_values
	from MPS_base_functions import glob_var
	import decimal
	global precision_global
	global time_total_global
	global object_1
	global sequence_time
	global runthrough_number
	global object_properties
	global assigned_objects
	global test_namespaces
	#sets precision for decimal module
	decimal.getcontext().prec = 28
	#-----------#
	#creates decimals from every input
	precision_dec = decimal.Decimal(precision)
	time_total_dec = decimal.Decimal(time_total)
	object_1_posx_dec = decimal.Decimal(object_1_posx)
	object_1_posy_dec = decimal.Decimal(object_1_posy)
	object_1_posz_dec = decimal.Decimal(object_1_posz)
	object_1_xmov_dec = decimal.Decimal(object_1_xmov)
	object_1_ymov_dec = decimal.Decimal(object_1_ymov)
	object_1_zmov_dec = decimal.Decimal(object_1_zmov)
	#-----------#
	#creates variable for testing global namespaces
	test_namespaces = True
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
	object_1 = object_class(object_1_posx_dec, object_1_posy_dec, object_1_posz_dec, object_1_xmov_dec, object_1_ymov_dec, object_1_zmov_dec)
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
			print("assigned_objects: ", assigned_objects_number)
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
		print("After process:", process_number, "\n object 1 is at: ", decimal.Decimal(object_1_coordinates[0]), decimal.Decimal(object_1_coordinates[1]), decimal.Decimal(object_1_coordinates[2]))
		#print("After process:", process_number, "\n object_2 is at: ", decimal.Decimal(object_2_coordinates[0]), decimal.Decimal(object_2_coordinates[1]), decimal.Decimal(object_2_coordinates[2]))
		#print("After process:", process_number, "\n object_3 is at: ", decimal.Decimal(object_3_coordinates[0]), decimal.Decimal(object_3_coordinates[1]), decimal.Decimal(object_3_coordinates[2]))
		#print("After process:", process_number, "\n object_4 is at: ", decimal.Decimal(object_4_coordinates[0]), decimal.Decimal(object_4_coordinates[1]), decimal.Decimal(object_4_coordinates[2]))
		#print("After process:", process_number, "\n object_5 is at: ", decimal.Decimal(object_5_coordinates[0]), decimal.Decimal(object_5_coordinates[1]), decimal.Decimal(object_5_coordinates[2]))
	#-----------#