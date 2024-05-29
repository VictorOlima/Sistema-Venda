# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 839)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.topMenu = QWidget(self.centralwidget)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setStyleSheet(u"QWidget{\n"
"background-color: rgb(71, 71, 71);\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.topMenu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton = QPushButton(self.topMenu)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMaximumSize(QSize(30, 30))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        icon = QIcon()
        icon.addFile(u"img/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(25, 25))
        self.pushButton.setCheckable(True)
        self.pushButton.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.pushButton)

        self.label_3 = QLabel(self.topMenu)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label_3)

        self.label = QLabel(self.topMenu)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.topMenu)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"img/gear (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(25, 25))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setAutoExclusive(True)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.topMenu)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(30, 30))
        self.pushButton_3.setMaximumSize(QSize(30, 30))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"border: none;\n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 85, 0);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"img/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(25, 25))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setAutoExclusive(False)

        self.horizontalLayout.addWidget(self.pushButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_5.addWidget(self.topMenu)

        self.mainMenu = QWidget(self.centralwidget)
        self.mainMenu.setObjectName(u"mainMenu")
        self.mainMenu.setMinimumSize(QSize(0, 40))
        self.mainMenu.setStyleSheet(u"QWidget{\n"
"background-color: rgb(255, 85, 0);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	border:none;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"	border-top-right-radius:10px;\n"
"	border-bottom-right-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background-color: rgb(255, 142, 89);\n"
"color: #341234;\n"
"font-weight:bold;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.mainMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, 0)
        self.clientes_2 = QPushButton(self.mainMenu)
        self.clientes_2.setObjectName(u"clientes_2")
        self.clientes_2.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u"img/user21.png", QSize(), QIcon.Normal, QIcon.Off)
        self.clientes_2.setIcon(icon3)
        self.clientes_2.setIconSize(QSize(25, 25))
        self.clientes_2.setCheckable(True)
        self.clientes_2.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.clientes_2)

        self.vendas_2 = QPushButton(self.mainMenu)
        self.vendas_2.setObjectName(u"vendas_2")
        self.vendas_2.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"img/cart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.vendas_2.setIcon(icon4)
        self.vendas_2.setIconSize(QSize(25, 25))
        self.vendas_2.setCheckable(True)
        self.vendas_2.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.vendas_2)

        self.produtos_2 = QPushButton(self.mainMenu)
        self.produtos_2.setObjectName(u"produtos_2")
        self.produtos_2.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u"img/box-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.produtos_2.setIcon(icon5)
        self.produtos_2.setIconSize(QSize(25, 25))
        self.produtos_2.setCheckable(True)
        self.produtos_2.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.produtos_2)

        self.finandeiro_2 = QPushButton(self.mainMenu)
        self.finandeiro_2.setObjectName(u"finandeiro_2")
        self.finandeiro_2.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u"img/calculator.png", QSize(), QIcon.Normal, QIcon.Off)
        self.finandeiro_2.setIcon(icon6)
        self.finandeiro_2.setIconSize(QSize(25, 25))
        self.finandeiro_2.setCheckable(True)
        self.finandeiro_2.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.finandeiro_2)

        self.config_2 = QPushButton(self.mainMenu)
        self.config_2.setObjectName(u"config_2")
        self.config_2.setStyleSheet(u"")
        self.config_2.setIcon(icon1)
        self.config_2.setIconSize(QSize(25, 25))
        self.config_2.setCheckable(True)
        self.config_2.setAutoExclusive(True)

        self.horizontalLayout_2.addWidget(self.config_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_5.addWidget(self.mainMenu)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.clientes = QWidget()
        self.clientes.setObjectName(u"clientes")
        self.gridLayout_4 = QGridLayout(self.clientes)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_6 = QWidget(self.clientes)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.tabelaClientes = QTableWidget(self.widget_6)
        if (self.tabelaClientes.columnCount() < 5):
            self.tabelaClientes.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelaClientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelaClientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelaClientes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelaClientes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelaClientes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelaClientes.setObjectName(u"tabelaClientes")
        self.tabelaClientes.setAlternatingRowColors(True)
        self.tabelaClientes.setShowGrid(True)
        self.tabelaClientes.verticalHeader().sectionSize(40)
        self.tabelaClientes.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tabelaClientes.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.horizontalLayout_6.addWidget(self.tabelaClientes)


        self.gridLayout_4.addWidget(self.widget_6, 2, 0, 1, 1)

        self.widget_7 = QWidget(self.clientes)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMaximumSize(QSize(16777215, 50))
        self.widget_7.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.tituloClientes = QLabel(self.widget_7)
        self.tituloClientes.setObjectName(u"tituloClientes")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.tituloClientes.setFont(font1)
        self.tituloClientes.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_4.addWidget(self.tituloClientes)


        self.gridLayout_4.addWidget(self.widget_7, 0, 0, 1, 1)

        self.widget_5 = QWidget(self.clientes)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_3 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.inputClientes = QLineEdit(self.widget_5)
        self.inputClientes.setObjectName(u"inputClientes")
        self.inputClientes.setMinimumSize(QSize(0, 30))
        self.inputClientes.setMaximumSize(QSize(16777215, 300))
        font2 = QFont()
        font2.setPointSize(10)
        self.inputClientes.setFont(font2)
        self.inputClientes.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(216, 216, 216);")

        self.horizontalLayout_3.addWidget(self.inputClientes)

        self.pesquisarClientes = QPushButton(self.widget_5)
        self.pesquisarClientes.setObjectName(u"pesquisarClientes")
        self.pesquisarClientes.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"img/magnifying-glass (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pesquisarClientes.setIcon(icon7)
        self.pesquisarClientes.setIconSize(QSize(25, 25))

        self.horizontalLayout_3.addWidget(self.pesquisarClientes)

        self.clientesCadastrar = QPushButton(self.widget_5)
        self.clientesCadastrar.setObjectName(u"clientesCadastrar")
        self.clientesCadastrar.setMaximumSize(QSize(16777215, 200))
        self.clientesCadastrar.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.clientesCadastrar)


        self.gridLayout_4.addWidget(self.widget_5, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.clientes)
        self.vendas = QWidget()
        self.vendas.setObjectName(u"vendas")
        self.verticalLayout_3 = QVBoxLayout(self.vendas)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_8 = QWidget(self.vendas)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 50))
        self.widget_8.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.tituloVendas = QLabel(self.widget_8)
        self.tituloVendas.setObjectName(u"tituloVendas")
        self.tituloVendas.setFont(font1)
        self.tituloVendas.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.tituloVendas)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_17 = QWidget(self.vendas)
        self.widget_17.setObjectName(u"widget_17")
        self.widget_17.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_10 = QGridLayout(self.widget_17)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.adicionarVendas = QPushButton(self.widget_17)
        self.adicionarVendas.setObjectName(u"adicionarVendas")
        self.adicionarVendas.setMaximumSize(QSize(16777215, 200))
        self.adicionarVendas.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")

        self.gridLayout_10.addWidget(self.adicionarVendas, 0, 2, 1, 2)

        self.inputVendas = QLineEdit(self.widget_17)
        self.inputVendas.setObjectName(u"inputVendas")
        self.inputVendas.setMinimumSize(QSize(0, 30))
        self.inputVendas.setMaximumSize(QSize(16777215, 300))
        self.inputVendas.setFont(font2)
        self.inputVendas.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(216, 216, 216);")

        self.gridLayout_10.addWidget(self.inputVendas, 0, 0, 1, 1)

        self.pesquisarVendas = QPushButton(self.widget_17)
        self.pesquisarVendas.setObjectName(u"pesquisarVendas")
        self.pesquisarVendas.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"\n"
