import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
class Manejador:
	def on_boton_quitar_clicked(self, *args):
		databaseio.eliminar()
	def on_boton_actualizar_clicked(self, *args):
		databaseio.modificar()
	def on_boton_agregar_clicked(self, *args):
		databaseio.guarda_formulario()
	def on_boton_adelante_clicked(self, *args):
		fila.positivo()
		formulario.actualizar(fila.posicion_actual())
	def on_boton_atras_clicked(self, *args):
		fila.negativo()
		formulario.actualizar(fila.posicion_actual())
	def on_boton_buscar_clicked(self, *args):
		pass
	def on_boton_importar_clicked(self, *args):
		pass
	def on_boton_salir_clicked(self, *args):
		Gtk.main_quit(*args)
class Entradas:
	def __init__(self):
		self.entrada_nombre = constructor.get_object("entrada_nombre")
		self.entrada_apellidos = constructor.get_object("entrada_apellidos")
		self.entrada_nick1 = constructor.get_object("entrada_nick1")
		self.entrada_nick2 = constructor.get_object("entrada_nick2")
		self.entrada_telefono = constructor.get_object("entrada_telefono")
		self.entrada_telefono2 = constructor.get_object("entrada_telefono2")
		self.entrada_skype = constructor.get_object("entrada_skype")
		self.entrada_whatsapp = constructor.get_object("entrada_whatsapp")
		self.entrada_telegram = constructor.get_object("entrada_telegram")
		self.entrada_email = constructor.get_object("entrada_email")
		self.entrada_email2 = constructor.get_object("entrada_email2")
		self.entrada_calle = constructor.get_object("entrada_calle")
		self.entrada_puerta = constructor.get_object("entrada_puerta")
		self.entrada_ciudad = constructor.get_object("entrada_ciudad")
		self.entrada_provincia = constructor.get_object("entrada_provincia")
		self.entrada_pais = constructor.get_object("entrada_pais")
		self.entrada_registros = constructor.get_object("entrada_registros")
		self.entrada_registro = constructor.get_object("entrada_registro")
	def insertar_nombre(self, mensaje):
		self.entrada_nombre.set_text(mensaje)
	def obtener_nombre(self):
		return (self.entrada_nombre.get_text())
	def insertar_apellidos(self, mensaje):
		self.entrada_apellidos.set_text(mensaje)
	def obtener_apellidos(self):
		return(self.entrada_apellidos.get_text())
	def insertar_nick1(self, mensaje):
		self.entrada_nick1.set_text(mensaje)
	def obtener_nick1(self):
		return(self.entrada_nick1.get_text())
	def insertar_nick2(self, mensaje):
		self.entrada_nick2.set_text(mensaje)
	def obtener_nick2(self):
		return(self.entrada_nick2.get_text())
	def insertar_telefono(self, mensaje):
		self.entrada_telefono.set_text(mensaje)
	def obtener_telefono(self):
		return(self.entrada_telefono.get_text())
	def insertar_telefono2(self, mensaje):
		self.entrada_telefono2.set_text(mensaje)
	def obtener_telefono2(self):
		return (self.entrada_telefono2.get_text())
	def insertar_skype(self, mensaje):
		self.entrada_skype.set_text(mensaje)
	def obtener_skype(self):
		return(self.entrada_skype.get_text())
	def insertar_whatsapp(self, mensaje):
		self.entrada_whatsapp.set_text(mensaje)
	def obtener_whatsapp(self):
		return(self.entrada_whatsapp.get_text())
	def insertar_telegram(self, mensaje):
		self.entrada_telegram.set_text(mensaje)
	def obtener_telegram(self):
		return(self.entrada_telegram.get_text())
	def insertar_email(self, mensaje):
		self.entrada_email.set_text(mensaje)
	def obtener_email(self):
		return(self.entrada_email.get_text())
	def insertar_email2(self, mensaje):
		self.entrada_email2.set_text(mensaje)
	def obtener_email2(self):
		return(self.entrada_email2.get_text())
	def insertar_calle(self, mensaje):
		self.entrada_calle.set_text(mensaje)
	def obtener_calle(self):
		return(self.entrada_calle.get_text())
	def insertar_puerta(self, mensaje):
		self.entrada_puerta.set_text(mensaje)
	def obtener_puerta(self):
		return(self.entrada_puerta.get_text())
	def insertar_ciudad(self, mensaje):
		self.entrada_ciudad.set_text(mensaje)
	def obtener_ciudad(self):
		return(self.entrada_ciudad.get_text())
	def insertar_provincia(self, mensaje):
		self.entrada_provincia.set_text(mensaje)
	def obtener_provincia(self):
		return(self.entrada_provincia.get_text())
	def insertar_pais(self, mensaje):
		self.entrada_pais.set_text(mensaje)
	def obtener_pais(self):
		return(self.entrada_pais.get_text())
	def insertar_registros(self, mensaje):
		self.entrada_registros.set_text(str(mensaje))
	def obtener_registros(self):
		return(self.entrada_registros.get_text())
	def insertar_registro(self, mensaje):
		self.entrada_registro.set_text(str(mensaje))
	def obtener_registro(self):
		return(self.entrada_registro.get_text())
