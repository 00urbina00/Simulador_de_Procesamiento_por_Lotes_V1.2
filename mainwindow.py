import random
import threading
import time

from lote_procesos import Lote

from PySide2.QtWidgets import QMainWindow, QPushButton, QLineEdit, QPlainTextEdit, QSpinBox, QFrame, QLabel
from PySide2.QtCore import QTimer
from proceso import *
from ui_mainwindow import Ui_MainWindow


def crea_proceso(operadores, tiempos, numero_programa):  # Aleatorio
    operador = random.choice(operadores)
    operando_a = random.randint(0, 1000)
    operando_b = random.randint(0, 1000)
    tiempo = str(random.choice(tiempos))
    return Proceso(operador, operando_a, operando_b, tiempo, numero_programa)


def not_num(num):
    try:
        float(num)
        return False
    except ValueError:
        print("No es un numero")
        return True


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowTitle("Simulador de procesos")
        self.continuar = False
        self.en_ejecucion = False
        # (creacion de proceso automaticos)
        # Lista de operadores aritméticos
        self.operadores = ['+', '-', '*', '/', '%', "%%"]
        # lista de tiempos a elegir 
        self.tiempo_proceso = [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
        self.id_proceso = -1
        self.tiempo_global = 0
        # Colas de procesos
        self.cola_de_lotes_inicio = []
        self.procesos_inicio = []
        self.cola_de_lotes_terminados = []

        self.num_lote = 1

        # Hilo de ejecucion
        self.hilo = None
        # Timer de actualziacion de la interfaz
        # Crear un QTimer para actualizar la interfaz cada 1 segundo
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.actualizar_interfaz)
        self.timer.start(1000)  # Intervalo en milisegundos (1 segundo)
        # Actualizacion datos de la interfaz:
        self.texto_lote_actual = "Sin lotes pendientes."
        self.texto_lotes_en_ejecucion = "Sin lotes a ejecutar."
        self.texto_lotes_terminados = "No hay lotes terminados."
        self.texto_lotes_pendientes = "0"
        self.texto_procesos_pendientes = "0"
        self.texto_tiempo_global = "0"
        self.bandera_limpiar_campos = False
        self.bandera_proceso_automatico = True

        self.bandera_i = False
        self.bandera_e = False
        self.bandera_p = False
        self.bandera_c = False

        self.bandera_detener = False  # Bandera para truncar la continuacion del programa

        # Definir los widgets

        # Label
        self.label_ejecucion = self.findChild(QLabel, "lb_pausa")

        # Boton
        self.btn_iniciar = self.findChild(QPushButton, "pb_iniciar")
        self.btn_agregar = self.findChild(QPushButton, "pb_agregar")
        self.btn_habilitar_capturar_proceso = self.findChild(QPushButton, "pb_capturar_procesos")
        self.btn_agregar_procesos = self.findChild(QPushButton, "pb_agregar_procesos")
        self.btn_limpiar = self.findChild(QPushButton, "btn_limpiar")
        # PlainTextEdit
        self.pte_lote_actual = self.findChild(QPlainTextEdit, "pte_lote_actual")
        self.pte_ejecucion = self.findChild(QPlainTextEdit, "pte_ejecucion")
        self.pte_terminados = self.findChild(QPlainTextEdit, "pte_terminados")
        # LineEdit
        # Entrada
        self.le_tiempo_max = self.findChild(QLineEdit, "le_tiempo_max")
        self.le_operador = self.findChild(QLineEdit, "le_operador")
        self.le_operando_a = self.findChild(QLineEdit, "le_operando_a")
        self.le_operando_b = self.findChild(QLineEdit, "le_operando_b")
        # Salida
        self.le_lotes = self.findChild(QLineEdit, "le_lotes")
        self.le_numero_procesos = self.findChild(QLineEdit, "le_numero_procesos")
        self.le_tiempo_global = self.findChild(QLineEdit, "le_tiempo_global")

        # Spinbox numero de procesos
        self.sb_num_procesos = self.findChild(QSpinBox, "sb_num_procesos")
        # Frame captura de datos
        self.frame_captura = self.findChild(QFrame, "frame_7")
        self.habilitar_campos()

        # Eventos

        # Habilitar / Deshabilitar frame
        self.btn_habilitar_capturar_proceso.clicked.connect(self.habilitar_campos)
        # Ejecutar el simulador
        self.btn_iniciar.clicked.connect(self.back_end)
        # Agregar proceso
        self.btn_agregar.clicked.connect(self.agregar_proceso)
        self.btn_agregar_procesos.clicked.connect(self.agregar_proceso)
        # Limpiar consolas
        self.btn_limpiar.clicked.connect(self.limpiar)

    # Funciones
    # -----------------------------------------------------------------------------------
    def limpiar(self):
        if not self.en_ejecucion:
            # Liberar memoria de lotes antiguos
            for lote in self.cola_de_lotes_terminados:
                lote.clear()
            self.cola_de_lotes_terminados.clear()
            # Limpiar los paneles
            self.texto_lote_actual = "Sin lotes pendientes."
            self.texto_lotes_en_ejecucion = "Sin lotes a ejecutar."
            self.texto_lotes_terminados = "No hay lotes terminados."
        else:
            print("Proceso en ejecucion")

    def closeEvent(self, event):  # Detectar si se va a cerrar el programa y protegerlo
        if self.en_ejecucion:
            self.bandera_detener = True
            print("Se canceló la ejecución del programa.")
            event.ignore()  # Evita que la ventana se cierre
        else:
            event.accept()  # Permite que la ventana se cierre

    def keyPressEvent(self, event):
        texto_tecla = str(event.text())
        if texto_tecla == 'i':
            print("Interrupcion")
            self.bandera_i = True
        elif texto_tecla == 'e':
            print("Error")
            self.bandera_e = True
        elif texto_tecla == 'p':
            self.label_ejecucion.setText("Pausa")
            self.label_ejecucion.setStyleSheet("color: red;")
            print("Pausa")
            self.bandera_p = True
        elif texto_tecla == 'c':
            self.label_ejecucion.setText("Ejecución")
            self.label_ejecucion.setStyleSheet("color: green;")
            print("Continuar")
            self.bandera_p = False

    def crear_lotes_de_procesos(self, cola_de_lotes, procesos):
        lote_actual = Lote(self.num_lote)
        cola_de_lotes.append(lote_actual)
        for proceso in procesos:
            if not lote_actual.agregar_proceso(proceso):
                self.num_lote += 1
                lote_actual = Lote(self.num_lote)
                cola_de_lotes.append(lote_actual)
                lote_actual.agregar_proceso(proceso)

    def habilitar_campos(self):
        if self.frame_captura.isEnabled():
            # Si está habilitado, deshabilitarlo
            self.frame_captura.setEnabled(False)
            self.bandera_proceso_automatico = True
        else:
            # Si está deshabilitado, habilitarlo
            self.frame_captura.setEnabled(True)
            self.bandera_proceso_automatico = False

    def actualizar_interfaz(self):
        # Esta función se llama cada vez que el QTimer se dispara
        self.pte_lote_actual.setPlainText(self.texto_lote_actual)
        self.pte_ejecucion.setPlainText(self.texto_lotes_en_ejecucion)
        self.pte_terminados.setPlainText(self.texto_lotes_terminados)
        self.le_lotes.setText(self.texto_lotes_pendientes)  # Lotes pendientes
        self.le_numero_procesos.setText(self.texto_procesos_pendientes)  # Procesos pendientes
        self.le_tiempo_global.setText(self.texto_tiempo_global)  # Tiempo global
        if self.bandera_limpiar_campos:
            print("Limpiando campos")
            self.le_tiempo_max.clear()
            self.le_operador.clear()
            self.le_operando_a.clear()
            self.le_operando_b.clear()
            self.bandera_limpiar_campos = False

    def iniciar_hilo(self):
        if not self.en_ejecucion and self.procesos_inicio:
            self.en_ejecucion = True
            self.hilo = threading.Thread(target=self.correr_interfaz)
            self.hilo.start()
        elif not self.en_ejecucion and self.bandera_proceso_automatico:
            self.en_ejecucion = True
            self.hilo = threading.Thread(target=self.correr_interfaz)
            self.hilo.start()
        elif self.en_ejecucion:
            print("El hilo ya está en ejecución")
        else:
            print("Sin procesos a ejecutar")

    def detener_hilo(self):
        if self.en_ejecucion:
            self.en_ejecucion = False
            # self.hilo.join()  # Espera a que el hilo termine de manera ordenada
        else:
            print("El hilo no está en ejecución")

    def esperar_hilo(self):
        if self.hilo:
            self.hilo.join()

    def back_end(self):
        self.texto_procesos_pendientes = str(len(self.procesos_inicio))
        self.texto_lotes_pendientes = str(len(self.cola_de_lotes_inicio))
        if not self.en_ejecucion:
            self.esperar_hilo()
            self.iniciar_hilo()
        else:
            print("En ejecución")

    def correr_interfaz(self):
        if self.procesos_inicio:
            self.crear_lotes_de_procesos(self.cola_de_lotes_inicio, self.procesos_inicio)
            self.texto_procesos_pendientes = str(len(self.procesos_inicio))
            self.texto_lotes_pendientes = str(len(self.cola_de_lotes_inicio))
            self.procesar_lotes()
        else:
            self.en_ejecucion = False

    def captura_proceso(self) -> Proceso:
        operador = self.le_operador.text()
        operando_a = float(self.le_operando_a.text())
        operando_b = float(self.le_operando_b.text())
        tiempo = int(self.le_tiempo_max.text())
        self.id_proceso += 1
        return Proceso(operador, operando_a, operando_b, tiempo, self.id_proceso)

    def crea_procesos(self, num_procesos):
        while num_procesos > 0:
            self.id_proceso += 1
            proceso = crea_proceso(self.operadores, self.tiempo_proceso, self.id_proceso)
            self.procesos_inicio.append(proceso)
            num_procesos -= 1

    def procesar_lotes(self):
        self.texto_lotes_pendientes = str(len(self.cola_de_lotes_inicio))
        while self.cola_de_lotes_inicio and not self.bandera_detener:  # La cola de lotes aun tiene lotes
            lote = self.cola_de_lotes_inicio.pop(0)  # Lo te completo
            self.texto_lotes_pendientes = str(len(self.cola_de_lotes_inicio))
            self.formato_texto_lote_actual(lote)
            while True and not self.bandera_detener:
                proceso = lote.saca_proceso()  # Sale proceso del lote
                if proceso is not None:  # El lote actual está vacio?
                    self.formato_texto_lotes_en_ejecucion(proceso)
                    if proceso in self.procesos_inicio:  # El proceso está en la lista de procesos aún
                        self.procesos_inicio.remove(proceso)  # Eliminar proceso de la lista
                    self.le_numero_procesos.setText(
                        str(len(self.procesos_inicio)))  # Actualizar número de procesos en interfaz
                    if proceso is not None:
                        tiempo = int(proceso.get_tiempo_restante())
                        t_funcion = tiempo
                        for i in range(tiempo):  # Se crea un bucle en funcion al tiempo del proceso
                            while self.bandera_p and not self.bandera_detener:
                                pass
                            if self.bandera_detener:
                                break
                            elif self.bandera_i:
                                self.bandera_i = False
                                lote.agregar_proceso(proceso)
                                break
                            elif self.bandera_e:
                                proceso.set_resultado(-1)
                                proceso.set_terminado()
                                self.inserta_proceso_terminado(proceso, lote.get_num_lote())
                                self.formato_texto_lotes_en_ejecucion(proceso)
                                self.formato_texto_procesos_terminados(lote, proceso)
                                print("Proceso con error")
                                self.bandera_e = False
                                break
                            else:
                                t_funcion -= 1
                                print("Tiempo restante: " + proceso.get_tiempo_restante())
                                lote.transcurre_tiempo()
                                self.formato_texto_lote_actual(lote)
                                self.formato_texto_lotes_en_ejecucion(proceso)
                                time.sleep(1)  # Simula el tiempo del proceso
                                proceso.segundo_transcurrido()  # Incrementa el tiempo transcurrido en 1
                                self.tiempo_global += 1
                                self.texto_tiempo_global = str(self.tiempo_global)
                                self.texto_procesos_pendientes = str(len(self.procesos_inicio))
                        if proceso.get_tiempo_transcurrido() == proceso.get_tiempo():
                            print("Proceso terminado")
                            proceso.ejecutar()
                            proceso.set_terminado()
                            self.inserta_proceso_terminado(proceso, lote.get_num_lote())
                            self.formato_texto_lotes_en_ejecucion(proceso)
                            self.formato_texto_procesos_terminados(lote, proceso)
                else:
                    break
        self.texto_lote_actual = "No hay lotes pendientes."
        self.le_numero_procesos.setText(str(len(self.procesos_inicio)))
        self.detener_hilo()
        self.bandera_detener = False
        print("Se terminaron todos los procesos!")

    def inserta_proceso_terminado(self, proceso, num_lote):
        if not self.cola_de_lotes_terminados:
            lote = Lote(num_lote)
        if not lote.agregar_proceso(proceso):  # Se intenta agrega el proceso en lote
            self.cola_de_lotes_terminados.append(lote)  # Se agrega el lote a la cola de terminados

    # Validaciones de campos de la interfaz

    def campos_validos(self) -> bool:  # Campo vacio
        if (self.le_tiempo_max.text() == "" or self.le_operador.text() not in self.operadores
                or self.le_operando_a.text() == "" or
                self.le_operando_b.text() == "" or not_num(self.le_operando_a.text()) or
                not_num(self.le_operando_b.text()) or (self.le_operador.text() == '/' and
                                                       self.le_operando_b.text() == '0') or (
                        self.le_operador.text() == '%%' and self.le_operando_b.text() == '0')):
            return False
        elif 0 < int(self.le_tiempo_max.text()) <= 10:  # 0 < tiempo <= 10
            numero = self.id_proceso + 1
            if any(proceso.get_id() == numero for proceso in self.procesos_inicio):  # ID existente
                return False
            else:
                return True
        else:
            return False

    def agregar_proceso(self):
        if not self.bandera_proceso_automatico:
            if self.campos_validos():
                proceso = self.captura_proceso()
                self.procesos_inicio.append(proceso)
                self.bandera_limpiar_campos = True
                self.texto_procesos_pendientes = str(len(self.procesos_inicio))
            # "PEGRILOSO" modificar interfaz desde hilo
            elif self.le_tiempo_max.text() == "":
                self.le_tiempo_max.setText("Llene el campo con sus datos!")
            elif self.le_operador.text() == "":
                self.le_operador.setText("Llene el campo con sus datos!")
            elif self.le_operador.text() not in self.operadores:
                self.le_operador.setText("Llene el campo con sus datos!")
            elif self.le_operando_a.text() == "":
                self.le_operando_a.setText("Llene el campo con sus datos!")
            elif self.le_operando_a.text() == "0" or not_num(self.le_operando_a.text()):
                self.le_operando_a.setText("NUM ERR")
            elif self.le_operando_b.text() == "":
                self.le_operando_b.setText("Llene el campo con sus datos!")
            elif self.le_operando_b.text() == "0" or not_num(self.le_operando_b.text()):
                self.le_operando_b.setText("DIV 0/NUM")
            else:
                self.le_nombre_prog.setText("Hay algún error de captura")
        else:
            numero_procesos = self.sb_num_procesos.value()
            print("Numero de procesos: " + str(numero_procesos))
            self.crea_procesos(numero_procesos)
            self.texto_procesos_pendientes = str(len(self.procesos_inicio))

    def formato_texto_lote_actual(self, lote):
        # Definir encabezados para el lote
        encabezados_lote = ["ID", "TME", "TT"]

        # Definir datos para el lote
        datos_lote = [str(lote.get_num_lote()), str(lote.get_tiempo_maximo()), str(lote.get_tiempo_transcurrido())]

        # Longitud máxima para cada columna (ajusta según tus necesidades)
        longitud_columna = 21  # Cambia este valor según tus preferencias
        formato_columna = f"{{:^{longitud_columna}}}"

        # Construir una lista de líneas para la tabla
        lineas_tabla = []

        # Encabezados del lote
        linea_encabezado_lote = " | ".join([formato_columna.format(encabezado) for encabezado in encabezados_lote])
        lineas_tabla.append(linea_encabezado_lote)

        # Datos del lote
        linea_datos_lote = " | ".join([formato_columna.format(valor) for valor in datos_lote])
        lineas_tabla.append(linea_datos_lote)

        # Línea de separación para el lote
        linea_separacion_lote = "-" * (longitud_columna * len(encabezados_lote) + len(encabezados_lote) - 1)
        lineas_tabla.append(linea_separacion_lote)

        # Encabezados para los procesos en ejecución
        encabezados_procesos = ["IDP", "TMEP", "TT"]
        linea_encabezado_procesos = " | ".join(
            [formato_columna.format(encabezado) for encabezado in encabezados_procesos])
        lineas_tabla.append(linea_encabezado_procesos)

        # Datos de los procesos en ejecución
        procesos = lote.get_procesos()
        for proceso in procesos:
            linea_datos_proceso = " | ".join(
                [formato_columna.format(proceso.get_id()), formato_columna.format(proceso.get_tiempo()),
                 formato_columna.format(proceso.get_tiempo_transcurrido())])
            lineas_tabla.append(linea_datos_proceso)

        # Unir todas las líneas en una sola cadena
        tabla_completa = "\n".join(lineas_tabla)
        self.texto_lote_actual = tabla_completa

    def formato_texto_lotes_en_ejecucion(self, proceso):
        # Definir encabezados
        encabezados = [" ID", "Ope", "TME", " TT", " TR"]
        # Definir datos como una lista de listas (ajusta según tus necesidades)
        datos = [
            [str(proceso.get_id()), str(proceso.get_operacion()),
             str(proceso.get_tiempo()), str(proceso.get_tiempo_transcurrido()), str(proceso.get_tiempo_restante())]
        ]
        # Longitud máxima para cada columna (ajusta según tus necesidades)
        longitud_columna = 17  # Cambia este valor según tus preferencias
        # Crear una cadena de formato fija para centrar cada columna
        formato_columna = f"{{:^{longitud_columna}}}"
        # Construir una lista de líneas para la tabla
        lineas_tabla = []
        # Encabezados
        linea_encabezado = " | ".join([formato_columna.format(encabezado) for encabezado in encabezados])
        lineas_tabla.append(linea_encabezado)
        # Línea de separación
        linea_separacion = "-" * (longitud_columna * len(encabezados) + len(encabezados) - 1)
        lineas_tabla.append(linea_separacion)
        # Datos
        for fila in datos:
            linea_datos = " | ".join([formato_columna.format(valor) for valor in fila])
            lineas_tabla.append(linea_datos)
        # Unir todas las líneas en una sola cadena
        tabla_completa = "\n".join(lineas_tabla)
        self.texto_lotes_en_ejecucion = tabla_completa

    def formato_texto_procesos_terminados(self, lote, proceso):
        # Definir encabezados
        encabezados = [" IDL", " IDP", " OA", " Ope", " OB", " Res"]
        # Longitud máxima para cada columna (ajusta según tus necesidades)
        longitud_columna = 13  # Cambia este valor según tus preferencias
        # Crear una cadena de formato fija para centrar cada columna
        formato_columna = f"{{:^{longitud_columna}}}"
        # Construir una lista de líneas para la tabla
        lineas_tabla = []

        if self.texto_lotes_terminados == "No hay lotes terminados.":
            # Si es la primera vez que se agrega, imprimir el encabezado
            linea_encabezado = " | ".join([formato_columna.format(encabezado) for encabezado in encabezados])
            lineas_tabla.append(linea_encabezado)
            # Línea de separación
            linea_separacion = "-" * (longitud_columna * len(encabezados) + len(encabezados) - 1)
            lineas_tabla.append(linea_separacion)
        resultado = str(proceso.get_resultado())
        if resultado == '-1':
            resultado = 'error'
        # Datos
        datos = [
            [str(lote.get_num_lote()), str(proceso.get_id()), str(proceso.get_operando_a()),
             str(proceso.get_operacion()), str(proceso.get_operando_b()), resultado]
        ]
        for fila in datos:
            linea_datos = " | ".join([formato_columna.format(valor) for valor in fila])
            lineas_tabla.append(linea_datos)

        # Unir todas las líneas en una sola cadena
        tabla_completa = "\n".join(lineas_tabla)

        if self.texto_lotes_terminados == "No hay lotes terminados.":
            self.texto_lotes_terminados = tabla_completa
        else:
            self.texto_lotes_terminados += "\n" + tabla_completa