"}")
        self.pesquisarVendas.setIcon(icon7)
        self.pesquisarVendas.setIconSize(QSize(25, 25))

        self.gridLayout_10.addWidget(self.pesquisarVendas, 0, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_17)

        self.widget_18 = QWidget(self.vendas)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_15 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.tabelaVendas = QTableWidget(self.widget_18)
        if (self.tabelaVendas.columnCount() < 5):
            self.tabelaVendas.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabelaVendas.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabelaVendas.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabelaVendas.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabelaVendas.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabelaVendas.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        self.tabelaVendas.setObjectName(u"tabelaVendas")
        self.tabelaVendas.setAlternatingRowColors(True)
        self.tabelaVendas.setShowGrid(True)
        self.tabelaVendas.verticalHeader().sectionSize(40)
        self.tabelaVendas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tabelaVendas.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)



        self.horizontalLayout_15.addWidget(self.tabelaVendas)


        self.verticalLayout_3.addWidget(self.widget_18)

        self.stackedWidget.addWidget(self.vendas)
        self.produtos = QWidget()
        self.produtos.setObjectName(u"produtos")
        self.verticalLayout_4 = QVBoxLayout(self.produtos)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_24 = QWidget(self.produtos)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMaximumSize(QSize(16777215, 50))
        self.widget_24.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_24)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.tituloProdutos = QLabel(self.widget_24)
        self.tituloProdutos.setObjectName(u"tituloProdutos")
        self.tituloProdutos.setFont(font1)
        self.tituloProdutos.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_36.addWidget(self.tituloProdutos)


        self.verticalLayout_4.addWidget(self.widget_24)

        self.widget_20 = QWidget(self.produtos)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_13 = QGridLayout(self.widget_20)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.cadastrarProdutos = QPushButton(self.widget_20)
        self.cadastrarProdutos.setObjectName(u"cadastrarProdutos")
        self.cadastrarProdutos.setMaximumSize(QSize(16777215, 200))
        self.cadastrarProdutos.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")

        self.gridLayout_13.addWidget(self.cadastrarProdutos, 0, 2, 1, 2)

        self.pesquisarProdutos = QPushButton(self.widget_20)
        self.pesquisarProdutos.setObjectName(u"pesquisarProdutos")
        self.pesquisarProdutos.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"\n"
