import numpy as np
import data_operations as do
import visualization as plot
import pyqtgraph as pg

def get_dan_data(graf, dataset_1, dataset_2, dataset_3, gradovi):
        datum = graf.pickDan.text().split('.')

        graf.ui.labelDay.setEnabled(True)
        graf.ui.valueDayB.setEnabled(True)

        x = []
        y = []

        if dataset_1:
                value_1 = do.get_day_value(gradovi[0], int(datum[0]), int(datum[1]), int(datum[2]))
                graf.ui.grad_1.setText(gradovi[0])
                graf.ui.valueDayB.setText(str(value_1))
                x.append(1)
                y.append(value_1)
        if dataset_2:
                value_2 = do.get_day_value(gradovi[1], int(datum[0]), int(datum[1]), int(datum[2]))
                graf.ui.grad_2.setText(gradovi[1])
                graf.ui.valueDayR.setText(str(value_2))
                x.append(2)
                y.append(value_2)
        if dataset_3:
                value_3 = do.get_day_value(gradovi[2], int(datum[0]), int(datum[1]), int(datum[2]))
                graf.ui.grad_3.setText(gradovi[2])
                graf.ui.valueDayG.setText(str(value_3))
                x.append(3)
                y.append(value_3)

        title = "Rain for day: " + str(datum[0]) + "." + str(datum[1]) + "." + str(datum[2]) + "."
        yLabel = "Daily rain"

        #print(x)
        #print(y)

        bar_graph(graf, title, yLabel, x, y, len(x))

# Mjesec za 1 grad
def get_mjesec_data(graf, dataset, gradovi):
        mjesec = graf.pickMjesecMjesec.value()
        godina = graf.pickMjesecGodina.value()

        sumM = do.get_month_sum(dataset, godina, mjesec)
        max_day, maxM = do.get_max_day_in_month(dataset, godina, mjesec)

        graf.ui.labelMsum.setEnabled(True)
        graf.ui.valueMsumB.setEnabled(True)
        graf.ui.labelMmax.setEnabled(True)
        graf.ui.valueMmaxB.setEnabled(True)

        graf.ui.valueMsumB.setText(str(sumM))
        graf.ui.valueMmaxB.setText(str(maxM) + " (" + str(max_day) + "." + str(mjesec) + ".)")

        title = "Rain for month: " + str(mjesec) + "." + str(godina) + "."
        xLabel = "Days"
        yLabel = "Daily rain"
        xyRange = (0.5, 31.5)
        #print(gradovi[0])
        x, y = plot.month_plot(gradovi[0], mjesec, godina)
        create_graph(graf, title, xLabel, yLabel, xyRange, x, y, 1, gradovi)

# Mjesec za 2 grada
def compare_mjesec_data_two(graf, dataset_1, dataset_2, gradovi):
        mjesec = graf.pickMjesecMjesec.value()
        godina = graf.pickMjesecGodina.value()
        sumM_1 = do.get_month_sum(dataset_1, godina, mjesec)
        sumM_2 = do.get_month_sum(dataset_2, godina, mjesec)
        max_day_1, maxM_1 = do.get_max_day_in_month(dataset_1, godina, mjesec)
        max_day_2, maxM_2 = do.get_max_day_in_month(dataset_2, godina, mjesec)

        graf.ui.labelMsum.setEnabled(True)
        graf.ui.valueMsumB.setEnabled(True)
        graf.ui.labelMmax.setEnabled(True)
        graf.ui.valueMmaxB.setEnabled(True)

        graf.ui.valueMsumB.setText(str(sumM_1))
        graf.ui.valueMsumR.setText(str(sumM_2))
        graf.ui.valueMmaxB.setText(str(maxM_1) + " (" + str(max_day_1) + "." + str(mjesec) + ".)")
        graf.ui.valueMmaxR.setText(str(maxM_2) + " (" + str(max_day_2) + "." + str(mjesec) + ".)")

        title = "Rain for month: " + str(mjesec) + "." + str(godina) + "."
        xLabel = "Days"
        yLabel = "Daily rain"
        xyRange = (0.5, 31.5)
        x_1, y_1 = plot.month_plot(gradovi[0], mjesec, godina)
        x_2, y_2 = plot.month_plot(gradovi[1], mjesec, godina)
        create_graph(graf, title, xLabel, yLabel, xyRange, x_1, y_1, 1, gradovi)
        create_graph(graf, title, xLabel, yLabel, xyRange, x_2, y_2, 2, gradovi)

