# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'buscarClientes.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QGridLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_buscarClientes(object):
    def setupUi(self, buscarClientes):
        if not buscarClientes.objectName():
            buscarClientes.setObjectName(u"buscarClientes")
        buscarClientes.resize(1104, 715)
        self.widget = QWidget(buscarClientes)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(70, 70, 961, 561))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pesquisaVendasClientes = QPushButton(self.widget)
        self.pesquisaVendasClientes.setObjectName(u"pesquisaVendasClientes")
        self.pesquisaVendasClientes.setStyleSheet(u"QPushButton{\n"
"border:none;\n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u"../img/magnifying-glass (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.pesquisaVendasClientes.setIcon(icon)
        self.pesquisaVendasClientes.setIconSize(QSize(25, 25))

        self.gridLayout.addWidget(self.pesquisaVendasClientes, 1, 1, 1, 1)

        self.buscarClientes2 = QLabel(self.widget)
        self.buscarClientes2.setObjectName(u"buscarClientes2")
        font = QFont()
        font.setFamilies([u"Montserrat ExtraBold"])
        font.setPointSize(20)
        font.setBold(True)
        self.buscarClientes2.setFont(font)
        self.buscarClientes2.setStyleSheet(u"color: rgb(99, 99, 99);")

        self.gridLayout.addWidget(self.buscarClientes2, 0, 0, 1, 1)

        self.tabelasPesquisaClientes = QTableWidget(self.widget)
        if (self.tabelasPesquisaClientes.columnCount() < 5):
            self.tabelasPesquisaClientes.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelasPesquisaClientes.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelasPesquisaClientes.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelasPesquisaClientes.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelasPesquisaClientes.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelasPesquisaClientes.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tabelasPesquisaClientes.setObjectName(u"tabelasPesquisaClientes")
        self.tabelasPesquisaClientes.setEnabled(True)
        self.tabelasPesquisaClientes.setAutoFillBackground(False)
        self.tabelasPesquisaClientes.setFrameShape(QFrame.StyledPanel)
        self.tabelasPesquisaClientes.setFrameShadow(QFrame.Plain)
        self.tabelasPesquisaClientes.setLineWidth(10)
        self.tabelasPesquisaClientes.setMidLineWidth(10)
        self.tabelasPesquisaClientes.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabelasPesquisaClientes.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tabelasPesquisaClientes.setAutoScroll(True)
        self.tabelasPesquisaClientes.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tabelasPesquisaClientes.setTabKeyNavigation(False)
        self.tabelasPesquisaClientes.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.tabelasPesquisaClientes.setShowGrid(True)
        self.tabelasPesquisaClientes.setSortingEnabled(False)
        self.tabelasPesquisaClientes.horizontalHeader().setVisible(False)
        self.tabelasPesquisaClientes.horizontalHeader().setCascadingSectionResizes(True)
        self.tabelasPesquisaClientes.horizontalHeader().setMinimumSectionSize(50)
        self.tabelasPesquisaClientes.horizontalHeader().setDefaultSectionSize(100)
        self.tabelasPesquisaClientes.horizontalHeader().setHighlightSections(False)
        self.tabelasPesquisaClientes.horizontalHeader().setProperty("showSortIndicator", False)
        self.tabelasPesquisaClientes.horizontalHeader().setStretchLastSection(True)
        self.tabelasPesquisaClientes.verticalHeader().setVisible(False)
        self.tabelasPesquisaClientes.verticalHeader().setCascadingSectionResizes(True)
        self.tabelasPesquisaClientes.verticalHeader().setMinimumSectionSize(10)
        self.tabelasPesquisaClientes.verticalHeader().setDefaultSectionSize(50)
        self.tabelasPesquisaClientes.verticalHeader().setHighlightSections(True)
        self.tabelasPesquisaClientes.verticalHeader().setProperty("showSortIndicator", True)
        self.tabelasPesquisaClientes.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.tabelasPesquisaClientes, 2, 0, 1, 2)

        self.tabelasPesquisaClientes2 = QLineEdit(self.widget)
        self.tabelasPesquisaClientes2.setObjectName(u"tabelasPesquisaClientes2")
        self.tabelasPesquisaClientes2.setMinimumSize(QSize(0, 30))
        self.tabelasPesquisaClientes2.setMaximumSize(QSize(16777215, 250))
        self.tabelasPesquisaClientes2.setSizeIncrement(QSize(250, 250))

        self.gridLayout.addWidget(self.tabelasPesquisaClientes2, 1, 0, 1, 1)


        self.retranslateUi(buscarClientes)

        QMetaObject.connectSlotsByName(buscarClientes)
    # setupUi

    def retranslateUi(self, buscarClientes):
        buscarClientes.setWindowTitle(QCoreApplication.translate("buscarClientes", u"Dialog", None))
        self.pesquisaVendasClientes.setText("")
        self.buscarClientes2.setText(QCoreApplication.translate("buscarClientes", u"Buscar Clientes:", None))
        ___qtablewidgetitem = self.tabelasPesquisaClientes.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("buscarClientes", u"ID", None));
        ___qtablewidgetitem1 = self.tabelasPesquisaClientes.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("buscarClientes", u"NOME", None));
        ___qtablewidgetitem2 = self.tabelasPesquisaClientes.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("buscarClientes", u"TELEFONE", None));
        ___qtablewidgetitem3 = self.tabelasPesquisaClientes.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("buscarClientes", u"EMAIL", None));
        ___qtablewidgetitem4 = self.tabelasPesquisaClientes.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("buscarClientes", u"EDITAR", None));
    # retranslateUi

