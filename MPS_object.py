#MPS object
#
#
#
#
#
#
#
#
#
#!-------- Object Class ---------!#
class object_class():
	def __init__(self, x_pos, y_pos, z_pos, x_movement, y_movement, z_movement, x_rot = 0, y_rot = 0, z_rot = 0, cw = 1, m = 1, density = 1, diameter_x = 1, diameter_y = 1, diameter_z = 1, metal = False, state = "solid"):
		self.data = [x_pos, y_pos, z_pos, x_movement, y_movement, z_movement, x_rot, y_rot, z_rot, cw, m, density, diameter_x, diameter_y, diameter_z, metal, state]
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
		if self.check_data() == "VALID":
			print("All the parameters are valid")
		else:
			#!-- OSError is just a placeholder for the upcoming selfdefined error --!#
			raise OSError("Some parameters are invalid")
		#if more data needs to be included it can easily be added there
	def update_variables(self):
		self.x_pos = self.data[0]
		self.y_pos = self.data[1]
		self.z_pos = self.data[2]
		self.x_movement = self.data[3]
		self.y_movement = self.data[4]
		self.z_movement = self.data[5]
		self.x_rot = self.data[6]
		self.y_rot = self.data[7]
		self.z_rot = self.data[8]
		self.cw = self.data[9]
		self.m = self.data[10]
		self.density = self.data[11]
		self.diameter_x = self.data[12]
		self.diameter_y = self.data[13]
		self.diameter_z = self.data[14]
		self.metal = self.data[15]
		self.state = self.data[16]
	
	def check_data(self):
		self.x_pos_valid = False
		self.y_pos_valid = False
		self.z_pos_valid = False
		self.x_movement_valid = False
		self.y_movement_valid = False
		self.z_movement_valid = False
		self.x_rot_valid = False
		self.y_rot_valid = False
		self.z_rot_valid = False
		self.cw_valid = False
		self.m = False
		self.density_valid = False
		self.diameter_x_valid = False
		self.diameter_y_valid = False
		self.diameter_z_valid = False
		self.metal_valid = False
		self.state_valid = False
		#instead of manual if statements for + if could have been used

		if self.x_pos == float(self.x_pos):
			print("X_POS VALID!")
			self.x_pos_valid = True
		else:
			print("X_POS NOT VALID!")
			self.x_pos_valid = False
		if self.y_pos == float(self.y_pos):
			print("Y_POS VALID!")
			self.y_pos_valid = True
		else:
			print("Y_POS NOT VALID!")
			self.y_pos_valid = False
		if self.z_pos == float(self.z_pos):
			print("Z_POS VALID!")
			self.z_pos_valid = True
		else:
			print("Z_POS NOT VALID!")
			self.z_pos_valid = False
		if self.x_movement == float(self.x_movement):
			print("X_MOVEMENT VALID!")
			self.x_movement_valid = True
		else:
			print("X_MOVEMENT NOT VALID!")
			self.x_movement_valid = False
		if self.y_movement == float(self.y_movement):
			print("Y_MOVEMENT VALID!")
			self.y_movement_valid = True
		else:
			print("Y_MOVEMENT NOT VALID!")
			self.y_movement_valid = False
		if self.z_movement ==float(self.z_movement):
			print("Z_MOVEMENT VALID!")
			self.z_movement_valid = True
		else:
			print("Z_MOVEMENT NOT VALID!")
			self.z_movement_valid = False
		if self.x_rot == float(self.x_rot):
			print("X_ROT VALID!")
			self.x_rot_valid = True
		else:
			print("X_ROT NOT VALID!")
			self.x_rot_valid = False
		if self.y_rot == float(self.y_rot):
			print("Y_ROT VALID!")
			self.y_rot_valid = True
		else:
			print("Y_ROT NOT VALID!")
			self.y_rot_valid = False
		if self.z_rot == float(self.z_rot):
			print("Z_ROT VALID!")
			self.z_rot_valid = True
		else:
			print("Z_ROT NOT VALID!")
			self.z_rot_valid = False
		if self.cw == float(self.cw):
			print("CW VALID!")
			self.cw_valid = True
		else:
			print("CW NOT VALID!")
			self.cw_valid = False
		if self.m == float(self.m):
			print("M VALID!")
			self.m_valid = True
		else:
			print("M NOT VALID!")
			self.m_valid = False
		if self.density == float(self.density):
			print("DENSITY VALID!")
			self.density_valid = True
		else:
			print("DENSITY NOT VALID!")
			self.density_valid = False
		if self.diameter_x == float(self.diameter_x):
			print("DIAMETER_X VALID!")
			self.diameter_x_valid = True
		else:
			print("DIAMETER_X NOT VALID!")
			self.diameter_x_valid = False
		if self.diameter_y == float(self.diameter_y):
			print("DIAMETER_Y VALID!")
			self.diameter_y_valid = True
		else:
			print("DIAMETER_Y NOT VALID!")
			self.diameter_y_valid = False
		if self.diameter_z == float(self.diameter_z):
			print("DIAMETER_Z VALID!")
			self.diameter_z_valid = True
		else:
			print("DIAMETER_Z NOT VALID!")
			self.diameter_z_valid = False
		if self.metal == True:
			print("METAL VALID!")
			self.metal_valid = True
		elif self.metal == False:
			print("METAL VALID!")
			self.metal_valid = True
		else:
			print("METAL NOT VALID!")
			self.metal_valid = False
		if self.state == "solid":
			print("STATE VALID!")
			self.state_valid = True
		elif self.state == "fluid":
			print("STATE VALID!")
			self.state_valid = True
		elif self.state == "gaseous":
			print("STATE VALID!")
			self.state_valid = True
		else:
			print("STATE NOT VALID!")
			self.state_valid = False
		#sum up in list instead it doesnt work
		self.list_valid = [self.x_pos_valid, self.y_pos_valid, self.z_pos_valid, self.x_movement_valid, self.y_movement_valid, self.z_movement_valid, self.x_rot_valid, self.y_rot_valid, self.z_rot_valid, self.cw_valid, self.m_valid, self.density_valid, self.diameter_x_valid, self.diameter_y_valid, self.diameter_z_valid, self.metal_valid, self.state_valid]
		for i in self.list_valid:
			if i == True:
				print("True")
			else:
				return "INVALID"
		else:
			return "VALID"


#!------- Object Class -------!#