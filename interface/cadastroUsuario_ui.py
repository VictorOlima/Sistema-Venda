# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastroUsuario.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_cadastroUsuario(object):
    def setupUi(self, cadastroUsuario):
        if not cadastroUsuario.objectName():
            cadastroUsuario.setObjectName(u"cadastroUsuario")
        cadastroUsuario.resize(370, 530)
        self.layoutWidget = QWidget(cadastroUsuario)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(110, 470, 211, 43))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cadastrarUsuario = QPushButton(self.layoutWidget)
        self.cadastrarUsuario.setObjectName(u"cadastrarUsuario")
        self.cadastrarUsuario.setMinimumSize(QSize(0, 41))
        self.cadastrarUsuario.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.cadastrarUsuario)

        self.cancelar = QPushButton(self.layoutWidget)
        self.cancelar.setObjectName(u"cancelar")
        self.cancelar.setMinimumSize(QSize(0, 41))
        self.cancelar.setStyleSheet(u"QPushButton{\n"
"	background-color: #585858;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")
        self.cancelar.setCheckable(True)

        self.horizontalLayout.addWidget(self.cancelar)

        self.layoutWidget_2 = QWidget(cadastroUsuario)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(30, 20, 294, 430))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Montserrat ExtraBold"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(99, 99, 99);")

        self.verticalLayout_2.addWidget(self.label)

        self.line = QFrame(self.layoutWidget_2)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.nome = QVBoxLayout()
        self.nome.setObjectName(u"nome")
        self.label_2 = QLabel(self.layoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.nome.addWidget(self.label_2)

        self.nomeUsuario = QLineEdit(self.layoutWidget_2)
        self.nomeUsuario.setObjectName(u"nomeUsuario")
        self.nomeUsuario.setMaximumSize(QSize(350, 35))
        font2 = QFont()
        font2.setPointSize(12)
        self.nomeUsuario.setFont(font2)

        self.nome.addWidget(self.nomeUsuario)


        self.verticalLayout_2.addLayout(self.nome)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.layoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_4)

        self.usuario = QLineEdit(self.layoutWidget_2)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setMaximumSize(QSize(350, 35))
        self.usuario.setFont(font2)

        self.verticalLayout_5.addWidget(self.usuario)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_5 = QLabel(self.layoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_5)

        self.senha_1 = QLineEdit(self.layoutWidget_2)
        self.senha_1.setObjectName(u"senha_1")
        self.senha_1.setMaximumSize(QSize(350, 35))
        self.senha_1.setFont(font2)

        self.verticalLayout_3.addWidget(self.senha_1)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_8 = QLabel(self.layoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_8)

        self.senha_2 = QLineEdit(self.layoutWidget_2)
        self.senha_2.setObjectName(u"senha_2")
        self.senha_2.setMaximumSize(QSize(350, 35))
        self.senha_2.setFont(font2)

        self.verticalLayout_8.addWidget(self.senha_2)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.layoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_9.addWidget(self.label_9)

        self.perfil = QComboBox(self.layoutWidget_2)
        self.perfil.addItem("")
        self.perfil.addItem("")
        self.perfil.addItem("")
        self.perfil.setObjectName(u"perfil")
        self.perfil.setMinimumSize(QSize(50, 40))
        self.perfil.setMaximumSize(QSize(16777215, 50))
        font3 = QFont()
        font3.setPointSize(10)
        self.perfil.setFont(font3)

        self.verticalLayout_9.addWidget(self.perfil)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)


        self.verticalLayout_2.addLayout(self.verticalLayout_8)


        self.retranslateUi(cadastroUsuario)
        self.cancelar.toggled.connect(cadastroUsuario.close)

        QMetaObject.connectSlotsByName(cadastroUsuario)
    # setupUi

    def retranslateUi(self, cadastroUsuario):
        cadastroUsuario.setWindowTitle(QCoreApplication.translate("cadastroUsuario", u"Dialog", None))
        self.cadastrarUsuario.setText(QCoreApplication.translate("cadastroUsuario", u"Cadastrar", None))
        self.cancelar.setText(QCoreApplication.translate("cadastroUsuario", u"Cancelar", None))
        self.label.setText(QCoreApplication.translate("cadastroUsuario", u"Cadastro de Usu\u00e1rio", None))
        self.label_2.setText(QCoreApplication.translate("cadastroUsuario", u"Nome", None))
        self.label_4.setText(QCoreApplication.translate("cadastroUsuario", u"Usu\u00e1rio", None))
        self.label_5.setText(QCoreApplication.translate("cadastroUsuario", u"Senha", None))
        self.label_8.setText(QCoreApplication.translate("cadastroUsuario", u"Senha", None))
        self.label_9.setText(QCoreApplication.translate("cadastroUsuario", u"Perfil", None))
        self.perfil.setItemText(0, QCoreApplication.translate("cadastroUsuario", u"Gerente", None))
        self.perfil.setItemText(1, QCoreApplication.translate("cadastroUsuario", u"Vendedor", None))
        self.perfil.setItemText(2, QCoreApplication.translate("cadastroUsuario", u"Estoquista", None))

    # retranslateUi