"}")
        self.pesquisarProdutos.setIcon(icon7)
        self.pesquisarProdutos.setIconSize(QSize(25, 25))

        self.gridLayout_13.addWidget(self.pesquisarProdutos, 0, 1, 1, 1)

        self.inputProdutos = QLineEdit(self.widget_20)
        self.inputProdutos.setObjectName(u"inputProdutos")
        self.inputProdutos.setMinimumSize(QSize(0, 30))
        self.inputProdutos.setMaximumSize(QSize(16777215, 300))
        self.inputProdutos.setFont(font2)
        self.inputProdutos.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(216, 216, 216);")

        self.gridLayout_13.addWidget(self.inputProdutos, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.widget_20)

        self.widget_19 = QWidget(self.produtos)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_20 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.tabelaProduto = QTableWidget(self.widget_19)
        if (self.tabelaProduto.columnCount() < 5):
            self.tabelaProduto.setColumnCount(9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabelaProduto.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabelaProduto.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabelaProduto.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabelaProduto.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabelaProduto.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        self.tabelaProduto.setObjectName(u"tabelaProduto")
        self.tabelaProduto.setAlternatingRowColors(True)
        self.tabelaProduto.setShowGrid(True)
        self.tabelaProduto.verticalHeader().sectionSize(40)
        self.tabelaProduto.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tabelaProduto.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.horizontalLayout_20.addWidget(self.tabelaProduto)


        self.verticalLayout_4.addWidget(self.widget_19)

        self.stackedWidget.addWidget(self.produtos)
        self.financeiro = QWidget()
        self.financeiro.setObjectName(u"financeiro")
        self.verticalLayout_18 = QVBoxLayout(self.financeiro)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_27 = QWidget(self.financeiro)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMaximumSize(QSize(16777215, 50))
        self.widget_27.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.tituloFinanceiro = QLabel(self.widget_27)
        self.tituloFinanceiro.setObjectName(u"tituloFinanceiro")
        self.tituloFinanceiro.setFont(font1)
        self.tituloFinanceiro.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_40.addWidget(self.tituloFinanceiro)


        self.verticalLayout_18.addWidget(self.widget_27)

        self.widget_26 = QWidget(self.financeiro)
        self.widget_26.setObjectName(u"widget_26")
        self.widget_26.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_15 = QGridLayout(self.widget_26)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.visualizarFinanceiro = QPushButton(self.widget_26)
        self.visualizarFinanceiro.setObjectName(u"visualizarFinanceiro")
        self.visualizarFinanceiro.setMaximumSize(QSize(16777215, 200))
        self.visualizarFinanceiro.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(0, 85, 0);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"")

        self.gridLayout_15.addWidget(self.visualizarFinanceiro, 0, 2, 1, 2)

        self.pesquisarFinanceiro = QPushButton(self.widget_26)
        self.pesquisarFinanceiro.setObjectName(u"pesquisarFinanceiro")
        self.pesquisarFinanceiro.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"\n"
