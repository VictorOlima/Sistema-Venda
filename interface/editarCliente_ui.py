# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editarCliente.ui'
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

class Ui_editarCliente(object):
    def setupUi(self, editarCliente):
        if not editarCliente.objectName():
            editarCliente.setObjectName(u"editarCliente")
        editarCliente.resize(547, 833)
        editarCliente.setInputMethodHints(Qt.ImhDialableCharactersOnly|Qt.ImhFormattedNumbersOnly|Qt.ImhNoPredictiveText|Qt.ImhPreferNumbers)
        self.layoutWidget_2 = QWidget(editarCliente)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(310, 780, 211, 43))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.botaoEditar = QPushButton(self.layoutWidget_2)
        self.botaoEditar.setObjectName(u"botaoEditar")
        self.botaoEditar.setMinimumSize(QSize(0, 41))
        self.botaoEditar.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}")

        self.horizontalLayout.addWidget(self.botaoEditar)

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

        self.layoutWidget = QWidget(editarCliente)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 10, 481, 741))
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

        self.editarRg = QLineEdit(self.layoutWidget)
        self.editarRg.setObjectName(u"editarRg")
        self.editarRg.setMaximumSize(QSize(350, 35))
        self.editarRg.setFont(font2)

        self.verticalLayout_3.addWidget(self.editarRg)


        self.verticalLayout_1.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.editarCpf = QLineEdit(self.layoutWidget)
        self.editarCpf.setObjectName(u"editarCpf")
        self.editarCpf.setMaximumSize(QSize(350, 35))
        self.editarCpf.setFont(font2)

        self.verticalLayout_4.addWidget(self.editarCpf)


        self.verticalLayout_1.addLayout(self.verticalLayout_4)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_11)

        self.editarTelefone = QLineEdit(self.layoutWidget)
        self.editarTelefone.setObjectName(u"editarTelefone")
        self.editarTelefone.setMaximumSize(QSize(350, 35))
        self.editarTelefone.setFont(font2)

        self.verticalLayout_7.addWidget(self.editarTelefone)


        self.verticalLayout_1.addLayout(self.verticalLayout_7)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_9)

        self.editarEmail = QLineEdit(self.layoutWidget)
        self.editarEmail.setObjectName(u"editarEmail")
        self.editarEmail.setMaximumSize(QSize(350, 35))
        self.editarEmail.setFont(font2)

        self.verticalLayout_5.addWidget(self.editarEmail)


        self.verticalLayout_1.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_10)

        self.editarEndereco = QLineEdit(self.layoutWidget)
        self.editarEndereco.setObjectName(u"editarEndereco")
        self.editarEndereco.setMaximumSize(QSize(350, 35))
        self.editarEndereco.setFont(font2)

        self.verticalLayout_6.addWidget(self.editarEndereco)


        self.verticalLayout_1.addLayout(self.verticalLayout_6)


        self.retranslateUi(editarCliente)
        self.cancelar.toggled.connect(editarCliente.close)

        QMetaObject.connectSlotsByName(editarCliente)
    # setupUi

    def retranslateUi(self, editarCliente):
        editarCliente.setWindowTitle(QCoreApplication.translate("editarCliente", u"Dialog", None))
        self.botaoEditar.setText(QCoreApplication.translate("editarCliente", u"Editar", None))
        self.cancelar.setText(QCoreApplication.translate("editarCliente", u"Cancelar", None))
        self.Editar_Cliente.setText(QCoreApplication.translate("editarCliente", u"Editar Clientes", None))
        self.label_2.setText(QCoreApplication.translate("editarCliente", u"Nome Completo", None))
        self.label_4.setText(QCoreApplication.translate("editarCliente", u"RG", None))
        self.label_5.setText(QCoreApplication.translate("editarCliente", u"CPF", None))
        self.label_11.setText(QCoreApplication.translate("editarCliente", u"Telefone", None))
        self.label_9.setText(QCoreApplication.translate("editarCliente", u"E-mail", None))
        self.label_10.setText(QCoreApplication.translate("editarCliente", u"Endere\u00e7o", None))
    # retranslateUi

