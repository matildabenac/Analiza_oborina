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
                graf.ui.valueDayB.setText(str(value_1))
                x.append(1)
                y.append(value_1)
        if dataset_2:
                value_2 = do.get_day_value(gradovi[1], int(datum[0]), int(datum[1]), int(datum[2]))
                graf.ui.valueDayR.setText(str(value_2))
                x.append(2)
                y.append(value_2)
        if dataset_3:
                value_3 = do.get_day_value(gradovi[2], int(datum[0]), int(datum[1]), int(datum[2]))
                graf.ui.valueDayG.setText(str(value_3))
                x.append(3)
                y.append(value_3)

        title = "Rain for day: " + str(datum[0]) + "." + str(datum[1]) + "." + str(datum[2]) + "."
        yLabel = "Daily rain (mm)"
        bar_graph(graf, title, yLabel, x, y, len(x))

        labels = [(i, gradovi[i-1]) for i in x]
        ax = graf.ui.Graf.getAxis('bottom')
        ax.setTicks([labels])

def month_data(graf, dataset_1, dataset_2, dataset_3, gradovi):
        mjesec = graf.pickMjesecMjesec.value()
        godina = graf.pickMjesecGodina.value()

        graf.ui.labelMsum.setEnabled(True)
        graf.ui.valueMsumB.setEnabled(True)
        graf.ui.labelMmax.setEnabled(True)
        graf.ui.valueMmaxB.setEnabled(True)

        title = "Rain for month: " + str(mjesec) + "." + str(godina) + "."
        xLabel = "Days"
        yLabel = "Daily rain (mm)"
        xyRange = (0.5, 31.5)

        if dataset_1:
                sumM_1 = do.get_month_sum(dataset_1, godina, mjesec)
                max_day_1, maxM_1 = do.get_max_day_in_month(dataset_1, godina, mjesec)
                graf.ui.valueMsumB.setText(str(sumM_1))
                graf.ui.valueMmaxB.setText(str(maxM_1) + " (" + str(max_day_1) + "." + str(mjesec) + ".)")
                x_1, y_1 = plot.month_plot(gradovi[0], mjesec, godina)
                line_graph(graf, title, xLabel, yLabel, xyRange, x_1, y_1, 1, gradovi)

        if dataset_2:
                sumM_2 = do.get_month_sum(dataset_2, godina, mjesec)
                max_day_2, maxM_2 = do.get_max_day_in_month(dataset_2, godina, mjesec)
                graf.ui.valueMsumR.setText(str(sumM_2))
                graf.ui.valueMmaxR.setText(str(maxM_2) + " (" + str(max_day_2) + "." + str(mjesec) + ".)")
                x_2, y_2 = plot.month_plot(gradovi[1], mjesec, godina)
                line_graph(graf, title, xLabel, yLabel, xyRange, x_2, y_2, 2, gradovi)

        if dataset_3:
                sumM_3 = do.get_month_sum(dataset_3, godina, mjesec)
                max_day_3, maxM_3 = do.get_max_day_in_month(dataset_3, godina, mjesec)
                graf.ui.valueMsumG.setText(str(sumM_3))
                graf.ui.valueMmaxG.setText(str(maxM_3) + " (" + str(max_day_3) + "." + str(mjesec) + ".)")
                x_3, y_3 = plot.month_plot(gradovi[2], mjesec, godina)
                line_graph(graf, title, xLabel, yLabel, xyRange, x_3, y_3, 3, gradovi)

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
        yLabel = "Monthly rain sum (mm)"
        xyRange = (0.5, 12.5)

        if dataset_1:
                sumY_1 = do.get_year_sum(dataset_1, godina)
                max_month_1, max_day_1, maxY_1 = do.get_max_day_in_year(dataset_1, godina)
                max_month_month_1, maxY_month_1 = do.get_max_month_in_year(dataset_1, godina)
                graf.ui.valueYsumB.setText(str(sumY_1))
                graf.ui.valueYmax_monthB.setText(str(maxY_month_1) + " (" + str(max_month_month_1) + ".)")
                graf.ui.valueYmaxB.setText(str(maxY_1) + " (" + str(max_day_1) + "." + str(max_month_1) + ".)")
                x_1, y_1 = plot.year_plot(dataset_1, godina)
                line_graph(graf, title, xLabel, yLabel, xyRange, x_1, y_1, 1, gradovi)

        if dataset_2:
                sumY_2 = do.get_year_sum(dataset_2, godina)
                max_month_2, max_day_2, maxY_2 = do.get_max_day_in_year(dataset_2, godina)
                max_month_month_2, maxY_month_2 = do.get_max_month_in_year(dataset_2, godina)
                graf.ui.valueYsumR.setText(str(sumY_2))
                graf.ui.valueYmax_monthR.setText(str(maxY_month_2) + " (" + str(max_month_month_2) + ".)")
                graf.ui.valueYmaxR.setText(str(maxY_2) + " (" + str(max_day_2) + "." + str(max_month_2) + ".)")
                x_2, y_2 = plot.year_plot(dataset_2, godina)
                line_graph(graf, title, xLabel, yLabel, xyRange, x_2, y_2, 2, gradovi)

        if dataset_3:
                sumY_3 = do.get_year_sum(dataset_3, godina)
                max_month_3, max_day_3, maxY_3 = do.get_max_day_in_year(dataset_3, godina)
                max_month_month_3, maxY_month_3 = do.get_max_month_in_year(dataset_3, godina)
                graf.ui.valueYsumG.setText(str(sumY_3))
                graf.ui.valueYmax_monthG.setText(str(maxY_month_3) + " (" + str(max_month_month_3) + ".)")
                graf.ui.valueYmaxG.setText(str(maxY_3) + " (" + str(max_day_3) + "." + str(max_month_3) + ".)")
                x_3, y_3 = plot.year_plot(dataset_3, godina)
                line_graph(graf, title, xLabel, yLabel, xyRange, x_3, y_3, 3, gradovi)

