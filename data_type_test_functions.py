#this is my file holding functions that test if an input is a data type.

def IsString(s):
	try:
		str(s)
		return True

	except(TypeError):
		return False

def IsFloat(f):
	try:
		float(f)
		return True

	except(TypeError, ValueError):
		return False

def IsInt(i):
	try:
		int(i)
		return True

	except(TypeError):
		return False