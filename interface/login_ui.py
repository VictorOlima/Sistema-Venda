# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(700, 500)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QSize(700, 500))
        Login.setMaximumSize(QSize(700, 500))
        Login.setAcceptDrops(True)
        Login.setAutoFillBackground(False)
        self.widget = QWidget(Login)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 70, 600, 350))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.btn_entrar = QPushButton(self.widget)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(380, 240, 161, 31))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 85, 0);")
        self.nomeUser = QLabel(self.widget)
        self.nomeUser.setObjectName(u"nomeUser")
        self.nomeUser.setGeometry(QRect(380, 110, 81, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setKerning(True)
        self.nomeUser.setFont(font1)
        self.inputNome = QLineEdit(self.widget)
        self.inputNome.setObjectName(u"inputNome")
        self.inputNome.setGeometry(QRect(380, 130, 161, 31))
        self.Sistema = QLabel(self.widget)
        self.Sistema.setObjectName(u"Sistema")
        self.Sistema.setGeometry(QRect(420, 50, 71, 31))
        font2 = QFont()
        font2.setPointSize(15)
        self.Sistema.setFont(font2)
        self.senhaUser = QLabel(self.widget)
        self.senhaUser.setObjectName(u"senhaUser")
        self.senhaUser.setGeometry(QRect(380, 170, 81, 21))
        font3 = QFont()
        font3.setPointSize(10)
        self.senhaUser.setFont(font3)
        self.inputSenha = QLineEdit(self.widget)
        self.inputSenha.setObjectName(u"inputSenha")
        self.inputSenha.setGeometry(QRect(380, 190, 161, 31))
        self.Logo = QLabel(self.widget)
        self.Logo.setObjectName(u"Logo")
        self.Logo.setGeometry(QRect(0, 0, 350, 350))
        self.Logo.setMaximumSize(QSize(400, 400))
        self.Logo.setPixmap(QPixmap(u"img/logo.png"))
        self.Logo.setScaledContents(True)
        self.imgUser = QLabel(self.widget)
        self.imgUser.setObjectName(u"imgUser")
        self.imgUser.setGeometry(QRect(340, 130, 35, 35))
        self.imgUser.setFont(font3)
        self.imgUser.setPixmap(QPixmap(u"img/user.png"))
        self.imgUser.setScaledContents(True)
        self.imgSenha = QLabel(self.widget)
        self.imgSenha.setObjectName(u"imgSenha")
        self.imgSenha.setGeometry(QRect(340, 190, 30, 30))
        self.imgSenha.setFont(font3)
        self.imgSenha.setPixmap(QPixmap(u"img/key.png"))
        self.imgSenha.setScaledContents(True)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.btn_entrar.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.nomeUser.setText(QCoreApplication.translate("Login", u"Nome", None))
        self.Sistema.setText(QCoreApplication.translate("Login", u"Sistema", None))
        self.senhaUser.setText(QCoreApplication.translate("Login", u"Senha", None))
        self.Logo.setText("")
        self.imgUser.setText("")
        self.imgSenha.setText("")
    # retranslateUi