"}")
        self.pesquisarFinanceiro.setIcon(icon7)
        self.pesquisarFinanceiro.setIconSize(QSize(25, 25))

        self.gridLayout_15.addWidget(self.pesquisarFinanceiro, 0, 1, 1, 1)

        self.inputFinanceiro = QLineEdit(self.widget_26)
        self.inputFinanceiro.setObjectName(u"inputFinanceiro")
        self.inputFinanceiro.setMinimumSize(QSize(0, 30))
        self.inputFinanceiro.setMaximumSize(QSize(16777215, 300))
        self.inputFinanceiro.setFont(font2)
        self.inputFinanceiro.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(216, 216, 216);")

        self.gridLayout_15.addWidget(self.inputFinanceiro, 0, 0, 1, 1)


        self.verticalLayout_18.addWidget(self.widget_26)

        self.widget_25 = QWidget(self.financeiro)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.tabelaFinanceiro = QTableWidget(self.widget_25)
        if (self.tabelaFinanceiro.columnCount() < 5):
            self.tabelaFinanceiro.setColumnCount(5)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabelaFinanceiro.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabelaFinanceiro.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabelaFinanceiro.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabelaFinanceiro.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabelaFinanceiro.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        self.tabelaFinanceiro.setObjectName(u"tabelaFinanceiro")
        self.tabelaFinanceiro.setAlternatingRowColors(True)
        self.tabelaFinanceiro.setShowGrid(True)
        self.tabelaFinanceiro.verticalHeader().sectionSize(40)
        self.tabelaFinanceiro.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tabelaFinanceiro.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.horizontalLayout_39.addWidget(self.tabelaFinanceiro)


        self.verticalLayout_18.addWidget(self.widget_25)

        self.stackedWidget.addWidget(self.financeiro)
        self.config = QWidget()
        self.config.setObjectName(u"config")
        self.verticalLayout_8 = QVBoxLayout(self.config)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_21 = QWidget(self.config)
        self.widget_21.setObjectName(u"widget_21")
        self.verticalLayout_7 = QVBoxLayout(self.widget_21)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_20 = QLabel(self.widget_21)
        self.label_20.setObjectName(u"label_20")
        font3 = QFont()
        font3.setFamilies([u"Montserrat ExtraBold"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"color: rgb(99, 99, 99);")

        self.verticalLayout_6.addWidget(self.label_20)

        self.line = QFrame(self.widget_21)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.verticalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_21 = QLabel(self.widget_21)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMinimumSize(QSize(150, 0))
        self.label_21.setMaximumSize(QSize(100, 100))
        font4 = QFont()
        font4.setFamilies([u"Montserrat Medium"])
        font4.setPointSize(12)
        self.label_21.setFont(font4)

        self.horizontalLayout_21.addWidget(self.label_21)

        self.nomeUsuario = QLineEdit(self.widget_21)
        self.nomeUsuario.setObjectName(u"nomeUsuario")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nomeUsuario.sizePolicy().hasHeightForWidth())
        self.nomeUsuario.setSizePolicy(sizePolicy)
        self.nomeUsuario.setMaximumSize(QSize(350, 35))
        font5 = QFont()
        font5.setPointSize(12)
        self.nomeUsuario.setFont(font5)

        self.horizontalLayout_21.addWidget(self.nomeUsuario)


        self.verticalLayout_6.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_22 = QLabel(self.widget_21)
        self.label_22.setObjectName(u"label_22")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Ignored, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy1)
        self.label_22.setMinimumSize(QSize(150, 0))
        self.label_22.setMaximumSize(QSize(150, 100))
        self.label_22.setFont(font4)

        self.horizontalLayout_22.addWidget(self.label_22)

        self.usuario = QLineEdit(self.widget_21)
        self.usuario.setObjectName(u"usuario")
        self.usuario.setMaximumSize(QSize(350, 35))
        self.usuario.setFont(font5)

        self.horizontalLayout_22.addWidget(self.usuario)


        self.verticalLayout_6.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_23 = QLabel(self.widget_21)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMinimumSize(QSize(150, 0))
        self.label_23.setMaximumSize(QSize(100, 100))
        self.label_23.setFont(font4)

        self.horizontalLayout_23.addWidget(self.label_23)

        self.senha_1 = QLineEdit(self.widget_21)
        self.senha_1.setObjectName(u"senha_1")
        self.senha_1.setMaximumSize(QSize(350, 35))
        self.senha_1.setFont(font5)
        self.senha_1.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_23.addWidget(self.senha_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_24 = QLabel(self.widget_21)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(150, 0))
        self.label_24.setMaximumSize(QSize(100, 100))
        self.label_24.setFont(font4)

        self.horizontalLayout_25.addWidget(self.label_24)

        self.senha_2 = QLineEdit(self.widget_21)
        self.senha_2.setObjectName(u"senha_2")
        self.senha_2.setMaximumSize(QSize(350, 35))
        self.senha_2.setFont(font5)
        self.senha_2.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.senha_2.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_25.addWidget(self.senha_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_25)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_25 = QLabel(self.widget_21)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(150, 0))
        self.label_25.setMaximumSize(QSize(100, 100))
        self.label_25.setFont(font4)

        self.horizontalLayout_24.addWidget(self.label_25)

        self.perfil = QComboBox(self.widget_21)
        self.perfil.addItem("")
        self.perfil.addItem("")
        self.perfil.addItem("")
        self.perfil.setObjectName(u"perfil")
        self.perfil.setMinimumSize(QSize(30, 30))
        self.perfil.setMaximumSize(QSize(350, 30))
        self.perfil.setFont(font2)

        self.horizontalLayout_24.addWidget(self.perfil)


        self.verticalLayout_9.addLayout(self.horizontalLayout_24)


        self.verticalLayout_6.addLayout(self.verticalLayout_9)


        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer = QSpacerItem(700, 10, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.cadastrarUsuario = QPushButton(self.widget_21)
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

        self.horizontalLayout_5.addWidget(self.cadastrarUsuario)

        self.cancelar = QPushButton(self.widget_21)
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

        self.horizontalLayout_5.addWidget(self.cancelar)


        self.verticalLayout_7.addLayout(self.horizontalLayout_5)


        self.verticalLayout_8.addWidget(self.widget_21)

        self.stackedWidget.addWidget(self.config)

        self.verticalLayout_5.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.toggled.connect(MainWindow.close)
        self.cancelar.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
#if QT_CONFIG(shortcut)
        self.pushButton.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Bem Vindo", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio: ", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.clientes_2.setText(QCoreApplication.translate("MainWindow", u"Clientes", None))
        self.vendas_2.setText(QCoreApplication.translate("MainWindow", u"Vendas", None))
        self.produtos_2.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.finandeiro_2.setText(QCoreApplication.translate("MainWindow", u"Financeiro", None))
        self.config_2.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00e3o", None))
        ___qtablewidgetitem = self.tabelaClientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tabelaClientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem2 = self.tabelaClientes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem3 = self.tabelaClientes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem4 = self.tabelaClientes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None));
        self.tituloClientes.setText(QCoreApplication.translate("MainWindow", u"CLIENTES", None))
        self.pesquisarClientes.setText("")
        self.clientesCadastrar.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.tituloVendas.setText(QCoreApplication.translate("MainWindow", u"VENDAS", None))
        self.adicionarVendas.setText(QCoreApplication.translate("MainWindow", u"ADICIONAR VENDA", None))
        self.pesquisarVendas.setText("")
        ___qtablewidgetitem5 = self.tabelaVendas.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem6 = self.tabelaVendas.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem7 = self.tabelaVendas.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem8 = self.tabelaVendas.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem9 = self.tabelaVendas.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None));
        self.tituloProdutos.setText(QCoreApplication.translate("MainWindow", u"PRODUTOS", None))
        self.cadastrarProdutos.setText(QCoreApplication.translate("MainWindow", u"CADASTRAR", None))
        self.pesquisarProdutos.setText("")
        ___qtablewidgetitem10 = self.tabelaProduto.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem11 = self.tabelaProduto.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem12 = self.tabelaProduto.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem13 = self.tabelaProduto.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem14 = self.tabelaProduto.horizontalHeaderItem(4)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None));
        self.tituloFinanceiro.setText(QCoreApplication.translate("MainWindow", u"FINANCEIRO", None))
        self.visualizarFinanceiro.setText(QCoreApplication.translate("MainWindow", u"VISUALIZAR", None))
        self.pesquisarFinanceiro.setText("")
        ___qtablewidgetitem15 = self.tabelaFinanceiro.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem16 = self.tabelaFinanceiro.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"NOME", None));
        ___qtablewidgetitem17 = self.tabelaFinanceiro.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"TELEFONE", None));
        ___qtablewidgetitem18 = self.tabelaFinanceiro.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None));
        ___qtablewidgetitem19 = self.tabelaFinanceiro.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"EDITAR", None));
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Cadastro de Usu\u00e1rio", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Repetir a senha", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Perfil", None))
        self.perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Gerente", None))
        self.perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Vendedor", None))
        self.perfil.setItemText(2, QCoreApplication.translate("MainWindow", u"Estoquista", None))

        self.cadastrarUsuario.setText(QCoreApplication.translate("MainWindow", u"Cadastrar", None))
        self.cancelar.setText(QCoreApplication.translate("MainWindow", u"Cancelar", None))
    # retranslateUi