def range_data(graf, dataset_1, dataset_2, dataset_3, gradovi):
        dateFrom = graf.rasponOd.text().split('.')
        dateTo = graf.rasponDo.text().split('.')

        graf.ui.labelRasponMax.setEnabled(True)
        graf.ui.labelRasponSum.setEnabled(True)

        title = "Range"
        xLabel = "Dates"
        yLabel = "Daily rain (mm)"
        xyRange = 0

        if dataset_1:
                maxDate, maxDateValue = do.get_range_max_day(dataset_1, int(dateFrom[2]), int(dateFrom[1]), int(dateFrom[0]), int(dateTo[2]), int(dateTo[1]), int(dateTo[0]))
                rangeSum = do.get_range_sum(dataset_1, int(dateFrom[2]), int(dateFrom[1]), int(dateFrom[0]), int(dateTo[2]), int(dateTo[1]), int(dateTo[0]))
                graf.ui.valueRasponMaxB.setText(str(maxDateValue) + " (" + str(maxDate) + ")")
                graf.ui.valueRasponSumB.setText(str(rangeSum))

                x, y = do.get_data_from_to_date(dataset_1, int(dateFrom[2]), int(dateFrom[1]), int(dateFrom[0]), int(dateTo[2]), int(dateTo[1]), int(dateTo[0]))
                
                num = []
                for i in range(len(x)):
                        num.append(i+1)
                labels = [(i, x[i-1]) for i in num]
                line_graph(graf, title, xLabel, yLabel, xyRange, num, y, 1, gradovi)

        if dataset_2:
                maxDate, maxDateValue = do.get_range_max_day(dataset_2, int(dateFrom[2]), int(dateFrom[1]), int(dateFrom[0]), int(dateTo[2]), int(dateTo[1]), int(dateTo[0]))
                rangeSum = do.get_range_sum(dataset_2, int(dateFrom[2]), int(dateFrom[1]), int(dateFrom[0]), int(dateTo[2]), int(dateTo[1]), int(dateTo[0]))
                graf.ui.valueRasponMaxR.setText(str(maxDateValue) + " (" + str(maxDate) + ")")
                graf.ui.valueRasponSumR.setText(str(rangeSum))

                x, y = do.get_data_from_to_date(dataset_2, int(dateFrom[2]), int(dateFrom[1]), int(dateFrom[0]), int(dateTo[2]), int(dateTo[1]), int(dateTo[0]))
                line_graph(graf, title, xLabel, yLabel, xyRange, num, y, 2, gradovi)

        if dataset_3:
                maxDate, maxDateValue = do.get_range_max_day(dataset_3, int(dateFrom[2]), int(dateFrom[1]), int(dateFrom[0]), int(dateTo[2]), int(dateTo[1]), int(dateTo[0]))
                rangeSum = do.get_range_sum(dataset_3, int(dateFrom[2]), int(dateFrom[1]), int(dateFrom[0]), int(dateTo[2]), int(dateTo[1]), int(dateTo[0]))
                graf.ui.valueRasponMaxG.setText(str(maxDateValue) + " (" + str(maxDate) + ")")
                graf.ui.valueRasponSumG.setText(str(rangeSum))

                x, y = do.get_data_from_to_date(dataset_3, int(dateFrom[2]), int(dateFrom[1]), int(dateFrom[0]), int(dateTo[2]), int(dateTo[1]), int(dateTo[0]))
                line_graph(graf, title, xLabel, yLabel, xyRange, num, y, 3, gradovi)

        ax = graf.ui.Graf.getAxis('bottom')
        ax.setTicks([labels])

