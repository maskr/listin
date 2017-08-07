# David Crespo, 2017
import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk
import acciones
class Manejador:
	def __init__(self):
		self.formulario = Ficha()
	def on_boton_quitar_clicked(self, *args):
		operacion = acciones.IO_dbf()
		operacion.eliminar()
	def on_boton_actualizar_clicked(self, *args):
		operacion = acciones.IO_dbf()
		operacion.modificar()
	def on_boton_agregar_clicked(self, *args):
		self.formulario.botones_nueva_ficha()
		self.formulario.limpiar()
	def on_boton_adelante_clicked(self, *args):
		self.formulario.botones_standard()
		maxval=(int(self.formulario.obtener_registros()))
		if self.formulario.obtener_registro() == 'new':
			actual=maxval
		else:
			actual=(int(self.formulario.obtener_registro()))
		if actual >= maxval:
			self.formulario.actualizar(0)
		else:
			self.formulario.actualizar(actual+1)
	def on_boton_atras_clicked(self, *args):
		self.formulario.botones_standard()
		maxval=(int(self.formulario.obtener_registros()))
		if self.formulario.obtener_registro() == 'new':
			actual=maxval
		else:
			actual=(int(self.formulario.obtener_registro()))
		if actual <= 0:
			self.formulario.actualizar(maxval)
		else:
			self.formulario.actualizar(actual-1)
	def on_boton_buscar_clicked(self, *args):
		pass
	def on_boton_importar_clicked(self, *args):
		pass
	def on_boton_salir_clicked(self, *args):
		Gtk.main_quit(*args)
	def on_boton_guardar_clicked(self, *args):
		operacion = acciones.IO_dbf()
		operacion.guarda_formulario()
		