# Mjesec za 3 grada
def month_data(graf, dataset_1, dataset_2, dataset_3, gradovi):
        mjesec = graf.pickMjesecMjesec.value()
        godina = graf.pickMjesecGodina.value()

        graf.ui.labelMsum.setEnabled(True)
        graf.ui.valueMsumB.setEnabled(True)
        graf.ui.labelMmax.setEnabled(True)
        graf.ui.valueMmaxB.setEnabled(True)

        title = "Rain for month: " + str(mjesec) + "." + str(godina) + "."
        xLabel = "Days"
        yLabel = "Daily rain"
        xyRange = (0.5, 31.5)

        if dataset_1:
                sumM_1 = do.get_month_sum(dataset_1, godina, mjesec)
                max_day_1, maxM_1 = do.get_max_day_in_month(dataset_1, godina, mjesec)
                graf.ui.valueMsumB.setText(str(sumM_1))
                graf.ui.valueMmaxB.setText(str(maxM_1) + " (" + str(max_day_1) + "." + str(mjesec) + ".)")
                x_1, y_1 = plot.month_plot(gradovi[0], mjesec, godina)
                create_graph(graf, title, xLabel, yLabel, xyRange, x_1, y_1, 1, gradovi)

        if dataset_2:
                sumM_2 = do.get_month_sum(dataset_2, godina, mjesec)
                max_day_2, maxM_2 = do.get_max_day_in_month(dataset_2, godina, mjesec)
                graf.ui.valueMsumR.setText(str(sumM_2))
                graf.ui.valueMmaxR.setText(str(maxM_2) + " (" + str(max_day_2) + "." + str(mjesec) + ".)")
                x_2, y_2 = plot.month_plot(gradovi[1], mjesec, godina)
                create_graph(graf, title, xLabel, yLabel, xyRange, x_2, y_2, 2, gradovi)

        if dataset_3:
                sumM_3 = do.get_month_sum(dataset_3, godina, mjesec)
                max_day_3, maxM_3 = do.get_max_day_in_month(dataset_3, godina, mjesec)
                graf.ui.valueMsumG.setText(str(sumM_3))
                graf.ui.valueMmaxG.setText(str(maxM_3) + " (" + str(max_day_3) + "." + str(mjesec) + ".)")
                x_3, y_3 = plot.month_plot(gradovi[2], mjesec, godina)
                create_graph(graf, title, xLabel, yLabel, xyRange, x_3, y_3, 3, gradovi)

# Godina za 1 grad
def get_godina_data(graf, dataset, gradovi):
        godina = graf.pickGodina.value()
        sumY = do.get_year_sum(dataset, godina)
        max_month, max_day, maxY = do.get_max_day_in_year(dataset, godina)
        max_month_month, maxY_month = do.get_max_month_in_year(dataset, godina)

        graf.ui.labelYsum.setEnabled(True)
        graf.ui.valueYsumB.setEnabled(True)
        graf.ui.labelYmax.setEnabled(True)
        graf.ui.valueYmaxB.setEnabled(True)
        graf.ui.labelYmax_month.setEnabled(True)
        graf.ui.valueYmax_monthB.setEnabled(True)

        graf.ui.valueYsumB.setText(str(sumY))
        graf.ui.valueYmax_monthB.setText(str(maxY_month) + " (" + str(max_month_month) + ".)")
        graf.ui.valueYmaxB.setText(str(maxY) + " (" + str(max_day) + "." + str(max_month) + ".)")

        title = "Rain for year: " + str(godina) + "."
        xLabel = "Months"
        yLabel = "Monthly sum of rain"
        xyRange = (0.5, 12.5)
        x, y = plot.year_plot(dataset, godina)
        create_graph(graf, title, xLabel, yLabel, xyRange, x, y, 1, gradovi)

