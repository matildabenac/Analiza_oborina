# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_graph_data_design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
import pyqtgraph as pg
import visualization

def get_points_array(i):
    x = np.arange(0, 2 * i + 10, 0.1)
    y1 = x * np.sin(x) * np.exp(-x)
    y2 = x * np.sin(x)
    y3 = x * np.cos(x)
    return x, y1, y2, y3

class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.setEnabled(True)
        GraphWindow.resize(1000, 810)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GraphWindow.sizePolicy().hasHeightForWidth())
        GraphWindow.setSizePolicy(sizePolicy)
        GraphWindow.setMinimumSize(QtCore.QSize(1000, 810))
        GraphWindow.setMaximumSize(QtCore.QSize(1000, 810))
        GraphWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(GraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        GraphWindow.setCentralWidget(self.centralwidget)

        #########################       #########################
        ######################### SLIKA #########################
        # Graf --> slika
        #self.Graf = QtWidgets.QGraphicsView(self.centralwidget)
        self.Graf = PlotWidget(self.centralwidget)
        self.Graf.setGeometry(QtCore.QRect(50, 50, 900, 400))
        self.Graf.setMaximumSize(QtCore.QSize(900, 16777215))
        self.Graf.setObjectName("Graf")
        self.Graf.setBackground('w')

        self.pen_1 = pg.mkPen(color=(77, 148, 255), width=3)
        self.pen_2 = pg.mkPen(color=(255, 102, 102), width=3)
        self.pen_3 = pg.mkPen(color=(73, 158, 33), width=3)

        #x = np.random.normal(size=20)
        #y = np.random.normal(size=20)
        #self.Graf.plot(x,y)
        ##################################################
        ##################################################


        #########################         #########################
        ######################### PODATCI #########################
        # Grid Frame --> sadrži grid layout
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(50, 500, 250, 230))
        self.gridFrame.setObjectName("gridFrame")
        # Grid layout --> sadrži labels
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")

        # Label day
        self.labelDay = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDay.setFont(font)
        self.labelDay.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelDay.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelDay.setObjectName("labelDay")
        self.gridLayout.addWidget(self.labelDay, 1, 0, 1, 1)
        # Value day
        self.valueDay = QtWidgets.QLabel(self.gridFrame)
        self.valueDay.setObjectName("valueDay")
        self.gridLayout.addWidget(self.valueDay, 1, 1, 1, 1)

        # Label M sum
        self.labelMsum = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelMsum.setFont(font)
        self.labelMsum.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelMsum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMsum.setObjectName("labelMsum")
        self.gridLayout.addWidget(self.labelMsum, 3, 0, 1, 1)
        # Value Month sum
        self.valueMsum = QtWidgets.QLabel(self.gridFrame)
        self.valueMsum.setObjectName("valueMsum")
        self.gridLayout.addWidget(self.valueMsum, 3, 1, 1, 1)

        # Label Year sum
        self.labelYsum = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelYsum.setFont(font)
        self.labelYsum.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelYsum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelYsum.setObjectName("labelYsum")
        self.gridLayout.addWidget(self.labelYsum, 5, 0, 1, 1)
        # Value Year sum
        self.valueYsum = QtWidgets.QLabel(self.gridFrame)
        self.valueYsum.setObjectName("valueYsum")
        self.gridLayout.addWidget(self.valueYsum, 5, 1, 1, 1)

        # Label Month max
        self.labelMmax = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelMmax.setFont(font)
        self.labelMmax.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelMmax.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMmax.setObjectName("labelMmax")
        self.gridLayout.addWidget(self.labelMmax, 2, 0, 1, 1)
        # Value Month max
        self.valueMmax = QtWidgets.QLabel(self.gridFrame)
        self.valueMmax.setObjectName("valueMmonth")
        self.gridLayout.addWidget(self.valueMmax, 2, 1, 1, 1)

        # Label Year max
        self.labelYmax = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelYmax.setFont(font)
        self.labelYmax.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelYmax.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelYmax.setObjectName("labelYmax")
        self.gridLayout.addWidget(self.labelYmax, 4, 0, 1, 1)
        # Value Year max
        self.valueYmax = QtWidgets.QLabel(self.gridFrame)
        self.valueYmax.setObjectName("valueYmax")
        self.gridLayout.addWidget(self.valueYmax, 4, 1, 1, 1)

        # Label sumarna razlika
        self.labelDif = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDif.setFont(font)
        self.labelDif.setObjectName("labelDif")
        self.gridLayout.addWidget(self.labelDif, 6, 0, 1, 1)
        # Value sumarna razlika
        self.valueDif = QtWidgets.QLabel(self.gridFrame)
        self.valueDif.setObjectName("valueDif")
        self.gridLayout.addWidget(self.valueDif, 6, 1, 1, 1)
        ##################################################
        ##################################################


        # Menu
        self.menubar = QtWidgets.QMenuBar(GraphWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 31))
        self.menubar.setObjectName("menubar")
        self.menuExport = QtWidgets.QMenu(self.menubar)
        self.menuExport.setObjectName("menuExport")
        GraphWindow.setMenuBar(self.menubar)
        # Status
        self.statusbar = QtWidgets.QStatusBar(GraphWindow)
        self.statusbar.setObjectName("statusbar")
        GraphWindow.setStatusBar(self.statusbar)

        # Menu save only graph
        self.actionGraph = QtWidgets.QAction(GraphWindow)
        self.actionGraph.setCheckable(False)
        self.actionGraph.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionGraph.setObjectName("actionGraph")
        # Menu save only data
        self.actionData = QtWidgets.QAction(GraphWindow)
        self.actionData.setObjectName("actionData")
        # Menu save all
        self.actionAll = QtWidgets.QAction(GraphWindow)
        self.actionAll.setObjectName("actionAll")
        
        self.menuExport.addAction(self.actionGraph)
        self.menuExport.addAction(self.actionData)
        self.menuExport.addAction(self.actionAll)
        self.menubar.addAction(self.menuExport.menuAction())

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "MainWindow"))
        self.labelDay.setText(_translate("GraphWindow", "Vrijednost za dan:"))
        self.valueDay.setText(_translate("GraphWindow", "-"))
        self.labelMmax.setText(_translate("GraphWindow", "Mjesec maksimum:"))
        self.labelYsum.setText(_translate("GraphWindow", "Godina suma:"))
        self.valueYsum.setText(_translate("GraphWindow", "-"))
        self.labelMsum.setText(_translate("GraphWindow", "Mjesec suma:"))
        self.valueMmax.setText(_translate("GraphWindow", "-"))
        self.labelYmax.setText(_translate("GraphWindow", "Godina maksimum:"))
        self.valueYmax.setText(_translate("GraphWindow", "-"))
        self.valueMsum.setText(_translate("GraphWindow", "-"))
        self.labelDif.setText(_translate("GraphWindow", "Sumarna razlika:"))
        self.valueDif.setText(_translate("GraphWindow", "-"))
        self.menuExport.setTitle(_translate("GraphWindow", "Export"))
        self.actionGraph.setText(_translate("GraphWindow", "Graph"))
        self.actionGraph.setToolTip(_translate("GraphWindow", "Graph"))
        self.actionGraph.setStatusTip(_translate("GraphWindow", "Save only graph"))
        self.actionGraph.setShortcut(_translate("GraphWindow", "Ctrl+G"))
        self.actionData.setText(_translate("GraphWindow", "Data"))
        self.actionData.setStatusTip(_translate("GraphWindow", "Save only data"))
        self.actionData.setShortcut(_translate("GraphWindow", "Ctrl+D"))
        self.actionAll.setText(_translate("GraphWindow", "All"))
        self.actionAll.setStatusTip(_translate("GraphWindow", "Save all"))
        self.actionAll.setShortcut(_translate("GraphWindow", "Ctrl+A"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GraphWindow = QtWidgets.QMainWindow()
    ui = Ui_GraphWindow()
    ui.setupUi(GraphWindow)
    GraphWindow.show()
    sys.exit(app.exec_())

