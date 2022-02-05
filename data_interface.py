# -*- coding: utf-8 -*-

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
        GraphWindow.setWindowIcon(QtGui.QIcon('icon_t.png'))
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
        ##################################################
        ##################################################


        #########################         #########################
        ######################### PODATCI #########################
        # Grid Frame --> sadrži grid layout
        self.gridFrame = QtWidgets.QFrame(self.centralwidget)
        self.gridFrame.setGeometry(QtCore.QRect(50, 500, 800, 230))
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
        self.labelDay.setEnabled(False)
        self.gridLayout.addWidget(self.labelDay, 1, 0, 1, 1)
        # Value day blue
        self.valueDayB = QtWidgets.QLabel(self.gridFrame)
        self.valueDayB.setObjectName("valueDayB")
        self.valueDayB.setStyleSheet("color: rgb(77, 148, 255)")
        self.valueDayB.setEnabled(False)
        self.gridLayout.addWidget(self.valueDayB, 1, 1, 1, 1)
        # Value day red 
        self.valueDayR = QtWidgets.QLabel(self.gridFrame)
        self.valueDayR.setObjectName("valueDayR")
        self.valueDayR.setStyleSheet("color: rgb(255, 102, 102)")
        self.gridLayout.addWidget(self.valueDayR, 1, 2, 1, 1)
        # Value day green
        self.valueDayG = QtWidgets.QLabel(self.gridFrame)
        self.valueDayG.setObjectName("valueDayG")
        self.valueDayG.setStyleSheet("color: rgb(73, 158, 33)")
        self.gridLayout.addWidget(self.valueDayG, 1, 3, 1, 1)

        # Label M sum
        self.labelMsum = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelMsum.setFont(font)
        self.labelMsum.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelMsum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMsum.setObjectName("labelMsum")
        self.labelMsum.setEnabled(False)
        self.gridLayout.addWidget(self.labelMsum, 3, 0, 1, 1)
        # Value Month sum blue
        self.valueMsumB = QtWidgets.QLabel(self.gridFrame)
        self.valueMsumB.setObjectName("valueMsumB")
        self.valueMsumB.setStyleSheet("color: rgb(77, 148, 255)")
        self.valueMsumB.setEnabled(False)
        self.gridLayout.addWidget(self.valueMsumB, 3, 1, 1, 1)
        # Value Month sum red
        self.valueMsumR = QtWidgets.QLabel(self.gridFrame)
        self.valueMsumR.setObjectName("valueMsumR")
        self.valueMsumR.setStyleSheet("color: rgb(255, 102, 102)")
        self.gridLayout.addWidget(self.valueMsumR, 3, 2, 1, 1)
        # Value Month sum green
        self.valueMsumG = QtWidgets.QLabel(self.gridFrame)
        self.valueMsumG.setObjectName("valueMsumG")
        self.valueMsumG.setStyleSheet("color: rgb(73, 158, 33)")
        self.gridLayout.addWidget(self.valueMsumG, 3, 3, 1, 1)

        # Label Year sum
        self.labelYsum = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelYsum.setFont(font)
        self.labelYsum.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelYsum.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelYsum.setObjectName("labelYsum")
        self.labelYsum.setEnabled(False)
        self.gridLayout.addWidget(self.labelYsum, 6, 0, 1, 1)
        # Value Year sum blue
        self.valueYsumB = QtWidgets.QLabel(self.gridFrame)
        self.valueYsumB.setObjectName("valueYsumB")
        self.valueYsumB.setStyleSheet("color: rgb(77, 148, 255)")
        self.valueYsumB.setEnabled(False)
        self.gridLayout.addWidget(self.valueYsumB, 6, 1, 1, 1)
        # Value Year sum red
        self.valueYsumR = QtWidgets.QLabel(self.gridFrame)
        self.valueYsumR.setObjectName("valueYsumR")
        self.valueYsumR.setStyleSheet("color: rgb(255, 102, 102)")
        self.gridLayout.addWidget(self.valueYsumR, 6, 2, 1, 1)
        # Value Year sum green
        self.valueYsumG = QtWidgets.QLabel(self.gridFrame)
        self.valueYsumG.setObjectName("valueYsumG")
        self.valueYsumG.setStyleSheet("color: rgb(73, 158, 33)")
        self.gridLayout.addWidget(self.valueYsumG, 6, 3, 1, 1)

        # Label Month max
        self.labelMmax = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelMmax.setFont(font)
        self.labelMmax.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelMmax.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelMmax.setObjectName("labelMmax")
        self.labelMmax.setEnabled(False)
        self.gridLayout.addWidget(self.labelMmax, 2, 0, 1, 1)
        # Value Month max blue
        self.valueMmaxB = QtWidgets.QLabel(self.gridFrame)
        self.valueMmaxB.setObjectName("valueMmaxB")
        self.valueMmaxB.setStyleSheet("color: rgb(77, 148, 255)")
        self.valueMmaxB.setEnabled(False)
        self.gridLayout.addWidget(self.valueMmaxB, 2, 1, 1, 1)
        # Value Month max red
        self.valueMmaxR = QtWidgets.QLabel(self.gridFrame)
        self.valueMmaxR.setObjectName("valueMaxR")
        self.valueMmaxR.setStyleSheet("color: rgb(255, 102, 102)")
        self.gridLayout.addWidget(self.valueMmaxR, 2, 2, 1, 1)
        # Value Month max green
        self.valueMmaxG = QtWidgets.QLabel(self.gridFrame)
        self.valueMmaxG.setObjectName("valueMmaxG")
        self.valueMmaxG.setStyleSheet("color: rgb(73, 158, 33)")
        self.gridLayout.addWidget(self.valueMmaxG, 2, 3, 1, 1)

        # Label Year Day max
        self.labelYmax = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelYmax.setFont(font)
        self.labelYmax.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelYmax.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelYmax.setObjectName("labelYmax")
        self.labelYmax.setEnabled(False)
        self.gridLayout.addWidget(self.labelYmax, 4, 0, 1, 1)
        # Value Year Day max blue
        self.valueYmaxB = QtWidgets.QLabel(self.gridFrame)
        self.valueYmaxB.setObjectName("valueYmaxB")
        self.valueYmaxB.setStyleSheet("color: rgb(77, 148, 255)")
        self.valueYmaxB.setEnabled(False)
        self.gridLayout.addWidget(self.valueYmaxB, 4, 1, 1, 1)
        # Value Year Day max red
        self.valueYmaxR = QtWidgets.QLabel(self.gridFrame)
        self.valueYmaxR.setObjectName("valueYmaxR")
        self.valueYmaxR.setStyleSheet("color: rgb(255, 102, 102)")
        self.gridLayout.addWidget(self.valueYmaxR, 4, 2, 1, 1)
        # Value Year Day sum green
        self.valueYmaxG = QtWidgets.QLabel(self.gridFrame)
        self.valueYmaxG.setObjectName("valueYmaxG")
        self.valueYmaxG.setStyleSheet("color: rgb(73, 158, 33)")
        self.gridLayout.addWidget(self.valueYmaxG, 4, 3, 1, 1)

        # Label Year Month max
        self.labelYmax_month = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelYmax_month.setFont(font)
        self.labelYmax_month.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.labelYmax_month.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelYmax_month.setObjectName("labelYmax_month")
        self.labelYmax_month.setEnabled(False)
        self.gridLayout.addWidget(self.labelYmax_month, 5, 0, 1, 1)
        # Value Year Month max blue
        self.valueYmax_monthB = QtWidgets.QLabel(self.gridFrame)
        self.valueYmax_monthB.setObjectName("valueYmax_monthB")
        self.valueYmax_monthB.setStyleSheet("color: rgb(77, 148, 255)")
        self.valueYmax_monthB.setEnabled(False)
        self.gridLayout.addWidget(self.valueYmax_monthB, 5, 1, 1, 1)
        # Value Year Month max red
        self.valueYmax_monthR = QtWidgets.QLabel(self.gridFrame)
        self.valueYmax_monthR.setObjectName("valueYmax_monthR")
        self.valueYmax_monthR.setStyleSheet("color: rgb(255, 102, 102)")
        self.gridLayout.addWidget(self.valueYmax_monthR, 5, 2, 1, 1)
        # Value Year Month sum green
        self.valueYmax_monthG = QtWidgets.QLabel(self.gridFrame)
        self.valueYmax_monthG.setObjectName("valueYmax_monthG")
        self.valueYmax_monthG.setStyleSheet("color: rgb(73, 158, 33)")
        self.gridLayout.addWidget(self.valueYmax_monthG, 5, 3, 1, 1)

        # Label raspon max
        self.labelRasponMax = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelRasponMax.setFont(font)
        self.labelRasponMax.setObjectName("labelRasponMax")
        self.labelRasponMax.setEnabled(False)
        self.gridLayout.addWidget(self.labelRasponMax, 7, 0, 1, 1)
        # Value raspon max blue
        self.valueRasponMaxB = QtWidgets.QLabel(self.gridFrame)
        self.valueRasponMaxB.setObjectName("valueRasponMaxB")
        self.valueRasponMaxB.setStyleSheet("color: rgb(77, 148, 255)")
        self.gridLayout.addWidget(self.valueRasponMaxB, 7, 1, 1, 1)
        # Value raspon max red
        self.valueRasponMaxR = QtWidgets.QLabel(self.gridFrame)
        self.valueRasponMaxR.setObjectName("valueRasponMaxR")
        self.valueRasponMaxR.setStyleSheet("color: rgb(255, 102, 102)")
        self.gridLayout.addWidget(self.valueRasponMaxR, 7, 2, 1, 1)
        # Value raspon max green
        self.valueRasponMaxG = QtWidgets.QLabel(self.gridFrame)
        self.valueRasponMaxG.setObjectName("valueRasponMaxG")
        self.valueRasponMaxG.setStyleSheet("color: rgb(73, 158, 33)")
        self.gridLayout.addWidget(self.valueRasponMaxG, 7, 3, 1, 1)

        # Label raspon sum
        self.labelRasponSum = QtWidgets.QLabel(self.gridFrame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelRasponSum.setFont(font)
        self.labelRasponSum.setObjectName("labelRasponSum")
        self.labelRasponSum.setEnabled(False)
        self.gridLayout.addWidget(self.labelRasponSum, 8, 0, 1, 1)
        # Value raspon sum blue
        self.valueRasponSumB = QtWidgets.QLabel(self.gridFrame)
        self.valueRasponSumB.setObjectName("valueRasponSumB")
        self.valueRasponSumB.setStyleSheet("color: rgb(77, 148, 255)")
        self.gridLayout.addWidget(self.valueRasponSumB, 8, 1, 1, 1)
        # Value raspon sum red
        self.valueRasponSumR = QtWidgets.QLabel(self.gridFrame)
        self.valueRasponSumR.setObjectName("valueRasponSumR")
        self.valueRasponSumR.setStyleSheet("color: rgb(255, 102, 102)")
        self.gridLayout.addWidget(self.valueRasponSumR, 8, 2, 1, 1)
        # Value raspon sum green
        self.valueRasponSumG = QtWidgets.QLabel(self.gridFrame)
        self.valueRasponSumG.setObjectName("valueRasponSumG")
        self.valueRasponSumG.setStyleSheet("color: rgb(73, 158, 33)")
        self.gridLayout.addWidget(self.valueRasponSumG, 8, 3, 1, 1)
        ##################################################
        ##################################################


        # Menu
        self.menubar = QtWidgets.QMenuBar(GraphWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 31))
        self.menubar.setObjectName("menubar")
        GraphWindow.setMenuBar(self.menubar)
        # Status
        self.statusbar = QtWidgets.QStatusBar(GraphWindow)
        self.statusbar.setObjectName("statusbar")
        GraphWindow.setStatusBar(self.statusbar)

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "Analiza oborina"))
        self.labelDay.setText(_translate("GraphWindow", "Day value:"))

        self.labelMmax.setText(_translate("GraphWindow", "Month max day:"))
        self.labelMsum.setText(_translate("GraphWindow", "Month sum:"))

        self.labelYmax.setText(_translate("GraphWindow", "Year max day:"))
        self.labelYmax_month.setText(_translate("GraphWindow", "Year max month:"))
        self.labelYsum.setText(_translate("GraphWindow", "Year sum:"))
        
        self.labelRasponMax.setText(_translate("GraphWindow", "Range max day:"))
        self.labelRasponSum.setText(_translate("GraphWindow", "Range sum:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GraphWindow = QtWidgets.QMainWindow()
    ui = Ui_GraphWindow()
    ui.setupUi(GraphWindow)
    GraphWindow.show()
    sys.exit(app.exec_())