class Ficha:
	constructor=Gtk.Builder()
	constructor.add_from_file("listin.glade")
	ventana = constructor.get_object("ficha")
	listin = constructor.get_object("database")
	entrada_nombre = constructor.get_object("entrada_nombre")
	entrada_apellidos = constructor.get_object("entrada_apellidos")
	entrada_nick1 = constructor.get_object("entrada_nick1")
	entrada_nick2 = constructor.get_object("entrada_nick2")
	entrada_telefono = constructor.get_object("entrada_telefono")
	entrada_telefono2 = constructor.get_object("entrada_telefono2")
	entrada_skype = constructor.get_object("entrada_skype")
	entrada_whatsapp = constructor.get_object("entrada_whatsapp")
	entrada_telegram = constructor.get_object("entrada_telegram")
	entrada_email = constructor.get_object("entrada_email")
	entrada_email2 = constructor.get_object("entrada_email2")
	entrada_calle = constructor.get_object("entrada_calle")
	entrada_puerta = constructor.get_object("entrada_puerta")
	entrada_ciudad = constructor.get_object("entrada_ciudad")
	entrada_provincia = constructor.get_object("entrada_provincia")
	entrada_pais = constructor.get_object("entrada_pais")
	entrada_registros = constructor.get_object("entrada_registros")
	entrada_registro = constructor.get_object("entrada_registro")
	def visualizar_ventana(self):
		self.ventana.show()
	def activar_botones(self):
		self.constructor.connect_signals(Manejador())
	def botones_standard(self):
		activos=("boton_quitar", "boton_agregar", "boton_actualizar", "boton_salir")
		inactivos=("boton_buscar", "boton_importar", "boton_guardar")
		for i in activos:
			boton = self.constructor.get_object(i)
			boton.show()
		for i in inactivos:
			boton = self.constructor.get_object(i)
			boton.hide()
	def botones_nueva_ficha(self):
		activos=("boton_guardar", "boton_salir")
		inactivos=("boton_buscar", "boton_importar", "boton_actualizar", "boton_quitar", "boton_agregar")
		for i in activos:
			boton = self.constructor.get_object(i)
			boton.show()
		for i in inactivos:
			boton = self.constructor.get_object(i)
			boton.hide()
	def obtener_columna(self, dato):
		self.campos={"nombre":0, "apellidos":1, "nick1":2, "nick2":3, "telefono":4, "telefono2":5, "skype":6, "whatsapp":7, "telegram":8, "email":9, "email2":10, "calle":11, "puerta":12, "ciudad":13, "provincia":14, "pais":15}
		return self.campos[dato]
	def obtener_valor(self, fila, dato):
		celda = self.obtener_columna(dato)
		return(self.listin.get_value(self.listin.get_iter(fila), celda))
	def leer_fila(self, fila):
		campos=("nombre", "apellidos", "nick1", "nick2", "telefono", "telefono2", "skype", "whatsapp", "telegram", "email", "email2", "calle", "puerta", "ciudad", "provincia", "pais")
		datos=[]
		for i in campos:
			datos=datos+[self.obtener_valor(fila, i)]
		return(datos)
	def leer(self):
		return self.listin
	def agregar(self, datos):
		self.listin.append(row=datos)
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
	def num_registros(self):
		a = 0
		for i in self.listin:
			a = a + 1
		return a-1
	def borrar_todo(self):
		self.listin.clear()
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
	def obtener(self):
		datos=[self.obtener_nombre()]
		datos=datos+[self.obtener_apellidos()]
		datos=datos+[self.obtener_nick1()]
		datos=datos+[self.obtener_nick2()]
		datos=datos+[self.obtener_telefono()]
		datos=datos+[self.obtener_telefono2()]
		datos=datos+[self.obtener_skype()]
		datos=datos+[self.obtener_whatsapp()]
		datos=datos+[self.obtener_telegram()]
		datos=datos+[self.obtener_email()]
		datos=datos+[self.obtener_email2()]
		datos=datos+[self.obtener_calle()]
		datos=datos+[self.obtener_puerta()]
		datos=datos+[self.obtener_ciudad()]
		datos=datos+[self.obtener_provincia()]
		datos=datos+[self.obtener_pais()]
		return(datos)
	def actualizar(self, fila):
		self.insertar_nombre(self.obtener_valor((fila), "nombre"))
		self.insertar_apellidos(self.obtener_valor((fila), "apellidos"))
		self.insertar_nick1(self.obtener_valor((fila), "nick1"))
		self.insertar_nick2(self.obtener_valor((fila), "nick2"))
		self.insertar_telefono(self.obtener_valor((fila), "telefono"))
		self.insertar_telefono2(self.obtener_valor((fila), "telefono2"))
		self.insertar_skype(self.obtener_valor((fila), "skype"))
		self.insertar_whatsapp(self.obtener_valor((fila), "whatsapp"))
		self.insertar_telegram(self.obtener_valor((fila), "telegram"))
		self.insertar_email(self.obtener_valor((fila), "email"))
		self.insertar_email2(self.obtener_valor((fila), "email2"))
		self.insertar_calle(self.obtener_valor((fila), "calle"))
		self.insertar_puerta(self.obtener_valor((fila), "puerta"))
		self.insertar_ciudad(self.obtener_valor((fila), "ciudad"))
		self.insertar_provincia(self.obtener_valor((fila), "provincia"))
		self.insertar_pais(self.obtener_valor((fila), "pais"))
		self.insertar_registro(fila)
		self.insertar_registros(self.num_registros())
	def limpiar(self):
		self.insertar_nombre("")
		self.insertar_apellidos("")
		self.insertar_nick1("")
		self.insertar_nick2("")
		self.insertar_telefono("")
		self.insertar_telefono2("")
		self.insertar_skype("")
		self.insertar_whatsapp("")
		self.insertar_telegram("")
		self.insertar_email("")
		self.insertar_email2("")
		self.insertar_calle("")
		self.insertar_puerta("")
		self.insertar_ciudad("")
		self.insertar_provincia("")
		self.insertar_pais("")
		self.insertar_registro("new")
		self.insertar_registros(self.num_registros())
	def bucle(self):
		Gtk.main()