def compare_data(graf, dataset, grad):
        day_1 = graf.usporedbaDanPrvi.value()
        month_1 = graf.usporedbaMjesecPrvi.value()
        year_1 = graf.usporedbaGodinaPrvi.value()
        day_2 = graf.usporedbaDanDrugi.value()
        month_2 = graf.usporedbaMjesecDrugi.value()
        year_2 = graf.usporedbaGodinaDrugi.value()

        years = [year_1, year_2]

        if month_1 and month_2:
                months = [month_1, month_2]

                if day_1 and day_2:
                        days = [day_1, day_2]
                        compare_day(graf, dataset, years, months, days, grad)
                else:
                        compare_month(graf, dataset, years, months, grad)
        else:
                compare_year(graf, dataset, years, grad)

def compare_day(graf, dataset, years, months, days, grad):
        graf.ui.labelDay.setEnabled(True)
        graf.ui.valueDayB.setEnabled(True)

        title = grad + " - days comparison"
        yLabel = "Daily rain (mm)"

        valueDay = []   # [value]
        bar = []        # [x ,y]
        xAxis = []
        dates = []

        for i in range(2):
                value = do.get_day_value(grad, int(days[i]), int(months[i]), int(years[i]))
                print(value)
                valueDay.append(value)
                xAxis.append(i+1)
                dates.append(str(days[i]) + "." + str(months[i]) + "." + str(years[i]) + ".")
                bar.append([i+1, value])

        graf.ui.valueDayB.setText(str(valueDay[0]))
        graf.ui.valueDayR.setText(str(valueDay[1]))

        bar_graph(graf, title, yLabel, xAxis, valueDay, id=2)

        labels = [(i, dates[i-1]) for i in xAxis]
        ax = graf.ui.Graf.getAxis('bottom')
        ax.setTicks([labels])