# Godina za 2 dana
def get_godina_data_two(graf, dataset_1, dataset_2, gradovi):
        godina = graf.pickGodina.value()
        sumY_1 = do.get_year_sum(dataset_1, godina)
        sumY_2 = do.get_year_sum(dataset_2, godina)
        max_month_1, max_day_1, maxY_1 = do.get_max_day_in_year(dataset_1, godina)
        max_month_2, max_day_2, maxY_2 = do.get_max_day_in_year(dataset_2, godina)
        max_month_month_1, maxY_month_1 = do.get_max_month_in_year(dataset_1, godina)
        max_month_month_2, maxY_month_2 = do.get_max_month_in_year(dataset_2, godina)

        graf.ui.labelYsum.setEnabled(True)
        graf.ui.valueYsumB.setEnabled(True)
        graf.ui.labelYmax.setEnabled(True)
        graf.ui.valueYmaxB.setEnabled(True)
        graf.ui.labelYmax_month.setEnabled(True)
        graf.ui.valueYmax_monthB.setEnabled(True)

        graf.ui.valueYsumB.setText(str(sumY_1))
        graf.ui.valueYsumR.setText(str(sumY_2))
        graf.ui.valueYmax_monthB.setText(str(maxY_month_1) + " (" + str(max_month_month_1) + ".)")
        graf.ui.valueYmax_monthR.setText(str(maxY_month_2) + " (" + str(max_month_month_2) + ".)")
        graf.ui.valueYmaxB.setText(str(maxY_1) + " (" + str(max_day_1) + "." + str(max_month_1) + ".)")
        graf.ui.valueYmaxR.setText(str(maxY_2) + " (" + str(max_day_2) + "." + str(max_month_2) + ".)")

        title = "Rain for year: " + str(godina) + "."
        xLabel = "Months"
        yLabel = "Monthly sum of rain"
        xyRange = (0.5, 12.5)
        x_1, y_1 = plot.year_plot(dataset_1, godina)
        x_2, y_2 = plot.year_plot(dataset_2, godina)
        create_graph(graf, title, xLabel, yLabel, xyRange, x_1, y_1, 1, gradovi)
        create_graph(graf, title, xLabel, yLabel, xyRange, x_2, y_2, 2, gradovi)

def year_data(graf, dataset_1, dataset_2, dataset_3, gradovi):
        godina = graf.pickGodina.value()

        graf.ui.labelYsum.setEnabled(True)
        graf.ui.valueYsumB.setEnabled(True)
        graf.ui.labelYmax.setEnabled(True)
        graf.ui.valueYmaxB.setEnabled(True)
        graf.ui.labelYmax_month.setEnabled(True)
        graf.ui.valueYmax_monthB.setEnabled(True)

        title = "Rain for year: " + str(godina) + "."
        xLabel = "Months"
        yLabel = "Monthly sum of rain"
        xyRange = (0.5, 12.5)

        if dataset_1:
                sumY_1 = do.get_year_sum(dataset_1, godina)
                max_month_1, max_day_1, maxY_1 = do.get_max_day_in_year(dataset_1, godina)
                max_month_month_1, maxY_month_1 = do.get_max_month_in_year(dataset_1, godina)
                graf.ui.valueYsumB.setText(str(sumY_1))
                graf.ui.valueYmax_monthB.setText(str(maxY_month_1) + " (" + str(max_month_month_1) + ".)")
                graf.ui.valueYmaxB.setText(str(maxY_1) + " (" + str(max_day_1) + "." + str(max_month_1) + ".)")
                x_1, y_1 = plot.year_plot(dataset_1, godina)
                create_graph(graf, title, xLabel, yLabel, xyRange, x_1, y_1, 1, gradovi)

        if dataset_2:
                sumY_2 = do.get_year_sum(dataset_2, godina)
                max_month_2, max_day_2, maxY_2 = do.get_max_day_in_year(dataset_2, godina)
                max_month_month_2, maxY_month_2 = do.get_max_month_in_year(dataset_2, godina)
                graf.ui.valueYsumR.setText(str(sumY_2))
                graf.ui.valueYmax_monthR.setText(str(maxY_month_2) + " (" + str(max_month_month_2) + ".)")
                graf.ui.valueYmaxR.setText(str(maxY_2) + " (" + str(max_day_2) + "." + str(max_month_2) + ".)")
                x_2, y_2 = plot.year_plot(dataset_2, godina)
                create_graph(graf, title, xLabel, yLabel, xyRange, x_2, y_2, 2, gradovi)

        if dataset_3:
                sumY_3 = do.get_year_sum(dataset_3, godina)
                max_month_3, max_day_3, maxY_3 = do.get_max_day_in_year(dataset_3, godina)
                max_month_month_3, maxY_month_3 = do.get_max_month_in_year(dataset_3, godina)
                graf.ui.valueYsumG.setText(str(sumY_3))
                graf.ui.valueYmax_monthG.setText(str(maxY_month_3) + " (" + str(max_month_month_3) + ".)")
                graf.ui.valueYmaxG.setText(str(maxY_3) + " (" + str(max_day_3) + "." + str(max_month_3) + ".)")
                x_3, y_3 = plot.year_plot(dataset_3, godina)
                create_graph(graf, title, xLabel, yLabel, xyRange, x_3, y_3, 3, gradovi)

