# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'final_graph_data_design.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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

        # Grid Frame --> sadrži grid layout
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(50, 500, 250, 230))
        self.gridFrame.setObjectName("gridFrame")
        # Grid layout --> sadrži labels
        self.gridLayout = QtWidgets.QGridLayout(self.gridFrame)
        self.gridLayout.setObjectName("gridLayout")

        # Label Month max
        self.labelMmax = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelMmax.setFont(font)
        self.labelMmax.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelMmax.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMmax.setObjectName("labelMmax")
        self.gridLayout.addWidget(self.labelMmax, 3, 0, 1, 1)

        # Label Year sum
        self.labelYsum = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelYsum.setFont(font)
        self.labelYsum.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelYsum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelYsum.setObjectName("labelYsum")
        self.gridLayout.addWidget(self.labelYsum, 2, 0, 1, 1)

        # Value Year sum
        self.valueYsum = QtWidgets.QLabel(self.gridFrame)
        self.valueYsum.setObjectName("valueYsum")
        self.gridLayout.addWidget(self.valueYsum, 2, 1, 1, 1)

        # Label M sum
        self.labelMsum = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelMsum.setFont(font)
        self.labelMsum.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelMsum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMsum.setObjectName("labelMsum")
        self.gridLayout.addWidget(self.labelMsum, 1, 0, 1, 1)

        # Value Month max
        self.valueMmonth = QtWidgets.QLabel(self.gridFrame)
        self.valueMmonth.setObjectName("valueMmonth")
        self.gridLayout.addWidget(self.valueMmonth, 3, 1, 1, 1)

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

        # Value Month sum
        self.valueMsum = QtWidgets.QLabel(self.gridFrame)
        self.valueMsum.setObjectName("valueMsum")
        self.gridLayout.addWidget(self.valueMsum, 1, 1, 1, 1)

        # Label sumarna razlika
        self.labelDif = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelDif.setFont(font)
        self.labelDif.setObjectName("labelDif")
        self.gridLayout.addWidget(self.labelDif, 5, 0, 1, 1)

        # Value sumarna razlika
        self.valueDif = QtWidgets.QLabel(self.gridFrame)
        self.valueDif.setObjectName("valueDif")
        self.gridLayout.addWidget(self.valueDif, 5, 1, 1, 1)

        # Graf --> slika
        self.Graf = QtWidgets.QGraphicsView(self.centralwidget)
        self.Graf.setGeometry(QtCore.QRect(50, 50, 600, 400))
        self.Graf.setMaximumSize(QtCore.QSize(800, 16777215))
        self.Graf.setObjectName("Graf")
        GraphWindow.setCentralWidget(self.centralwidget)

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
        self.labelMmax.setText(_translate("GraphWindow", "Maksimum mjesec:"))
        self.labelYsum.setText(_translate("GraphWindow", "Godišnje sume:"))
        self.valueYsum.setText(_translate("GraphWindow", "50"))
        self.labelMsum.setText(_translate("GraphWindow", "Mjesečne sume:"))
        self.valueMmonth.setText(_translate("GraphWindow", "100"))
        self.labelYmax.setText(_translate("GraphWindow", "Maksimum godina:"))
        self.valueYmax.setText(_translate("GraphWindow", "500"))
        self.valueMsum.setText(_translate("GraphWindow", "20"))
        self.labelDif.setText(_translate("GraphWindow", "Sumarna razlika:"))
        self.valueDif.setText(_translate("GraphWindow", "25"))
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

