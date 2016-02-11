def coordinate_assign(new_coordinates, object_number):
	import MPS

	index_number = object_number * 17
	#after full implementation for loop can be added here instead of manual assignment
	MPS.object_properties[index_number + 0] = new_coordinates[0]
	MPS.object_properties[index_number + 1] = new_coordinates[1]
	MPS.object_properties[index_number + 2] = new_coordinates[2]
	if object_number == 1:
		MPS.object_1.data[0] = new_coordinates[0]
		MPS.object_1.data[1] = new_coordinates[1]
		MPS.object_1.data[2] = new_coordinates[2]
		MPS.object_1.update_variables()
	elif object_number == 2:
		#same as above
		print("obj2")
	elif object_number == 3:
		#same as above
		print("obj3")
	elif object_number == 4:
		#same as above
		print("obj4")
	elif object_number == 5:
		#same as above
		print("obj5")

	print("You should never see this. I use this to stop unstable versions from crashing completely")

def export_values(object_number):
	import MPS
	if object_number > 5:
		#--again OSError is just temporary--#
		raise OSError("Object number bejond possibility")
	else:
		object_index = object_number * 17
		if object_number == 1:
			data = MPS.object_1.data
		elif object_number == 2:
			data = MPS.object_2.data
		elif object_number == 3:
			data = MPS.object_3.data
		elif object_number == 4:
			data = MPS.object_4.data
		elif object_number == 5:
			data = MPS.object_5.data
		for variable in range(17):
			index_number = variable + object_index
			MPS.object_properties[index_number] = data[variable]
global glob_var
glob_var = True