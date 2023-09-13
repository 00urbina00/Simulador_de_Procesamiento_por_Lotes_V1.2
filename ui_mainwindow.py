# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1517, 925)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.groupBox_4 = QGroupBox(self.frame_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 50))
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.groupBox_4)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(111, 0))
        self.label.setMaximumSize(QSize(111, 16777215))
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.le_lotes = QLineEdit(self.groupBox_4)
        self.le_lotes.setObjectName(u"le_lotes")
        self.le_lotes.setMinimumSize(QSize(100, 0))
        self.le_lotes.setMaximumSize(QSize(100, 16777215))
        self.le_lotes.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_lotes.setFrame(False)
        self.le_lotes.setAlignment(Qt.AlignCenter)
        self.le_lotes.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.le_lotes)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.frame_5 = QFrame(self.groupBox_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(900, 0))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.pb_iniciar = QPushButton(self.frame_5)
        self.pb_iniciar.setObjectName(u"pb_iniciar")
        self.pb_iniciar.setMinimumSize(QSize(100, 23))
        self.pb_iniciar.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"	background-color: rgb(220, 220, 220);\n"
"	\n"
"	color: rgb(0, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"   \n"
"	background-color: rgb(190, 190, 190);\n"
"	\n"
"	color: rgb(0, 170, 0);\n"
"}")
        self.pb_iniciar.setCheckable(False)

        self.horizontalLayout_13.addWidget(self.pb_iniciar)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.label_10 = QLabel(self.frame_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(111, 0))
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_10)

        self.sb_num_procesos = QSpinBox(self.frame_5)
        self.sb_num_procesos.setObjectName(u"sb_num_procesos")
        self.sb_num_procesos.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.sb_num_procesos.setWrapping(False)
        self.sb_num_procesos.setFrame(True)
        self.sb_num_procesos.setAlignment(Qt.AlignCenter)
        self.sb_num_procesos.setReadOnly(False)
        self.sb_num_procesos.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.sb_num_procesos.setMinimum(1)

        self.horizontalLayout_13.addWidget(self.sb_num_procesos)

        self.pb_agregar_procesos = QPushButton(self.frame_5)
        self.pb_agregar_procesos.setObjectName(u"pb_agregar_procesos")
        self.pb_agregar_procesos.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"	background-color: rgb(220, 220, 220);\n"
