#main module launcher module
#
#
#
#
#
#
#
#
#
def MPS(precision, time_total, object_1_posx, object_1_posy, object_1_posz, object_1_xmov, object_1_ymov, object_1_zmov):
	import MPS_object
	import MPS_modules
	import decimal 
	#creates needed presets for MPS to work
	decimal.getcontext().prec = 28
	assigned_objects = 0
	negative_precision = 0 - precision
	sequence_time = 10**negative_precision
	#!
	object_1 = object_class(object_1_posx_dec, object_1_posy_dec, object_1_posz_dec, object_1_xmov_dec, object_1_ymov_dec, object_1_zmov_dec)
