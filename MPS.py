#prototype module launcher

#!-------- Object Class ---------!#
class object_class():
	def __init__(self, x_pos, y_pos, z_pos, x_movement, y_movement, z_movement, x_rot = 0, y_rot = 0, z_rot = 0, cw = 1, m = 1, density = 1, diameter_x = 1, diameter_y = 1, diameter_z = 1, metal = False, state = "solid"):
		self.data = [x_pos, y_pos, z_pos, x_movement, y_movement, z_movement, x_rot, y_rot, z_rot, cw, m, density, diamenter_x, diameter_y, diameter_z, metal, state]
		self.x_pos = x_pos
		self.y_pos = y_pos
		self.z_pos = z_pos
		self.x_movement = x_movement
		self.y_movement = y_movement
		self.z_movement = z_movement
		self.x_rot = x_rot
		self.y_rot = y_rot
		self.z_rot = z_rot
		self.cw = cw
		self.m = m
		self.density = density
		self.diameter_x = diameter_x
		self.diameter_y = diameter_y
		self.diameter_z = diameter_z
		self.metal = metal
		self.state = state
		self.check_data()
		#if more data needs to be included it can easily be added there
	def check_data():
		global x_pos_valid
		global y_pos_valid
		global z_pos_valid
		global x_movement_valid
		global y_movement_valid
		global z_movement_valid
		global x_rot_valid
		global y_rot_valid
		global z_rot_valid
		global cw_valid
		global m
		global density_valid
		global diameter_x_valid
		global diameter_y_valid
		global diameter_z_valid
		global metal_valid
		global state_valid
		#instead of manual if statements for + if could have been used

		if x_pos == float(x_pos):
			print("X_POS VALID!")
			x_pos_valid = True
		else:
			print("X_POS NOT VALID!")
			x_pos_valid = False
		if y_pos == float(y_pos):
			print("Y_POS VALID!")
			y_pos_valid = True
		else:
			print("Y_POS NOT VALID!")
			y_pos_valid = False
		if z_pos == float(z_pos):
			print("Z_POS VALID!")
			z_pos_valid = True
		else:
			print("Z_POS NOT VALID!")
			z_pos_valid = False
		if x_movement == float(x_movement):
			print("X_MOVEMENT VALID!")
			x_movement_valid = True
		else:
			print("X_MOVEMENT NOT VALID!")
			x_movement_valid = False
		if y_movement == float(y_movement):
			print("Y_MOVEMENT VALID!")
			y_movement_valid = True
		else:
			print("Y_MOVEMENT NOT VALID!")
			y_movement_valid = False
		if z_movement ==float(z_movement):
			print("Z_MOVEMENT VALID!")
			z_movement_valid = True
		else:
			print("Z_MOVEMENT NOT VALID!")
			z_movement_valid = False
		if x_rot == float(x_rot):
			print("X_ROT VALID!")
			x_rot_valid = True
		else:
			print("X_ROT NOT VALID!")
			x_rot_valid = False
		if y_rot == float(y_rot):
			print("Y_ROT VALID!")
			y_rot_valid = True
		else:
			print("Y_ROT NOT VALID!")
			y_rot_valid = False
		if z_rot == float(z_rot):
			print("Z_ROT VALID!")
			z_rot_valid = True
		else:
			print("Z_ROT NOT VALID!")
			z_rot_valid = False
		if cw == float(cw):
			print("CW VALID!")
			cw_valid = True
		else:
			print("CW NOT VALID!")
			cw_valid = False
		if m == float(m):
			print("M VALID!")
			m_valid = True
		else:
			print("M NOT VALID!")
			m_valid = False
		if density == float(density):
			print("DENSITY VALID!")
			density_valid = True
		else:
			print("DENSITY NOT VALID!")
			density_valid = False
		if diameter_x == float(diameter_x):
			print("DIAMETER_X VALID!")
			diameter_x_valid = True
		else:
			print("DIAMETER_X NOT VALID!")
			diameter_x_valid = False
		if diameter_y == float(diameter_y):
			print("DIAMETER_Y VALID!")
			diameter_y_valid = True
		else:
			print("DIAMETER_Y NOT VALID!")
			diameter_y_valid = False
		if diameter_z == float(diameter_z):
			print("DIAMETER_Z VALID!")
			diameter_z_valid = True
		else:
			print("DIAMETER_Z NOT VALID!")
			diameter_z_valid = False
		if metal == True:
			print("METAL VALID!")
			metal_valid = True
		elif metal == False:
			print("METAL VALID!")
			metal_valid = True
		else:
			print("METAL NOT VALID!")
			metal_valid = False
		if state == "solid":
			print("STATE VALID!")
			state_valid = True
		elif state == "fluid":
			print("STATE VALID!")
			state_valid = True
		elif state == "gaseous":
			print("STATE VALID!")
			state_valid = True
		else:
			print("STATE NOT VALID!")
			state_valid = False
		#sum up in list instead it doesnt work
		return x_pos_valid
		return y_pos_valid
		return z_pos_valid
		return x_movement_valid
		return y_movement_valid
		return z_movement_valid
		return x_rot_valid
		return y_rot_valid
		return z_rot_valid
		return cw_valid
		return m
		return density_valid
		return diameter_x_valid
		return diameter_y_valid
		return diameter_z_valid
		return metal_valid
		return state_valid

#!------- Object Class -------!#
#!main launcher module!#
#!---need to add leftover parameters---!#
def MPS(precision, time_runthrough, object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov):
	import MS_modules
	global precision
	global time_runthrough
	global object_1
	object_1 = object_class(object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov)
	negative_precision = 0-precision
	sequence_time = 10**negative_precision
	sequence_movement = [False, False, False]
	#---!sets movement per calculation process according to precision!---#
	for i ín range(3):
		sequence_movement[i] = movement[i] * sequence_time