"	\n"
"	color: rgb(0, 85, 255);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"   \n"
"	background-color: rgb(190, 190, 190);\n"
"	\n"
"	color: rgb(0, 170, 0);\n"
"}")

        self.horizontalLayout_13.addWidget(self.pb_agregar_procesos)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(111, 0))
        self.label_9.setMaximumSize(QSize(220, 16777215))
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_9)

        self.le_numero_procesos = QLineEdit(self.frame_5)
        self.le_numero_procesos.setObjectName(u"le_numero_procesos")
        self.le_numero_procesos.setMinimumSize(QSize(50, 0))
        self.le_numero_procesos.setMaximumSize(QSize(50, 16777215))
        self.le_numero_procesos.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_numero_procesos.setFrame(False)
        self.le_numero_procesos.setAlignment(Qt.AlignCenter)
        self.le_numero_procesos.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.le_numero_procesos)


        self.horizontalLayout_13.addLayout(self.horizontalLayout_5)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.gridLayout_4.addWidget(self.groupBox_4, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(6, 6, 6, 6)
        self.groupBox = QGroupBox(self.frame_4)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 400))
        self.groupBox.setMaximumSize(QSize(495, 800))
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(0, 85, 255);")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.pte_lote_actual = QPlainTextEdit(self.groupBox)
        self.pte_lote_actual.setObjectName(u"pte_lote_actual")
        self.pte_lote_actual.setMinimumSize(QSize(378, 0))
        self.pte_lote_actual.setMaximumSize(QSize(1677777, 16777215))
        font1 = QFont()
        font1.setFamily(u"Courier New")
        font1.setPointSize(9)
        self.pte_lote_actual.setFont(font1)
        self.pte_lote_actual.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_6.addWidget(self.pte_lote_actual, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.frame_4)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(400, 400))
        self.groupBox_2.setMaximumSize(QSize(16777215, 800))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(85, 170, 0);")
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.pte_ejecucion = QPlainTextEdit(self.groupBox_2)
        self.pte_ejecucion.setObjectName(u"pte_ejecucion")
        self.pte_ejecucion.setFont(font1)
        self.pte_ejecucion.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_7.addWidget(self.pte_ejecucion, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.frame_4)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(500, 400))
        self.groupBox_3.setMaximumSize(QSize(16777215, 800))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(255, 0, 0);")
        self.gridLayout_8 = QGridLayout(self.groupBox_3)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.pte_terminados = QPlainTextEdit(self.groupBox_3)
        self.pte_terminados.setObjectName(u"pte_terminados")
        self.pte_terminados.setFont(font1)
        self.pte_terminados.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")

        self.gridLayout_8.addWidget(self.pte_terminados, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_3)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.btn_limpiar = QPushButton(self.frame_4)
        self.btn_limpiar.setObjectName(u"btn_limpiar")
        self.btn_limpiar.setStyleSheet(u"color: rgb(0, 0, 255);")

        self.gridLayout_2.addWidget(self.btn_limpiar, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_3)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_5 = QGroupBox(self.frame_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 50))
        self.groupBox_5.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.groupBox_5)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(111, 0))
        self.label_2.setMaximumSize(QSize(111, 16777215))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(0, 85, 255);")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.le_tiempo_global = QLineEdit(self.groupBox_5)
        self.le_tiempo_global.setObjectName(u"le_tiempo_global")
        self.le_tiempo_global.setMinimumSize(QSize(100, 0))
        self.le_tiempo_global.setMaximumSize(QSize(100, 16777215))
        self.le_tiempo_global.setFont(font)
        self.le_tiempo_global.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.le_tiempo_global.setFrame(False)
        self.le_tiempo_global.setAlignment(Qt.AlignCenter)
        self.le_tiempo_global.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.le_tiempo_global)


        self.horizontalLayout_7.addLayout(self.horizontalLayout_2)

        self.frame_6 = QFrame(self.groupBox_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(900, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.lb_pausa = QLabel(self.frame_6)
        self.lb_pausa.setObjectName(u"lb_pausa")
        self.lb_pausa.setMinimumSize(QSize(111, 0))
        self.lb_pausa.setFont(font)
        self.lb_pausa.setStyleSheet(u"color: rgb(0, 170, 0);")
        self.lb_pausa.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.lb_pausa)

        self.horizontalSpacer_7 = QSpacerItem(260, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_7)

        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(111, 0))
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11)

        self.pb_capturar_procesos = QPushButton(self.frame_6)
        self.pb_capturar_procesos.setObjectName(u"pb_capturar_procesos")
        self.pb_capturar_procesos.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"	background-color: rgb(220, 220, 220);\n"
