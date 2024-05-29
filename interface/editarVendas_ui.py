# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editarVendas.ui'
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

class Ui_editarVendas(object):
    def setupUi(self, editarVendas):
        if not editarVendas.objectName():
            editarVendas.setObjectName(u"editarVendas")
        editarVendas.resize(611, 863)
        self.layoutWidget = QWidget(editarVendas)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(70, 20, 481, 741))
        self.verticalLayout_1 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.verticalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.Editar_Cliente = QLabel(self.layoutWidget)
        self.Editar_Cliente.setObjectName(u"Editar_Cliente")
        font = QFont()
        font.setFamilies([u"Montserrat ExtraBold"])
        font.setPointSize(20)
        font.setBold(True)
        self.Editar_Cliente.setFont(font)
        self.Editar_Cliente.setStyleSheet(u"color: rgb(99, 99, 99);")

        self.verticalLayout_1.addWidget(self.Editar_Cliente)

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

        self.editarVendasCliente = QLineEdit(self.layoutWidget)
        self.editarVendasCliente.setObjectName(u"editarVendasCliente")
        self.editarVendasCliente.setMaximumSize(QSize(350, 35))
        font2 = QFont()
        font2.setPointSize(12)
        self.editarVendasCliente.setFont(font2)

        self.verticalLayout_2.addWidget(self.editarVendasCliente)


        self.verticalLayout_1.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.editarVendasProdutos = QLineEdit(self.layoutWidget)
        self.editarVendasProdutos.setObjectName(u"editarVendasProdutos")
        self.editarVendasProdutos.setMaximumSize(QSize(350, 35))
        self.editarVendasProdutos.setFont(font2)

        self.verticalLayout_3.addWidget(self.editarVendasProdutos)


        self.verticalLayout_1.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.editarVendasValor = QLineEdit(self.layoutWidget)
        self.editarVendasValor.setObjectName(u"editarVendasValor")
        self.editarVendasValor.setMaximumSize(QSize(350, 35))
        self.editarVendasValor.setFont(font2)

        self.verticalLayout_4.addWidget(self.editarVendasValor)


        self.verticalLayout_1.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_11)

        self.editarVendasPagamento = QLineEdit(self.layoutWidget)
        self.editarVendasPagamento.setObjectName(u"editarVendasPagamento")
        self.editarVendasPagamento.setMaximumSize(QSize(350, 35))
        self.editarVendasPagamento.setFont(font2)

        self.verticalLayout_7.addWidget(self.editarVendasPagamento)


        self.verticalLayout_1.addLayout(self.verticalLayout_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_9)

        self.editarVendasStatus = QLineEdit(self.layoutWidget)
        self.editarVendasStatus.setObjectName(u"editarVendasStatus")
        self.editarVendasStatus.setMaximumSize(QSize(350, 35))
        self.editarVendasStatus.setFont(font2)

        self.verticalLayout_5.addWidget(self.editarVendasStatus)


        self.verticalLayout_1.addLayout(self.verticalLayout_5)

        self.layoutWidget_2 = QWidget(editarVendas)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(340, 790, 211, 43))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cadastrarVenda = QPushButton(self.layoutWidget_2)
        self.cadastrarVenda.setObjectName(u"cadastrarVenda")
        self.cadastrarVenda.setMinimumSize(QSize(0, 41))
        self.cadastrarVenda.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.cadastrarVenda)

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


        self.retranslateUi(editarVendas)
        self.cancelar.toggled.connect(editarVendas.close)

        QMetaObject.connectSlotsByName(editarVendas)
    # setupUi

    def retranslateUi(self, editarVendas):
        editarVendas.setWindowTitle(QCoreApplication.translate("editarVendas", u"Dialog", None))
        self.Editar_Cliente.setText(QCoreApplication.translate("editarVendas", u"Editar Vendas", None))
        self.label_2.setText(QCoreApplication.translate("editarVendas", u"Cliente", None))
        self.label_4.setText(QCoreApplication.translate("editarVendas", u"Produtos", None))
        self.label_5.setText(QCoreApplication.translate("editarVendas", u"Valor", None))
        self.label_11.setText(QCoreApplication.translate("editarVendas", u"Forma de pagamento", None))
        self.label_9.setText(QCoreApplication.translate("editarVendas", u"Status Pagamento", None))
        self.cadastrarVenda.setText(QCoreApplication.translate("editarVendas", u"Cadastrar", None))
        self.cancelar.setText(QCoreApplication.translate("editarVendas", u"Cancelar", None))
    # retranslateUi

