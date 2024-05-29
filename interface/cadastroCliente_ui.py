# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastroCliente.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_cadastroCliente(object):
    def setupUi(self, cadastroCliente):
        if not cadastroCliente.objectName():
            cadastroCliente.setObjectName(u"cadastroCliente")
        cadastroCliente.resize(546, 832)
        cadastroCliente.setStyleSheet(u"QDialog{\n"
"	background-color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border:1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left: 15px;\n"
"	height: 35px;\n"
"\n"
"}")
        self.layoutWidget = QWidget(cadastroCliente)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 10, 481, 741))
        self.verticalLayout_1 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.Adicionar_Cliente = QLabel(self.layoutWidget)
        self.Adicionar_Cliente.setObjectName(u"Adicionar_Cliente")
        font = QFont()
        font.setFamilies([u"Montserrat ExtraBold"])
        font.setPointSize(20)
        font.setBold(True)
        self.Adicionar_Cliente.setFont(font)
        self.Adicionar_Cliente.setStyleSheet(u"color: rgb(99, 99, 99);")

        self.verticalLayout_1.addWidget(self.Adicionar_Cliente)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_1.addWidget(self.line)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Montserrat Medium"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_2)

        self.nome = QLineEdit(self.layoutWidget)
        self.nome.setObjectName(u"nome")
        self.nome.setMaximumSize(QSize(350, 35))
        font2 = QFont()
        font2.setPointSize(12)
        self.nome.setFont(font2)

        self.verticalLayout_2.addWidget(self.nome)


        self.verticalLayout_1.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.rg = QLineEdit(self.layoutWidget)
        self.rg.setObjectName(u"rg")
        self.rg.setMaximumSize(QSize(350, 35))
        self.rg.setFont(font2)

        self.verticalLayout_3.addWidget(self.rg)


        self.verticalLayout_1.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.cpf = QLineEdit(self.layoutWidget)
        self.cpf.setObjectName(u"cpf")
        self.cpf.setMaximumSize(QSize(350, 35))
        self.cpf.setFont(font2)

        self.verticalLayout_4.addWidget(self.cpf)


        self.verticalLayout_1.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_11)

        self.telefone = QLineEdit(self.layoutWidget)
        self.telefone.setObjectName(u"telefone")
        self.telefone.setMaximumSize(QSize(350, 35))
        self.telefone.setFont(font2)

        self.verticalLayout_7.addWidget(self.telefone)


        self.verticalLayout_1.addLayout(self.verticalLayout_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_9)

        self.email = QLineEdit(self.layoutWidget)
        self.email.setObjectName(u"email")
        self.email.setMaximumSize(QSize(350, 35))
        self.email.setFont(font2)

        self.verticalLayout_5.addWidget(self.email)


        self.verticalLayout_1.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_10)

        self.endereco = QLineEdit(self.layoutWidget)
        self.endereco.setObjectName(u"endereco")
        self.endereco.setMaximumSize(QSize(350, 35))
        self.endereco.setFont(font2)

        self.verticalLayout_6.addWidget(self.endereco)


        self.verticalLayout_1.addLayout(self.verticalLayout_6)

        self.layoutWidget1 = QWidget(cadastroCliente)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(300, 780, 211, 43))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnCadastrarCliente = QPushButton(self.layoutWidget1)
        self.btnCadastrarCliente.setObjectName(u"btnCadastrarCliente")
        self.btnCadastrarCliente.setMinimumSize(QSize(0, 41))
        self.btnCadastrarCliente.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btnCadastrarCliente)

        self.cancelar = QPushButton(self.layoutWidget1)
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


        self.retranslateUi(cadastroCliente)
        self.cancelar.toggled.connect(cadastroCliente.close)

        QMetaObject.connectSlotsByName(cadastroCliente)
    # setupUi

    def retranslateUi(self, cadastroCliente):
        cadastroCliente.setWindowTitle(QCoreApplication.translate("cadastroCliente", u"Dialog", None))
        self.Adicionar_Cliente.setText(QCoreApplication.translate("cadastroCliente", u"Adicionar Cliente", None))
        self.label_2.setText(QCoreApplication.translate("cadastroCliente", u"Nome Completo", None))
        self.label_4.setText(QCoreApplication.translate("cadastroCliente", u"RG", None))
        self.label_5.setText(QCoreApplication.translate("cadastroCliente", u"CPF", None))
        self.label_11.setText(QCoreApplication.translate("cadastroCliente", u"Telefone", None))
        self.label_9.setText(QCoreApplication.translate("cadastroCliente", u"E-mail", None))
        self.label_10.setText(QCoreApplication.translate("cadastroCliente", u"Endere\u00e7o", None))
        self.btnCadastrarCliente.setText(QCoreApplication.translate("cadastroCliente", u"Cadastrar", None))
        self.cancelar.setText(QCoreApplication.translate("cadastroCliente", u"Cancelar", None))
    # retranslateUi