"	\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"   \n"
"	background-color: rgb(190, 190, 190);\n"
"	\n"
"	\n"
"	color: rgb(0, 0, 255);\n"
"}")

        self.horizontalLayout_6.addWidget(self.pb_capturar_procesos)


        self.horizontalLayout_7.addWidget(self.frame_6)


        self.gridLayout_5.addWidget(self.groupBox_5, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.frame_7 = QFrame(self.frame)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 0))
        self.frame_7.setMaximumSize(QSize(16777215, 180))
        self.frame_7.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_7)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_6 = QGroupBox(self.frame_7)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMinimumSize(QSize(100, 0))
        self.groupBox_6.setMaximumSize(QSize(16777215, 170))
        self.groupBox_6.setFont(font)
        self.groupBox_6.setStyleSheet(u"background-color: rgb(190, 190, 190);")
        self.gridLayout_10 = QGridLayout(self.groupBox_6)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.groupBox_8 = QGroupBox(self.groupBox_6)
        self.groupBox_8.setObjectName(u"groupBox_8")
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        self.groupBox_8.setFont(font2)
        self.groupBox_8.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.gridLayout_11 = QGridLayout(self.groupBox_8)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.groupBox_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 50))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_5)


        self.horizontalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.le_tiempo_max = QLineEdit(self.groupBox_8)
        self.le_tiempo_max.setObjectName(u"le_tiempo_max")
        self.le_tiempo_max.setEnabled(True)
        self.le_tiempo_max.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.le_tiempo_max.setText(u"")
        self.le_tiempo_max.setMaxLength(10)
        self.le_tiempo_max.setFrame(True)
        self.le_tiempo_max.setAlignment(Qt.AlignCenter)
        self.le_tiempo_max.setClearButtonEnabled(True)

        self.verticalLayout_3.addWidget(self.le_tiempo_max)


        self.horizontalLayout_8.addLayout(self.verticalLayout_3)


        self.gridLayout_11.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)


        self.gridLayout_10.addWidget(self.groupBox_8, 1, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox_6)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setFont(font2)
        self.groupBox_7.setStyleSheet(u"background-color: rgb(200, 200, 200);")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_4 = QLabel(self.groupBox_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 50))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_4)

        self.le_operador = QLineEdit(self.groupBox_7)
        self.le_operador.setObjectName(u"le_operador")
        self.le_operador.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.le_operador.setFrame(True)
        self.le_operador.setAlignment(Qt.AlignCenter)
        self.le_operador.setClearButtonEnabled(True)

        self.horizontalLayout_11.addWidget(self.le_operador)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_11)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.groupBox_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7)

        self.le_operando_a = QLineEdit(self.groupBox_7)
        self.le_operando_a.setObjectName(u"le_operando_a")
        self.le_operando_a.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.le_operando_a.setFrame(True)
        self.le_operando_a.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.le_operando_a)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_9)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.groupBox_7)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_8)

        self.le_operando_b = QLineEdit(self.groupBox_7)
        self.le_operando_b.setObjectName(u"le_operando_b")
        self.le_operando_b.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.le_operando_b.setFrame(True)
        self.le_operando_b.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.le_operando_b)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_10)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.gridLayout_10.addWidget(self.groupBox_7, 1, 1, 1, 1)

        self.pb_agregar = QPushButton(self.groupBox_6)
        self.pb_agregar.setObjectName(u"pb_agregar")
        self.pb_agregar.setMinimumSize(QSize(1204, 23))
        self.pb_agregar.setFont(font)
        self.pb_agregar.setStyleSheet(u"\n"
"QPushButton {\n"
"   \n"
"	background-color: rgb(220, 220, 220);\n"
"	border-bottom-left-radius: 20px;\n"
"    border-bottom-right-radius: 20px;\n"
"	\n"
"	color: rgb(0, 85, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    \n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QPushButton:pressed {\n"
"   \n"
"	background-color: rgb(190, 190, 190);\n"
"	\n"
"	color: rgb(0, 170, 0);\n"
"}")

        self.gridLayout_10.addWidget(self.pb_agregar, 2, 0, 1, 2)


        self.gridLayout_9.addWidget(self.groupBox_6, 0, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_7, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1517, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simulador de procesos", None))
        self.groupBox_4.setTitle("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Lotes Pendientes: ", None))
        self.le_lotes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.pb_iniciar.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Procesos iniciales: ", None))
        self.pb_agregar_procesos.setText(QCoreApplication.translate("MainWindow", u"Agregar", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"N\u00famero de procesos en cola: ", None))
        self.le_numero_procesos.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Lote Actual", None))
        self.pte_lote_actual.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID  | TME | TT", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"En Ejecuci\u00f3n", None))
        self.pte_ejecucion.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Informacion (Nombre, Operacion, TME, ID) | TT | TR", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Terminados", None))
        self.pte_terminados.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ID | Operacion y datos | Resultado", None))
        self.btn_limpiar.setText(QCoreApplication.translate("MainWindow", u"Limpiar consolas", None))
        self.groupBox_5.setTitle("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tiempo Global:", None))
        self.le_tiempo_global.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lb_pausa.setText(QCoreApplication.translate("MainWindow", u"Ejecuci\u00f3n", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Capturar procesos", None))
        self.pb_capturar_procesos.setText(QCoreApplication.translate("MainWindow", u"Habilitar/Deshabilitar", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"Crear Proceso", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("MainWindow", u"Datos", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Tiempo Maximo Estimado:", None))
        self.le_tiempo_max.setPlaceholderText(QCoreApplication.translate("MainWindow", u"1", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"Operaci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Operacion a realizar:", None))
        self.le_operador.setPlaceholderText(QCoreApplication.translate("MainWindow", u"(+, -, *, /,%, %%)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Operando A:", None))
        self.le_operando_a.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Operando", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Operando B", None))
        self.le_operando_b.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Operando", None))
        self.pb_agregar.setText(QCoreApplication.translate("MainWindow", u"Agregar Proceso", None))
    # retranslateUi