class Listin:
	def __init__(self):
		self.listin = constructor.get_object("database")
	def obtener_columna(self, dato):
		self.campos={"nombre":0, "apellidos":1, "nick1":2, "nick2":3, "telefono":4, "telefono2":5, "skype":6, "whatsapp":7, "telegram":8, "email":9, "email2":10, "calle":11, "puerta":12, "ciudad":13, "provincia":14, "pais":15}
		return self.campos[dato]
	def leer_fila(self, fila):
		campos=("nombre", "apellidos", "nick1", "nick2", "telefono", "telefono2", "skype", "whatsapp", "telegram", "email", "email2", "calle", "puerta", "ciudad", "provincia", "pais")
		datos=[]
		for i in campos:
			datos=datos+[self.obtener_valor(fila, i)]
		return(datos)
	def obtener_valor(self, fila, dato):
		celda = self.obtener_columna(dato)
		return(self.listin.get_value(self.listin.get_iter(fila), celda))
	def agregar(self, datos):
		self.listin.append(row=datos)
	def leer(self):
		return self.listin
	def modificar(self, registro, columna, valor):
		self.listin.set_value(registro, columna, valor)
	def obtener_iter(self, seleccion):
		seleccion = int(seleccion) -1
		registro=self.listin.get_iter(seleccion)
		return(registro)
	def eliminar_entrada(self, seleccion):
		seleccion = int(seleccion) -1
		registro=self.listin.get_iter(seleccion)
		self.listin.remove(registro)
	def obtener_posicion_por_nombre(self, nombre):
		a = 0
		for i in self.listin:
			if self.listin.get_value(self.listin.get_iter(a), 1)==nombre:
				return a
			else:
				a = a + 1
	def num_registros(self):
		a = 0
		for i in self.listin:
			a = a + 1
		return a
	def limpiar(self):
		self.listin.clear()
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
class IO_dbf:
	def carga(self):
		ficha = []
		fichero=(database.leer())
		listadatos.limpiar()
		for i in fichero:
			dato=(i.strip("\n"))
			if dato==("<siguiente>"):
				listadatos.agregar(ficha)
				ficha = []
			else:
				nueva_celda = "{}".format(str(dato))
				ficha.append(nueva_celda)
		maxreg=listadatos.num_registros()
		fila.valor_max(maxreg)
		formulario.actualizar(0)
	def guarda_formulario(self):
		form=formulario.obtener()
		listadatos.agregar(form)
		formulario.actualizar(0)
		maxreg=listadatos.num_registros()
		fila.valor_max(maxreg)
		for i in form:
			database.agregar(str(i), 0)
		database.agregar("<siguiente>\n", 1)
	def eliminar(self):
		seleccion = entrada.obtener_registro()
		listadatos.eliminar_entrada(seleccion)
		maxreg=listadatos.num_registros()
		fila.valor_max(maxreg)
		formulario.actualizar(0)
		lista = listadatos.leer()
		database.crear()
		for b in lista:
			for i in b:
				database.agregar(str(i), 0)
			database.agregar("<siguiente>\n", 1)
	def modificar(self):
		form = formulario.obtener()
		seleccion = entrada.obtener_registro()
		seleccion=listadatos.obtener_iter(seleccion)
		a=0
		for i in form:
			listadatos.modificar(seleccion, a, i)
			a=a+1
		maxreg=listadatos.num_registros()
		fila.valor_max(maxreg)
		formulario.actualizar(0)
		lista = listadatos.leer()
		database.crear()
		for b in lista:
			for i in b:
				database.agregar(str(i), 0)
			database.agregar("<siguiente>\n", 1)
