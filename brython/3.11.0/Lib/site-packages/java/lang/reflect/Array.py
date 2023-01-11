from typing import overload as overloaded

class Array(object):
	""" generated source for class Array """
	def __init__(self):
		""" generated source for method __init__ """

	@classmethod
	@overloaded
	def newInstance(cls, componentType, length):
		""" generated source for method newInstance """
		return newArray(componentType, length)

	@classmethod #@newInstance.register(object, Class, A)
	@overloaded
	def newInstance(cls, componentType, *dimensions):
		""" generated source for method newInstance_0 """
		return multiNewArray(componentType, dimensions)

	@classmethod
	def getLength(cls, array):
		""" generated source for method getLength """

	@classmethod
	def get(cls, array, index):
		""" generated source for method get """

	@classmethod
	def getBoolean(cls, array, index):
		""" generated source for method getBoolean """

	@classmethod
	def getByte(cls, array, index):
		""" generated source for method getByte """

	@classmethod
	def getChar(cls, array, index):
		""" generated source for method getChar """

	@classmethod
	def getShort(cls, array, index):
		""" generated source for method getShort """

	@classmethod
	def getInt(cls, array, index):
		""" generated source for method getInt """

	@classmethod
	def getLong(cls, array, index):
		""" generated source for method getLong """

	@classmethod
	def getFloat(cls, array, index):
		""" generated source for method getFloat """

	@classmethod
	def getDouble(cls, array, index):
		""" generated source for method getDouble """

	@classmethod
	def set(cls, array, index, value):
		""" generated source for method set """

	@classmethod
	def setBoolean(cls, array, index, z):
		""" generated source for method setBoolean """

	@classmethod
	def setByte(cls, array, index, b):
		""" generated source for method setByte """

	@classmethod
	def setChar(cls, array, index, c):
		""" generated source for method setChar """

	@classmethod
	def setShort(cls, array, index, s):
		""" generated source for method setShort """

	@classmethod
	def setInt(cls, array, index, i):
		""" generated source for method setInt """

	@classmethod
	def setLong(cls, array, index, l):
		""" generated source for method setLong """

	@classmethod
	def setFloat(cls, array, index, f):
		""" generated source for method setFloat """

	@classmethod
	def setDouble(cls, array, index, d):
		""" generated source for method setDouble """

	@classmethod
	def newArray(cls, componentType, length):
		""" generated source for method newArray """

	@classmethod
	def multiNewArray(cls, componentType, dimensions):
		""" generated source for method multiNewArray """