def get_raspon_data(graf, dataset):
        od = graf.rasponOd.text().split('.')
        do = graf.rasponDo.text().split('.')

        print(od)
        print(do)

        graf.ui.valueMsumB.setText("Ovo je za raspon")

def get_usporedba_data(graf):
        graf.ui.valueMsumB.setText("Ovo je za usporedbu")

def create_graph(graf, title, xLabel, yLabel, xyRange, x, y, id, gradovi):
        style = {'color':'k', 'font-size':'15px'}

        graf.ui.Graf.setTitle(title, color="k", size="13pt")
        graf.ui.Graf.setLabel('bottom', xLabel, **style)
        graf.ui.Graf.setLabel('left', yLabel, **style)
        graf.ui.Graf.showGrid(x=True, y=True)
        graf.ui.Graf.setXRange(xyRange[0], xyRange[1], padding=0)
        graf.ui.Graf.addLegend()

        if len(gradovi) >= 1: grad_1 = gradovi[0]
        if len(gradovi) >= 2: grad_2 = gradovi[1]
        if len(gradovi) == 3: grad_3 = gradovi[2]
        
        if id == 1: graf.ui.Graf.plot(x, y, name=grad_1, pen=graf.ui.pen_1, symbol='o', symbolSize=5, symbolBrush=(22, 19, 83))
        elif id == 2: graf.ui.Graf.plot(x, y, name=grad_2, pen=graf.ui.pen_2, symbol='o', symbolSize=5, symbolBrush=(22, 19, 83))
        elif id == 3: graf.ui.Graf.plot(x, y, name=grad_3, pen=graf.ui.pen_3, symbol='o', symbolSize=5, symbolBrush=(22, 19, 83))

def bar_graph(graf, title, yLabel, x, y, id):
        style = {'color':'k', 'font-size':'15px'}

        graf.ui.Graf.setTitle(title, color="k", size="13pt")
        graf.ui.Graf.setLabel('left', yLabel, **style)
        graf.ui.Graf.showGrid(x=True, y=True)
        graf.ui.Graf.addLegend()

        # if id == 1: 
        #         x.append(2)
        #         x.append(3)
        #         y.append(0)
        #         y.append(0)
        # if id == 2:
        #         x.append(3)
        #         y.append(0)

        # print(x)
        # print(y)

        if id >= 1:
                bargraph_1 = pg.BarGraphItem(x=range(1,2),  height=y[0], width=0.3, brush=(77, 148, 255))
                graf.ui.Graf.addItem(bargraph_1)
        if id >= 2:
                bargraph_2 = pg.BarGraphItem(x=range(2,3), height=y[1], width=0.3, brush=(255, 102, 102))
                graf.ui.Graf.addItem(bargraph_2)
        if id == 3:
                bargraph_3 = pg.BarGraphItem(x=range(3,4), height=y[2], width=0.3, brush=(73, 158, 33))
                graf.ui.Graf.addItem(bargraph_3)
