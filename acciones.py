# David Crespo, 2017
import ficha
import fichero

class IO_dbf:
	def __init__(self):
		self.formulario = ficha.Ficha()
		self.databasefile = fichero.Fichero("basedatos.dat")
	def iniciar_formulario(self):
		self.formulario.activar_botones()
		self.formulario.botones_standard()
		self.formulario.visualizar_ventana()
		self.carga()
		self.formulario.bucle()
	def carga(self):
		self.formulario.borrar_todo()
		ficha = []
		fichero=(self.databasefile.leer())
		self.formulario.limpiar()
		for i in fichero:
			dato=(i.strip("\n"))
			if dato==("<siguiente>"):
				self.formulario.agregar(ficha)
				ficha = []
			else:
				nueva_celda = "{}".format(str(dato))
				ficha.append(nueva_celda)
		self.formulario.actualizar(0)
	def guarda_formulario(self):
		form=self.formulario.obtener()
		self.formulario.agregar(form)
		self.formulario.actualizar(0)
		for i in form:
			self.databasefile.agregar(str(i), 0)
		self.databasefile.agregar("<siguiente>\n", 1)
	def eliminar(self):
		seleccion = int(self.formulario.obtener_registro())+1
		self.formulario.eliminar_entrada(seleccion)
		self.formulario.actualizar(0)
		lista = self.formulario.leer()
		self.databasefile.crear()
		for b in lista:
			for i in b:
				self.databasefile.agregar(str(i), 0)
			self.databasefile.agregar("<siguiente>\n", 1)
	def modificar(self):
		form = self.formulario.obtener()
		seleccion = int(self.formulario.obtener_registro())+1
		seleccion=self.formulario.obtener_iter(seleccion)
		a=0
		for i in form:
			self.formulario.modificar(seleccion, a, i)
			a=a+1
		self.formulario.actualizar(0)
		lista = self.formulario.leer()
		self.databasefile.crear()
		for b in lista:
			for i in b:
				self.databasefile.agregar(str(i), 0)
			self.databasefile.agregar("<siguiente>\n", 1)
