# -*- coding: utf-8 -*-

import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from data_interface import Ui_GraphWindow
import data_operations as do
import visualization as plot
import get_data as gt

class Ui_OptionsWindow(object):
    def setupUi(self, OptionsWindow):
        # Window
        OptionsWindow.setObjectName("OptionsWindow")
        OptionsWindow.setEnabled(True)
        # Window size
        OptionsWindow.resize(850, 665)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OptionsWindow.sizePolicy().hasHeightForWidth())
        OptionsWindow.setSizePolicy(sizePolicy)
        # Min & max window size 
        OptionsWindow.setMinimumSize(QtCore.QSize(850, 665))
        OptionsWindow.setMaximumSize(QtCore.QSize(850, 665))
        # Icon
        OptionsWindow.setWindowIcon(QtGui.QIcon('icon_t.png'))

        # CentralWidget --> u njega idu svi ostali widgeti
        self.centralwidget = QtWidgets.QWidget(OptionsWindow)
        self.centralwidget.setObjectName("CentralWidget")

        #########################         #########################
        ######################### VRIJEME #########################
        # Group Box koji sadrži opcije za odabir vremenskog perioda
        self.vrijemeBox = QtWidgets.QGroupBox(self.centralwidget)
        self.vrijemeBox.setGeometry(QtCore.QRect(50, 50, 480, 480))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.vrijemeBox.setFont(font)
        self.vrijemeBox.setAlignment(QtCore.Qt.AlignCenter)
        self.vrijemeBox.setObjectName("vrijemeBox")

        # Grid widget
        self.vrijemeGridLayoutWidget = QtWidgets.QWidget(self.vrijemeBox)
        self.vrijemeGridLayoutWidget.setGeometry(QtCore.QRect(20, 30, 442, 430))
        self.vrijemeGridLayoutWidget.setObjectName("vrijemeGridLayoutWidget")
        # Grid layout
        self.vrijemeGridLayout = QtWidgets.QGridLayout(self.vrijemeGridLayoutWidget)
        self.vrijemeGridLayout.setContentsMargins(0, 0, 0, 0)
        self.vrijemeGridLayout.setHorizontalSpacing(0)
        self.vrijemeGridLayout.setVerticalSpacing(10)
        self.vrijemeGridLayout.setObjectName("vrijemeGridLayout")


        ############### DAN ###############
        # Radio button za aktivirati 'dan'
        self.danRadio = QtWidgets.QRadioButton(self.vrijemeGridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.danRadio.setFont(font)
        self.danRadio.setObjectName("danRadio")
        self.vrijemeGridLayout.addWidget(self.danRadio, 2, 0, 1, 1)
        # Horizontal layout u kojem je widget za odabir dana
        self.pickDanHL = QtWidgets.QHBoxLayout()
        self.pickDanHL.setContentsMargins(40, -1, 215, 15)
        self.pickDanHL.setSpacing(0)
        self.pickDanHL.setObjectName("pickDanHL")
        # Time Edit Widget za odabir dana
        self.pickDan = QtWidgets.QDateTimeEdit(self.vrijemeGridLayoutWidget)
        self.pickDan.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pickDan.setFont(font)
        self.pickDan.setWrapping(False)
        self.pickDan.setDate(QtCore.QDate(2008, 1, 1))
        self.pickDan.setCalendarPopup(True)
        self.pickDan.setObjectName("pickDan")
        self.pickDanHL.addWidget(self.pickDan)
        self.vrijemeGridLayout.addLayout(self.pickDanHL, 3, 0, 1, 1)


        ############### MJESEC ###############
        # Radio button za aktivirati 'mjesec'
        self.mjesecRadio = QtWidgets.QRadioButton(self.vrijemeGridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.mjesecRadio.setFont(font)
        self.mjesecRadio.setObjectName("mjesecRadio")
        self.vrijemeGridLayout.addWidget(self.mjesecRadio, 4, 0, 1, 1)
        # Horizontal layout u kojem je widget za odabir mjeseca
        self.pickMjesecHL = QtWidgets.QHBoxLayout()
        self.pickMjesecHL.setContentsMargins(40, -1, -1, 15)
        self.pickMjesecHL.setSpacing(25)
        self.pickMjesecHL.setObjectName("pickMjesecHL")
        # Combo box widget za odabir mjeseca
        self.pickMjesecMjesec = QtWidgets.QSpinBox(self.vrijemeGridLayoutWidget)
        self.pickMjesecMjesec.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pickMjesecMjesec.setFont(font)
        self.pickMjesecMjesec.setMaximum(12)
        self.pickMjesecMjesec.setMinimum(1)
        self.pickMjesecMjesec.setValue(1)
        self.pickMjesecMjesec.setObjectName("pickMjesecMjesec")
        self.pickMjesecHL.addWidget(self.pickMjesecMjesec)
        # Combo box widget za odabir godine
        self.pickMjesecGodina = QtWidgets.QSpinBox(self.vrijemeGridLayoutWidget)
        self.pickMjesecGodina.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pickMjesecGodina.setFont(font)
        self.pickMjesecGodina.setMaximum(9999)
        self.pickMjesecGodina.setValue(2008)
        self.pickMjesecGodina.setObjectName("pickMjesecGodina")
        self.pickMjesecHL.addWidget(self.pickMjesecGodina)
        self.vrijemeGridLayout.addLayout(self.pickMjesecHL, 5, 0, 1, 1)


        ############### GODINA ###############
        # Radio button za aktivirati 'godinu'
        self.godinaRadio = QtWidgets.QRadioButton(self.vrijemeGridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.godinaRadio.setFont(font)
        self.godinaRadio.setObjectName("godinaRadio")
        self.vrijemeGridLayout.addWidget(self.godinaRadio, 6, 0, 1, 1)
        # Horizontal layout u kojem je widget za odabir godine
        self.pickGodinaHL = QtWidgets.QHBoxLayout()
        self.pickGodinaHL.setContentsMargins(40, -1, 215, 15)
        self.pickGodinaHL.setObjectName("pickGodinaHL")
        # Spin box widget za odabir godine
        self.pickGodina = QtWidgets.QSpinBox(self.vrijemeGridLayoutWidget)
        self.pickGodina.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.pickGodina.setFont(font)
        self.pickGodina.setMaximum(9999)
        self.pickGodina.setValue(2008)
        self.pickGodina.setObjectName("pickGodina")
        self.pickGodinaHL.addWidget(self.pickGodina)
        self.vrijemeGridLayout.addLayout(self.pickGodinaHL, 7, 0, 1, 1)


        ############### RASPON ###############
        # Radio button za aktivirati 'raspon'
        self.rasponRadio = QtWidgets.QRadioButton(self.vrijemeGridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.rasponRadio.setFont(font)
        self.rasponRadio.setObjectName("rasponRadio")
        self.vrijemeGridLayout.addWidget(self.rasponRadio, 8, 0, 1, 1)
        # Horizontal layout u kojem je widget za odabir raspona
        self.pickRasponHL = QtWidgets.QHBoxLayout()
        self.pickRasponHL.setContentsMargins(40, -1, -1, 15)
        self.pickRasponHL.setSpacing(10)
        self.pickRasponHL.setObjectName("pickRasponHL")
        # Label 'od'
        self.rasponOdLabel = QtWidgets.QLabel(self.vrijemeGridLayoutWidget)
        self.rasponOdLabel.setEnabled(False)
        self.rasponOdLabel.setMaximumSize(QtCore.QSize(25, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.rasponOdLabel.setFont(font)
        self.rasponOdLabel.setMinimumSize(40, 20)
        self.rasponOdLabel.setMaximumSize(40, 20)
        self.rasponOdLabel.setObjectName("rasponOdLabel")
        self.pickRasponHL.addWidget(self.rasponOdLabel)
        # Time Edit widget za početak raspona
        self.rasponOd = QtWidgets.QDateTimeEdit(self.vrijemeGridLayoutWidget)
        self.rasponOd.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.rasponOd.setFont(font)
        self.rasponOd.setDate(QtCore.QDate(2008, 1, 1))
        self.rasponOd.setCalendarPopup(True)
        self.rasponOd.setMinimumSize(140, 20)
        self.rasponOd.setMaximumSize(140, 20)
        self.rasponOd.setObjectName("rasponOd")
        self.pickRasponHL.addWidget(self.rasponOd)
        # Label do
        self.rasponDoLabel = QtWidgets.QLabel(self.vrijemeGridLayoutWidget)
        self.rasponDoLabel.setEnabled(False)
        self.rasponDoLabel.setMaximumSize(QtCore.QSize(25, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.rasponDoLabel.setFont(font)
        self.rasponDoLabel.setMinimumSize(40, 20)
        self.rasponDoLabel.setMaximumSize(40, 20)
        self.rasponDoLabel.setObjectName("rasponDoLabel")
        self.pickRasponHL.addWidget(self.rasponDoLabel)
        # Time Edit widget za kraj raspona
        self.rasponDo = QtWidgets.QDateTimeEdit(self.vrijemeGridLayoutWidget)
        self.rasponDo.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.rasponDo.setFont(font)
        self.rasponDo.setDate(QtCore.QDate(2008, 1, 1))
        self.rasponDo.setCalendarPopup(True)
        self.rasponDo.setMinimumSize(140, 20)
        self.rasponDo.setMaximumSize(140, 20)
        self.rasponDo.setObjectName("rasponDo")
        self.pickRasponHL.addWidget(self.rasponDo)
        self.vrijemeGridLayout.addLayout(self.pickRasponHL, 9, 0, 1, 1)


        ############### USPOREDBA ###############
        # Radio button za aktivirati 'usporedbu'
        self.usporedbaRadio = QtWidgets.QRadioButton(self.vrijemeGridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usporedbaRadio.setFont(font)
        self.usporedbaRadio.setObjectName("usporedbaRadio")
        self.vrijemeGridLayout.addWidget(self.usporedbaRadio, 10, 0, 1, 1)
        # Grid layout koji sadrži widgete za odabir raspona
        self.usporedbaGL = QtWidgets.QGridLayout()
        self.usporedbaGL.setContentsMargins(40, -1, -1, -1)
        self.usporedbaGL.setSpacing(10)
        self.usporedbaGL.setObjectName("usporedbaGL")
        ##### LABELS #####
        # Label dan
        self.usporedbaDanLabel = QtWidgets.QLabel(self.vrijemeGridLayoutWidget)
        self.usporedbaDanLabel.setEnabled(False)
        self.usporedbaDanLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usporedbaDanLabel.setFont(font)
        self.usporedbaDanLabel.setObjectName("usporedbaDanLabel")
        self.usporedbaGL.addWidget(self.usporedbaDanLabel, 0, 0, 1, 1)
        # Label mjesec
        self.usporedbaMjesecLabel = QtWidgets.QLabel(self.vrijemeGridLayoutWidget)
        self.usporedbaMjesecLabel.setEnabled(False)
        self.usporedbaMjesecLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usporedbaMjesecLabel.setFont(font)
        self.usporedbaMjesecLabel.setObjectName("usporedbaMjesecLabel")
        self.usporedbaGL.addWidget(self.usporedbaMjesecLabel, 0, 1, 1, 1)
        # Label godina
        self.usporedbaGodinaLabel = QtWidgets.QLabel(self.vrijemeGridLayoutWidget)
        self.usporedbaGodinaLabel.setEnabled(False)
        self.usporedbaGodinaLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usporedbaGodinaLabel.setFont(font)
        self.usporedbaGodinaLabel.setObjectName("usporedbaGodinaLabel")
        self.usporedbaGL.addWidget(self.usporedbaGodinaLabel, 0, 2, 1, 1)
        self.vrijemeGridLayout.addLayout(self.usporedbaGL, 11, 0, 1, 1)
        ##### PRVI DAN #####
        # Spin box widget za odabir prvog dana usporedbe
        self.usporedbaDanPrvi = QtWidgets.QSpinBox(self.vrijemeGridLayoutWidget)
        self.usporedbaDanPrvi.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usporedbaDanPrvi.setFont(font)
        self.usporedbaDanPrvi.setMaximum(31)
        self.usporedbaDanPrvi.setProperty("value", 0)
        self.usporedbaDanPrvi.setObjectName("usporedbaDanPrvi")
        self.usporedbaGL.addWidget(self.usporedbaDanPrvi, 1, 0, 1, 1)
        # Spin box widget za odabir prvog mjeseca usporedbe
        self.usporedbaMjesecPrvi = QtWidgets.QSpinBox(self.vrijemeGridLayoutWidget)
        self.usporedbaMjesecPrvi.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usporedbaMjesecPrvi.setFont(font)
        self.usporedbaMjesecPrvi.setMaximum(12)
        self.usporedbaMjesecPrvi.setProperty("value", 0)
        self.usporedbaMjesecPrvi.setObjectName("usporedbaMjesecPrvi")
        self.usporedbaGL.addWidget(self.usporedbaMjesecPrvi, 1, 1, 1, 1)
        # Combo box widget za odabir prve godine usporedbe
        self.usporedbaGodinaPrvi = QtWidgets.QSpinBox(self.vrijemeGridLayoutWidget)
        self.usporedbaGodinaPrvi.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usporedbaGodinaPrvi.setFont(font)
        self.usporedbaGodinaPrvi.setMaximum(9999)
        self.usporedbaGodinaPrvi.setProperty("value", 2008)
        self.usporedbaGodinaPrvi.setObjectName("usporedbaGodinaPrvi")
        self.usporedbaGL.addWidget(self.usporedbaGodinaPrvi, 1, 2, 1, 1)
        ##### DRUGI DAN #####
        # Spin box widget za odabir drugog dana usporedbe
        self.usporedbaDanDrugi = QtWidgets.QSpinBox(self.vrijemeGridLayoutWidget)
        self.usporedbaDanDrugi.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usporedbaDanDrugi.setFont(font)
        self.usporedbaDanDrugi.setMaximum(31)
        self.usporedbaDanDrugi.setProperty("value", 0)
        self.usporedbaDanDrugi.setObjectName("usporedbaDanDrugi")
        self.usporedbaGL.addWidget(self.usporedbaDanDrugi, 2, 0, 1, 1)
        # Spin box widget za odabir drugog mjeseca usporedbe
        self.usporedbaMjesecDrugi = QtWidgets.QSpinBox(self.vrijemeGridLayoutWidget)
        self.usporedbaMjesecDrugi.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usporedbaMjesecDrugi.setFont(font)
        self.usporedbaMjesecDrugi.setMaximum(12)
        self.usporedbaMjesecDrugi.setProperty("value", 0)
        self.usporedbaMjesecDrugi.setObjectName("usporedbaMjesecDrugi")
        self.usporedbaGL.addWidget(self.usporedbaMjesecDrugi, 2, 1, 1, 1)
        # Combo box widget za odabir druge godine usporedbe
        self.usporedbaGodinaDrugi = QtWidgets.QSpinBox(self.vrijemeGridLayoutWidget)
        self.usporedbaGodinaDrugi.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.usporedbaGodinaDrugi.setFont(font)
        self.usporedbaGodinaDrugi.setMaximum(9999)
        self.usporedbaGodinaDrugi.setProperty("value", 2008)
        self.usporedbaGodinaDrugi.setObjectName("usporedbaGodinaDrugi")
        self.usporedbaGL.addWidget(self.usporedbaGodinaDrugi, 2, 2, 1, 1)
        ##################################################
        ##################################################


        #########################         #########################
        ######################### GRADOVI #########################
        # gradoviBox --> Group Box koji sadrži Check Boxes za gradove
        self.gradoviBox = QtWidgets.QGroupBox(self.centralwidget)
        # Pozicija widgeta i veličina
        self.gradoviBox.setGeometry(QtCore.QRect(600, 185, 200, 210))
        # Tekst
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.gradoviBox.setFont(font)
        self.gradoviBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gradoviBox.setAutoFillBackground(False)
        self.gradoviBox.setAlignment(QtCore.Qt.AlignCenter)
        self.gradoviBox.setObjectName("gradoviBox")

        # Vertikalni box koji sadrži vertikalni layout
        self.gradoviChecksLayoutBox = QtWidgets.QWidget(self.gradoviBox)
        self.gradoviChecksLayoutBox.setGeometry(QtCore.QRect(20, 30, 161, 161))
        self.gradoviChecksLayoutBox.setObjectName("gradoviChecksLayoutBox")
        # Vertikalni layout koji sadrži check boxes za gradove
        self.gradoviVerticalLayout = QtWidgets.QVBoxLayout(self.gradoviChecksLayoutBox)
        self.gradoviVerticalLayout.setContentsMargins(20, 0, 0, 0)
        self.gradoviVerticalLayout.setSpacing(0)
        self.gradoviVerticalLayout.setObjectName("gradoviVerticalLayout")

        # Check box 'Rijeka'
        self.checkBoxRijeka = QtWidgets.QCheckBox(self.gradoviChecksLayoutBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxRijeka.setFont(font)
        self.checkBoxRijeka.setObjectName("checkBoxRijeka")
        self.gradoviVerticalLayout.addWidget(self.checkBoxRijeka)

        # Check box 'Marcelji'
        self.checkBoxMarcelji = QtWidgets.QCheckBox(self.gradoviChecksLayoutBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxMarcelji.setFont(font)
        self.checkBoxMarcelji.setObjectName("checkBoxMarcelji")
        self.gradoviVerticalLayout.addWidget(self.checkBoxMarcelji)

        # Check box 'Matulji'
        self.checkBoxMatulji = QtWidgets.QCheckBox(self.gradoviChecksLayoutBox)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.checkBoxMatulji.setFont(font)
        self.checkBoxMatulji.setObjectName("checkBoxMatulji")
        self.gradoviVerticalLayout.addWidget(self.checkBoxMatulji)
        ##################################################
        ##################################################
        

        #########################                #########################
        ######################### CONFIRM BUTTON #########################
        # Confirm (prikazi podatke) button
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.openDataWindow())
        self.confirmButton.setGeometry(QtCore.QRect(350, 580, 150, 35))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.confirmButton.sizePolicy().hasHeightForWidth())
        self.confirmButton.setSizePolicy(sizePolicy)
        self.confirmButton.setMinimumSize(QtCore.QSize(150, 35))
        self.confirmButton.setMaximumSize(QtCore.QSize(150, 35))
        self.confirmButton.setObjectName("confirmButton")
        OptionsWindow.setCentralWidget(self.centralwidget)
        ##################################################
        ##################################################
        
        # Button click
        # self.confirmButton.clicked.connect(self.openDataWindow)

        # Menu
        self.menubar = QtWidgets.QMenuBar(OptionsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 850, 31))
        self.menubar.setObjectName("menubar")
        OptionsWindow.setMenuBar(self.menubar)
        # Status
        self.statusbar = QtWidgets.QStatusBar(OptionsWindow)
        self.statusbar.setObjectName("statusbar")
        OptionsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(OptionsWindow)
        self.danRadio.toggled['bool'].connect(self.pickDan.setEnabled)
        self.mjesecRadio.toggled['bool'].connect(self.pickMjesecMjesec.setEnabled)
        self.mjesecRadio.toggled['bool'].connect(self.pickMjesecGodina.setEnabled)
        self.godinaRadio.toggled['bool'].connect(self.pickGodina.setEnabled)
        self.rasponRadio.toggled['bool'].connect(self.rasponOdLabel.setEnabled)
        self.rasponRadio.toggled['bool'].connect(self.rasponOd.setEnabled)
        self.rasponRadio.toggled['bool'].connect(self.rasponDoLabel.setEnabled)
        self.rasponRadio.toggled['bool'].connect(self.rasponDo.setEnabled)
        self.usporedbaRadio.toggled['bool'].connect(self.usporedbaDanPrvi.setEnabled)
        self.usporedbaRadio.toggled['bool'].connect(self.usporedbaMjesecPrvi.setEnabled)
        self.usporedbaRadio.toggled['bool'].connect(self.usporedbaGodinaPrvi.setEnabled)
        self.usporedbaRadio.toggled['bool'].connect(self.usporedbaDanDrugi.setEnabled)
        self.usporedbaRadio.toggled['bool'].connect(self.usporedbaMjesecDrugi.setEnabled)
        self.usporedbaRadio.toggled['bool'].connect(self.usporedbaGodinaDrugi.setEnabled)
        self.usporedbaRadio.toggled['bool'].connect(self.usporedbaDanLabel.setEnabled)
        self.usporedbaRadio.toggled['bool'].connect(self.usporedbaMjesecLabel.setEnabled)
        self.usporedbaRadio.toggled['bool'].connect(self.usporedbaGodinaLabel.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(OptionsWindow)
        OptionsWindow.setTabOrder(self.danRadio, self.mjesecRadio)
        OptionsWindow.setTabOrder(self.mjesecRadio, self.godinaRadio)
        OptionsWindow.setTabOrder(self.godinaRadio, self.rasponRadio)
        OptionsWindow.setTabOrder(self.rasponRadio, self.checkBoxRijeka)
        OptionsWindow.setTabOrder(self.checkBoxRijeka, self.checkBoxMarcelji)
        OptionsWindow.setTabOrder(self.checkBoxMarcelji, self.checkBoxMatulji)
        OptionsWindow.setTabOrder(self.checkBoxMatulji, self.pickDan)
        OptionsWindow.setTabOrder(self.pickDan, self.pickMjesecMjesec)
        OptionsWindow.setTabOrder(self.pickMjesecMjesec, self.pickMjesecGodina)
        OptionsWindow.setTabOrder(self.pickMjesecGodina, self.pickGodina)
        OptionsWindow.setTabOrder(self.pickGodina, self.rasponOd)
        OptionsWindow.setTabOrder(self.rasponOd, self.rasponDo)

    def retranslateUi(self, OptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        OptionsWindow.setWindowTitle(_translate("OptionsWindow", "Analiza oborina"))
        self.gradoviBox.setTitle(_translate("OptionsWindow", "Cities"))
        self.checkBoxRijeka.setText(_translate("OptionsWindow", "Rijeka"))
        self.checkBoxMarcelji.setText(_translate("OptionsWindow", "Marčelji"))
        self.checkBoxMatulji.setText(_translate("OptionsWindow", "Matulji"))
        self.vrijemeBox.setTitle(_translate("OptionsWindow", "Time period"))
        self.pickDan.setDisplayFormat(_translate("OptionsWindow", "dd.MM.yyyy."))
        self.rasponRadio.setText(_translate("OptionsWindow", "Range"))
        self.mjesecRadio.setText(_translate("OptionsWindow", "Month"))
        self.godinaRadio.setText(_translate("OptionsWindow", "Year"))
        self.rasponOdLabel.setText(_translate("OptionsWindow", "From:"))
        self.rasponOd.setDisplayFormat(_translate("OptionsWindow", "dd.MM.yyyy."))
        self.rasponDoLabel.setText(_translate("OptionsWindow", "To:"))
        self.rasponDo.setDisplayFormat(_translate("OptionsWindow", "dd.MM.yyyy."))
        self.danRadio.setText(_translate("OptionsWindow", "Day"))
        self.usporedbaRadio.setText(_translate("OptionsWindow", "Comparison"))
        self.usporedbaDanLabel.setText(_translate("OptionsWindow", "Day"))
        self.usporedbaMjesecLabel.setText(_translate("OptionsWindow", "Month"))
        self.usporedbaGodinaLabel.setText(_translate("OptionsWindow", "Year"))
        self.confirmButton.setText(_translate("OptionsWindow", "Show data"))

    def openDataWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_GraphWindow()
        self.ui.setupUi(self.window)

        gradovi = []
        if self.checkBoxRijeka.isChecked():
            gradovi.append("Rijeka")
        if self.checkBoxMarcelji.isChecked():
            gradovi.append("Marcelji")
        if self.checkBoxMatulji.isChecked():
            gradovi.append("Matulji")

        numGradovi = len(gradovi)
        dataset_1 = []
        dataset_2 = []
        dataset_3 = []

        if numGradovi >= 1: 
            dataset_1 = do.load_dataset("data/" + gradovi[0] + ".csv", gradovi[0])
        if numGradovi >= 2:
            dataset_2 = do.load_dataset("data/" + gradovi[1] + ".csv", gradovi[1])
        if numGradovi == 3:
            dataset_3 = do.load_dataset("data/" + gradovi[2] + ".csv", gradovi[2])

        if self.danRadio.isChecked():
            gt.get_dan_data(self, dataset_1, dataset_2, dataset_3, gradovi)

        if self.mjesecRadio.isChecked():
            gt.month_data(self, dataset_1, dataset_2, dataset_3, gradovi)

        if self.godinaRadio.isChecked():
            gt.year_data(self, dataset_1, dataset_2, dataset_3, gradovi)

        if self.rasponRadio.isChecked():
            gt.range_data(self, dataset_1, dataset_2, dataset_3, gradovi)

        if self.usporedbaRadio.isChecked():
            gt.compare_data(self, dataset_1, gradovi[0])

        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OptionsWindow = QtWidgets.QMainWindow()
    ui = Ui_OptionsWindow()
    ui.setupUi(OptionsWindow)
    OptionsWindow.show()
    sys.exit(app.exec_())
