# David Crespo, 2017
class Fichero:
	def __init__(self, nombre):
		self.nombre = nombre
	def crear(self):
		fichero = open(self.nombre, 'w')
		fichero.close()
	def leer(self):
		fichero = open (self.nombre, 'r')
		datos = fichero.readlines()
		fichero.close()
		return datos
	def agregar(self, dato, estado):
		fichero = open(self.nombre, "a")
		fichero.write(dato)
		if estado == 0:
			fichero.write("\n")
		else:
			pass
		fichero.close()
	def escribir(self, linea):
		fichero = open(self.nombre, "a")
		fichero.write(linea)
		fichero.write("\n")
		fichero.close()
	def reescribir(self, datos):
		fichero = open(self.nombre, "w")
		fichero.write(datos)
		fichero.close()
