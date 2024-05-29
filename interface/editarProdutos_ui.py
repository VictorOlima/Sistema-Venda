# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editarProdutos.ui'
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

class Ui_editarProdutos(object):
    def setupUi(self, editarProdutos):
        if not editarProdutos.objectName():
            editarProdutos.setObjectName(u"editarProdutos")
        editarProdutos.resize(516, 848)
        self.layoutWidget = QWidget(editarProdutos)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 20, 481, 741))
        self.verticalLayout_1 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.Editar_Produtos = QLabel(self.layoutWidget)
        self.Editar_Produtos.setObjectName(u"Editar_Produtos")
        font = QFont()
        font.setFamilies([u"Montserrat ExtraBold"])
        font.setPointSize(20)
        font.setBold(True)
        self.Editar_Produtos.setFont(font)
        self.Editar_Produtos.setStyleSheet(u"color: rgb(99, 99, 99);")

        self.verticalLayout_1.addWidget(self.Editar_Produtos)

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

        self.editarNome = QLineEdit(self.layoutWidget)
        self.editarNome.setObjectName(u"editarNome")
        self.editarNome.setMaximumSize(QSize(350, 35))
        font2 = QFont()
        font2.setPointSize(12)
        self.editarNome.setFont(font2)

        self.verticalLayout_2.addWidget(self.editarNome)


        self.verticalLayout_1.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.editarCategoria = QComboBox(self.layoutWidget)
        self.editarCategoria.addItem("")
        self.editarCategoria.addItem("")
        self.editarCategoria.addItem("")
        self.editarCategoria.setObjectName(u"editarCategoria")
        self.editarCategoria.setMinimumSize(QSize(0, 0))
        self.editarCategoria.setMaximumSize(QSize(350, 35))
        font3 = QFont()
        font3.setFamilies([u"Raleway Black"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setItalic(True)
        font3.setUnderline(False)
        font3.setStrikeOut(False)
        font3.setKerning(True)
        self.editarCategoria.setFont(font3)

        self.verticalLayout_3.addWidget(self.editarCategoria)


        self.verticalLayout_1.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.editarFabrincante = QLineEdit(self.layoutWidget)
        self.editarFabrincante.setObjectName(u"editarFabrincante")
        self.editarFabrincante.setMaximumSize(QSize(350, 35))
        self.editarFabrincante.setFont(font2)

        self.verticalLayout_4.addWidget(self.editarFabrincante)


        self.verticalLayout_1.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_11)

        self.editarQuantidade = QLineEdit(self.layoutWidget)
        self.editarQuantidade.setObjectName(u"editarQuantidade")
        self.editarQuantidade.setMaximumSize(QSize(350, 35))
        self.editarQuantidade.setFont(font2)

        self.verticalLayout_7.addWidget(self.editarQuantidade)


        self.verticalLayout_1.addLayout(self.verticalLayout_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_9)

        self.editarValor = QLineEdit(self.layoutWidget)
        self.editarValor.setObjectName(u"editarValor")
        self.editarValor.setMaximumSize(QSize(350, 35))
        self.editarValor.setFont(font2)
        self.editarValor.setInputMethodHints(Qt.ImhPreferNumbers)

        self.verticalLayout_5.addWidget(self.editarValor)


        self.verticalLayout_1.addLayout(self.verticalLayout_5)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.verticalLayout_8.addWidget(self.label_12)

        self.EditarGarantia = QLineEdit(self.layoutWidget)
        self.EditarGarantia.setObjectName(u"EditarGarantia")
        self.EditarGarantia.setMaximumSize(QSize(350, 35))
        self.EditarGarantia.setFont(font2)

        self.verticalLayout_8.addWidget(self.EditarGarantia)


        self.verticalLayout_1.addLayout(self.verticalLayout_8)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_10)

        self.EditarCodigoDeBarra = QLineEdit(self.layoutWidget)
        self.EditarCodigoDeBarra.setObjectName(u"EditarCodigoDeBarra")
        self.EditarCodigoDeBarra.setMaximumSize(QSize(350, 35))
        self.EditarCodigoDeBarra.setFont(font2)

        self.verticalLayout_6.addWidget(self.EditarCodigoDeBarra)


        self.verticalLayout_1.addLayout(self.verticalLayout_6)

        self.layoutWidget_2 = QWidget(editarProdutos)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(290, 790, 211, 43))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btnEditarProdutos = QPushButton(self.layoutWidget_2)
        self.btnEditarProdutos.setObjectName(u"btnEditarProdutos")
        self.btnEditarProdutos.setMinimumSize(QSize(0, 41))
        self.btnEditarProdutos.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.btnEditarProdutos)

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


        self.retranslateUi(editarProdutos)
        self.cancelar.toggled.connect(editarProdutos.close)

        QMetaObject.connectSlotsByName(editarProdutos)
    # setupUi

    def retranslateUi(self, editarProdutos):
        editarProdutos.setWindowTitle(QCoreApplication.translate("editarProdutos", u"Dialog", None))
        self.Editar_Produtos.setText(QCoreApplication.translate("editarProdutos", u"Editar Produtos", None))
        self.label_2.setText(QCoreApplication.translate("editarProdutos", u"Nome do produto", None))
        self.label_4.setText(QCoreApplication.translate("editarProdutos", u"Categoria", None))
        self.editarCategoria.setItemText(0, QCoreApplication.translate("editarProdutos", u"Jogos", None))
        self.editarCategoria.setItemText(1, QCoreApplication.translate("editarProdutos", u"Acess\u00f3rios", None))
        self.editarCategoria.setItemText(2, QCoreApplication.translate("editarProdutos", u"Produtos Geek", None))

        self.label_5.setText(QCoreApplication.translate("editarProdutos", u"Fabricante", None))
        self.label_11.setText(QCoreApplication.translate("editarProdutos", u"Quantidade", None))
        self.label_9.setText(QCoreApplication.translate("editarProdutos", u"Valor", None))
        self.label_12.setText(QCoreApplication.translate("editarProdutos", u"Garantia", None))
        self.label_10.setText(QCoreApplication.translate("editarProdutos", u"Codigo de barra", None))
        self.btnEditarProdutos.setText(QCoreApplication.translate("editarProdutos", u"Cadastrar", None))
        self.cancelar.setText(QCoreApplication.translate("editarProdutos", u"Cancelar", None))
    # retranslateUi

