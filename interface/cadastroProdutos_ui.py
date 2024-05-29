# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastroProdutos.ui'
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

class Ui_cadastroProdutos(object):
    def setupUi(self, cadastroProdutos):
        if not cadastroProdutos.objectName():
            cadastroProdutos.setObjectName(u"cadastroProdutos")
        cadastroProdutos.resize(519, 848)
        self.layoutWidget = QWidget(cadastroProdutos)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 481, 741))
        self.verticalLayout_1 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.Adicionar_Produtos = QLabel(self.layoutWidget)
        self.Adicionar_Produtos.setObjectName(u"Adicionar_Produtos")
        font = QFont()
        font.setFamilies([u"Montserrat ExtraBold"])
        font.setPointSize(20)
        font.setBold(True)
        self.Adicionar_Produtos.setFont(font)
        self.Adicionar_Produtos.setStyleSheet(u"color: rgb(99, 99, 99);")

        self.verticalLayout_1.addWidget(self.Adicionar_Produtos)

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

        self.categoria = QComboBox(self.layoutWidget)
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.addItem("")
        self.categoria.setObjectName(u"categoria")
        self.categoria.setMinimumSize(QSize(0, 0))
        self.categoria.setMaximumSize(QSize(350, 35))
        font3 = QFont()
        font3.setFamilies([u"Raleway Black"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.categoria.setFont(font3)

        self.verticalLayout_3.addWidget(self.categoria)


        self.verticalLayout_1.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.fabricante = QLineEdit(self.layoutWidget)
        self.fabricante.setObjectName(u"fabricante")
        self.fabricante.setMaximumSize(QSize(350, 35))
        self.fabricante.setFont(font2)

        self.verticalLayout_4.addWidget(self.fabricante)


        self.verticalLayout_1.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_11)

        self.quantidade = QLineEdit(self.layoutWidget)
        self.quantidade.setObjectName(u"quantidade")
        self.quantidade.setMaximumSize(QSize(350, 35))
        self.quantidade.setFont(font2)

        self.verticalLayout_7.addWidget(self.quantidade)


        self.verticalLayout_1.addLayout(self.verticalLayout_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_9)

        self.valor = QLineEdit(self.layoutWidget)
        self.valor.setObjectName(u"valor")
        self.valor.setMaximumSize(QSize(350, 35))
        self.valor.setFont(font2)

        self.verticalLayout_5.addWidget(self.valor)


        self.verticalLayout_1.addLayout(self.verticalLayout_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_12)

        self.garantia = QLineEdit(self.layoutWidget)
        self.garantia.setObjectName(u"garantia")
        self.garantia.setMaximumSize(QSize(350, 35))
        self.garantia.setFont(font2)

        self.verticalLayout_8.addWidget(self.garantia)


        self.verticalLayout_1.addLayout(self.verticalLayout_8)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_10)

        self.codigoDeBarra = QLineEdit(self.layoutWidget)
        self.codigoDeBarra.setObjectName(u"codigoDeBarra")
        self.codigoDeBarra.setMaximumSize(QSize(350, 35))
        self.codigoDeBarra.setFont(font2)
        self.codigoDeBarra.setReadOnly(True)

        self.verticalLayout_6.addWidget(self.codigoDeBarra)


        self.verticalLayout_1.addLayout(self.verticalLayout_6)

        self.layoutWidget_2 = QWidget(cadastroProdutos)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(290, 790, 211, 43))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnCadastrarProdutos = QPushButton(self.layoutWidget_2)
        self.btnCadastrarProdutos.setObjectName(u"btnCadastrarProdutos")
        self.btnCadastrarProdutos.setMinimumSize(QSize(0, 41))
        self.btnCadastrarProdutos.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btnCadastrarProdutos)

        self.cancelar = QPushButton(self.layoutWidget_2)
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


        self.retranslateUi(cadastroProdutos)
        self.cancelar.toggled.connect(cadastroProdutos.close)

        QMetaObject.connectSlotsByName(cadastroProdutos)
    # setupUi

    def retranslateUi(self, cadastroProdutos):
        cadastroProdutos.setWindowTitle(QCoreApplication.translate("cadastroProdutos", u"Dialog", None))
        self.Adicionar_Produtos.setText(QCoreApplication.translate("cadastroProdutos", u"Cadastro de Produtos", None))
        self.label_2.setText(QCoreApplication.translate("cadastroProdutos", u"Nome do produto", None))
        self.label_4.setText(QCoreApplication.translate("cadastroProdutos", u"Categoria", None))
        self.categoria.setItemText(0, QCoreApplication.translate("cadastroProdutos", u"Jogos", None))
        self.categoria.setItemText(1, QCoreApplication.translate("cadastroProdutos", u"Acess\u00f3rios", None))
        self.categoria.setItemText(2, QCoreApplication.translate("cadastroProdutos", u"Produtos Geek", None))

        self.label_5.setText(QCoreApplication.translate("cadastroProdutos", u"Fabricante", None))
        self.label_11.setText(QCoreApplication.translate("cadastroProdutos", u"Quantidade", None))
        self.label_9.setText(QCoreApplication.translate("cadastroProdutos", u"Valor", None))
        self.label_12.setText(QCoreApplication.translate("cadastroProdutos", u"Garantia", None))
        self.label_10.setText(QCoreApplication.translate("cadastroProdutos", u"Codigo de barra", None))
        self.btnCadastrarProdutos.setText(QCoreApplication.translate("cadastroProdutos", u"Cadastrar", None))
        self.cancelar.setText(QCoreApplication.translate("cadastroProdutos", u"Cancelar", None))
    # retranslateUi