def compare_month(graf, dataset, years, months, grad):
        graf.ui.labelMsum.setEnabled(True)
        graf.ui.valueMsumB.setEnabled(True)
        graf.ui.labelMmax.setEnabled(True)
        graf.ui.valueMmaxB.setEnabled(True)

        title = grad + " - months comparison"
        xLabel = "Days"
        yLabel = "Daily rain (mm)"
        xyRange = (0.5, 31.5)

        sumMonth = []   # [sum_value]
        maxDay = []     # [max_day, max_value]
        plt = []        # [x, y]
        legend = []     # [str]
        
        for i in range(2):
                sumMonth.append(do.get_month_sum(dataset, years[i], months[i]))
                maxDay.append(do.get_max_day_in_month(dataset, years[i], months[i]))
                plt.append(plot.month_plot(grad, months[i], years[i]))
                legend.append(str(months[i]) + "." + str(years[i]) + ".")
        
        graf.ui.valueMmaxB.setText(str(maxDay[0][1]) + " (" + str(maxDay[0][0]) + "." + str(months[0]) + ".)")
        graf.ui.valueMmaxR.setText(str(maxDay[1][1]) + " (" + str(maxDay[1][0]) + "." + str(months[1]) + ".)")
        graf.ui.valueMsumB.setText(str(sumMonth[0]))
        graf.ui.valueMsumR.setText(str(sumMonth[1]))

        line_graph(graf, title, xLabel, yLabel, xyRange, plt[0][0], plt[0][1], 1, legend)
        line_graph(graf, title, xLabel, yLabel, xyRange, plt[1][0], plt[1][1], 2, legend)

def compare_year(graf, dataset, years, grad):
        graf.ui.labelYsum.setEnabled(True)
        graf.ui.valueYsumB.setEnabled(True)
        graf.ui.labelYmax.setEnabled(True)
        graf.ui.valueYmaxB.setEnabled(True)
        graf.ui.labelYmax_month.setEnabled(True)
        graf.ui.valueYmax_monthB.setEnabled(True)

        sumYear = []    # [sum_value]
        maxDay = []     # [max_month, max_day, max_value]
        maxMonth = []   # [max_month, max_value]
        plt = []        # [x, y]

        for year in years:
                sumYear.append(do.get_year_sum(dataset, year))
                maxDay.append(do.get_max_day_in_year(dataset, year))
                maxMonth.append(do.get_max_month_in_year(dataset, year))
                plt.append(plot.year_plot(dataset, year))

        graf.ui.valueYsumB.setText(str(sumYear[0]))
        graf.ui.valueYsumR.setText(str(sumYear[1]))
        graf.ui.valueYmaxB.setText(str(maxDay[0][2]) + " (" + str(maxDay[0][1]) + "." + str(maxDay[0][0]) + ".)")
        graf.ui.valueYmaxR.setText(str(maxDay[1][2]) + " (" + str(maxDay[1][1]) + "." + str(maxDay[1][0]) + ".)")
        graf.ui.valueYmax_monthB.setText(str(maxMonth[0][1]) + " (" + str(maxMonth[0][0]) + ".)")
        graf.ui.valueYmax_monthR.setText(str(maxMonth[1][1]) + " (" + str(maxMonth[1][0]) + ".)")
        
        title = grad + " - years comparison"
        xLabel = "Months"
        yLabel = "Monthly rain sum (mm)"
        xyRange = (0.5, 12.5)

        line_graph(graf, title, xLabel, yLabel, xyRange, plt[0][0], plt[0][1], 1, years)
        line_graph(graf, title, xLabel, yLabel, xyRange, plt[1][0], plt[1][1], 2, years)

def line_graph(graf, title, xLabel, yLabel, xyRange, x, y, id, gradovi):
        style = {'color':'k', 'font-size':'15px'}
        if xyRange:
                graf.ui.Graf.setXRange(xyRange[0], xyRange[1], padding=0)

        graf.ui.Graf.setTitle(title, color="k", size="13pt")
        graf.ui.Graf.setLabel('bottom', xLabel, **style)
        graf.ui.Graf.setLabel('left', yLabel, **style)
        graf.ui.Graf.showGrid(x=True, y=True)
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

        if id >= 1:
                bargraph_1 = pg.BarGraphItem(x=range(1,2),  height=y[0], width=0.3, brush=(77, 148, 255))
                graf.ui.Graf.addItem(bargraph_1)
        if id >= 2:
                bargraph_2 = pg.BarGraphItem(x=range(2,3), height=y[1], width=0.3, brush=(255, 102, 102))
                graf.ui.Graf.addItem(bargraph_2)
        if id == 3:
                bargraph_3 = pg.BarGraphItem(x=range(3,4), height=y[2], width=0.3, brush=(73, 158, 33))
                graf.ui.Graf.addItem(bargraph_3)
