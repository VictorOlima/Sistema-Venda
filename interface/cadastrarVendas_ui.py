# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastrarVendas.ui'
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
    QWidget)

class Ui_cadastroVendas(object):
    def setupUi(self, cadastroVendas):
        if not cadastroVendas.objectName():
            cadastroVendas.setObjectName(u"cadastroVendas")
        cadastroVendas.resize(485, 676)
        self.layoutWidget_2 = QWidget(cadastroVendas)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(200, 590, 211, 43))
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

        self.cliente = QLabel(cadastroVendas)
        self.cliente.setObjectName(u"cliente")
        self.cliente.setGeometry(QRect(60, 140, 58, 22))
        font = QFont()
        font.setFamilies([u"Montserrat Medium"])
        font.setPointSize(12)
        self.cliente.setFont(font)
        self.vendas = QLabel(cadastroVendas)
        self.vendas.setObjectName(u"vendas")
        self.vendas.setGeometry(QRect(40, 47, 107, 37))
        font1 = QFont()
        font1.setFamilies([u"Montserrat ExtraBold"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.vendas.setFont(font1)
        self.vendas.setStyleSheet(u"color: rgb(99, 99, 99);")
        self.line = QFrame(cadastroVendas)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(40, 90, 421, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.produtos = QLabel(cadastroVendas)
        self.produtos.setObjectName(u"produtos")
        self.produtos.setGeometry(QRect(60, 220, 76, 22))
        self.produtos.setFont(font)
        self.formaDePagamento = QLabel(cadastroVendas)
        self.formaDePagamento.setObjectName(u"formaDePagamento")
        self.formaDePagamento.setGeometry(QRect(60, 380, 180, 22))
        self.formaDePagamento.setFont(font)
        self.statusPagamento_2 = QLabel(cadastroVendas)
        self.statusPagamento_2.setObjectName(u"statusPagamento_2")
        self.statusPagamento_2.setGeometry(QRect(60, 460, 221, 31))
        self.statusPagamento_2.setFont(font)
        self.valor = QLabel(cadastroVendas)
        self.valor.setObjectName(u"valor")
        self.valor.setGeometry(QRect(60, 300, 41, 22))
        self.valor.setFont(font)
        self.vendasValor = QLineEdit(cadastroVendas)
        self.vendasValor.setObjectName(u"vendasValor")
        self.vendasValor.setGeometry(QRect(60, 330, 350, 35))
        self.vendasValor.setMaximumSize(QSize(350, 35))
        font2 = QFont()
        font2.setPointSize(12)
        self.vendasValor.setFont(font2)
        self.vendasCliente = QLineEdit(cadastroVendas)
        self.vendasCliente.setObjectName(u"vendasCliente")
        self.vendasCliente.setGeometry(QRect(60, 170, 351, 31))
        self.vendasProdutos = QLineEdit(cadastroVendas)
        self.vendasProdutos.setObjectName(u"vendasProdutos")
        self.vendasProdutos.setGeometry(QRect(60, 250, 351, 31))
        self.vendasPagamento = QLineEdit(cadastroVendas)
        self.vendasPagamento.setObjectName(u"vendasPagamento")
        self.vendasPagamento.setGeometry(QRect(60, 410, 350, 35))
        self.vendasPagamento.setMaximumSize(QSize(350, 35))
        self.vendasPagamento.setFont(font2)
        self.vendasStatus = QLineEdit(cadastroVendas)
        self.vendasStatus.setObjectName(u"vendasStatus")
        self.vendasStatus.setGeometry(QRect(60, 500, 350, 35))
        self.vendasStatus.setMaximumSize(QSize(350, 35))
        self.vendasStatus.setFont(font2)

        self.retranslateUi(cadastroVendas)
        self.cancelar.toggled.connect(cadastroVendas.close)

        QMetaObject.connectSlotsByName(cadastroVendas)
    # setupUi

    def retranslateUi(self, cadastroVendas):
        cadastroVendas.setWindowTitle(QCoreApplication.translate("cadastroVendas", u"Dialog", None))
        self.cadastrarVenda.setText(QCoreApplication.translate("cadastroVendas", u"Cadastrar", None))
        self.cancelar.setText(QCoreApplication.translate("cadastroVendas", u"Cancelar", None))
        self.cliente.setText(QCoreApplication.translate("cadastroVendas", u"Cliente", None))
        self.vendas.setText(QCoreApplication.translate("cadastroVendas", u"Vendas", None))
        self.produtos.setText(QCoreApplication.translate("cadastroVendas", u"Produtos", None))
        self.formaDePagamento.setText(QCoreApplication.translate("cadastroVendas", u"Forma de pagamento", None))
        self.statusPagamento_2.setText(QCoreApplication.translate("cadastroVendas", u"Status Pagamento", None))
        self.valor.setText(QCoreApplication.translate("cadastroVendas", u"Valor", None))
    # retranslateUi