class Posicion:
	def __init__(self):
		self.fila=0
		self.max_fila=0
	def valor_max(self, valor):
		self.max_fila=valor
	def obtener_valor_max(self):
		return(self.max_fila)
	def positivo(self):
		if self.fila>=self.obtener_valor_max()-1:
			self.fila=0
		else:
			self.fila=self.fila + 1
	def negativo(self):
		if self.fila<=0:
			self.fila=self.obtener_valor_max()-1
		else:
			self.fila=self.fila -1
	def posicion_actual(self):
		return(self.fila)
class Formulario:
	def obtener(self):
		datos=[entrada.obtener_nombre()]
		datos=datos+[entrada.obtener_apellidos()]
		datos=datos+[entrada.obtener_nick1()]
		datos=datos+[entrada.obtener_nick2()]
		datos=datos+[entrada.obtener_telefono()]
		datos=datos+[entrada.obtener_telefono2()]
		datos=datos+[entrada.obtener_skype()]
		datos=datos+[entrada.obtener_whatsapp()]
		datos=datos+[entrada.obtener_telegram()]
		datos=datos+[entrada.obtener_email()]
		datos=datos+[entrada.obtener_email2()]
		datos=datos+[entrada.obtener_calle()]
		datos=datos+[entrada.obtener_puerta()]
		datos=datos+[entrada.obtener_ciudad()]
		datos=datos+[entrada.obtener_provincia()]
		datos=datos+[entrada.obtener_pais()]
		return(datos)
	def actualizar(self, fila):
		entrada.insertar_nombre(listadatos.obtener_valor((fila), "nombre"))
		entrada.insertar_apellidos(listadatos.obtener_valor((fila), "apellidos"))
		entrada.insertar_nick1(listadatos.obtener_valor((fila), "nick1"))
		entrada.insertar_nick2(listadatos.obtener_valor((fila), "nick2"))
		entrada.insertar_telefono(listadatos.obtener_valor((fila), "telefono"))
		entrada.insertar_telefono2(listadatos.obtener_valor((fila), "telefono2"))
		entrada.insertar_skype(listadatos.obtener_valor((fila), "skype"))
		entrada.insertar_whatsapp(listadatos.obtener_valor((fila), "whatsapp"))
		entrada.insertar_telegram(listadatos.obtener_valor((fila), "telegram"))
		entrada.insertar_email(listadatos.obtener_valor((fila), "email"))
		entrada.insertar_email2(listadatos.obtener_valor((fila), "email2"))
		entrada.insertar_calle(listadatos.obtener_valor((fila), "calle"))
		entrada.insertar_puerta(listadatos.obtener_valor((fila), "puerta"))
		entrada.insertar_ciudad(listadatos.obtener_valor((fila), "ciudad"))
		entrada.insertar_provincia(listadatos.obtener_valor((fila), "provincia"))
		entrada.insertar_pais(listadatos.obtener_valor((fila), "pais"))
		entrada.insertar_registro(fila+1)
		entrada.insertar_registros(listadatos.num_registros())

constructor = Gtk.Builder()
constructor.add_from_file("listin.glade")
constructor.connect_signals(Manejador())
ventana = constructor.get_object("ficha")
boton_buscar = constructor.get_object("boton_buscar")
boton_importar = constructor.get_object("boton_importar")
fila = Posicion()
nombre_database = "basedatos.dat"
database = Fichero(nombre_database)
databaseio = IO_dbf()
listadatos = Listin()
listadatos.leer_fila(0)
entrada = Entradas()
fila.valor_max(listadatos.num_registros())
formulario = Formulario()
formulario.actualizar(fila.posicion_actual())
log = Fichero("listin.log")
log.crear()
log.escribir("Lista de objetos cargados.")
for i in (constructor.get_objects()):
	log.escribir(str(i))
log.escribir("Accediendo a la base de datos.")
databaseio.carga()
ventana.show_all()
boton_buscar.hide()
boton_importar.hide()
Gtk.main()

