import data_operations as do
import visualization as plot

def get_dan_data(graf, dataset, grad):
        datum = graf.pickDan.text().split('.')
        value = do.get_day_value(grad, int(datum[0]), int(datum[1]), int(datum[2]))
        graf.ui.valueDay.setText(str(value))

def get_mjesec_data(graf, dataset, grad):
        mjesec = graf.pickMjesecMjesec.value()
        godina = graf.pickMjesecGodina.value()
        sumM = do.get_month_sum(dataset, godina, mjesec)
        max_day, maxM = do.get_max_day_in_month(dataset, godina, mjesec)

        graf.ui.valueMsum.setText(str(sumM))
        graf.ui.valueMmax.setText(str(maxM) + " (" + str(max_day) + "." + str(mjesec) + ".)")

        title = "Rain for month: " + str(mjesec) + "." + str(godina) + "."
        xLabel = "Days"
        yLabel = "Daily rain"
        xyRange = (0.5, 31.5)
        x, y = plot.month_plot(grad, mjesec, godina)
        create_graph(graf, title, xLabel, yLabel, xyRange, x, y, 1)

def compare_mjesec_data_two(graf, dataset_1, dataset_2, grad_1, grad_2):
        mjesec = graf.pickMjesecMjesec.value()
        godina = graf.pickMjesecGodina.value()
        sumM_1 = do.get_month_sum(dataset_1, godina, mjesec)
        sumM_2 = do.get_month_sum(dataset_2, godina, mjesec)
        max_day_1, maxM_1 = do.get_max_day_in_month(dataset_1, godina, mjesec)
        max_day_2, maxM_2 = do.get_max_day_in_month(dataset_2, godina, mjesec)

        graf.ui.valueMsum.setText(str(sumM_1))
        graf.ui.valueMmax.setText(str(maxM_1) + " (" + str(max_day_1) + "." + str(mjesec) + ".)")

        title = "Rain for month: " + str(mjesec) + "." + str(godina) + "."
        xLabel = "Days"
        yLabel = "Daily rain"
        xyRange = (0.5, 31.5)
        x_1, y_1 = plot.month_plot(grad_1, mjesec, godina)
        x_2, y_2 = plot.month_plot(grad_2, mjesec, godina)
        create_graph(graf, title, xLabel, yLabel, xyRange, x_1, y_1, 1)
        create_graph(graf, title, xLabel, yLabel, xyRange, x_2, y_2, 2)

def compare_mjesec_data_three(graf, dataset_1, dataset_2, dataset_3, grad_1, grad_2, grad_3):
        mjesec = graf.pickMjesecMjesec.value()
        godina = graf.pickMjesecGodina.value()
        sumM_1 = do.get_month_sum(dataset_1, godina, mjesec)
        sumM_2 = do.get_month_sum(dataset_2, godina, mjesec)
        sumM_3 = do.get_month_sum(dataset_3, godina, mjesec)
        max_day_1, maxM_1 = do.get_max_day_in_month(dataset_1, godina, mjesec)
        max_day_2, maxM_2 = do.get_max_day_in_month(dataset_2, godina, mjesec)
        max_day_3, maxM_3 = do.get_max_day_in_month(dataset_3, godina, mjesec)

        graf.ui.valueMsum.setText(str(sumM_1))
        graf.ui.valueMmax.setText(str(maxM_1) + " (" + str(max_day_1) + "." + str(mjesec) + ".)")

        title = "Rain for month: " + str(mjesec) + "." + str(godina) + "."
        xLabel = "Days"
        yLabel = "Daily rain"
        xyRange = (0.5, 31.5)
        x_1, y_1 = plot.month_plot(grad_1, mjesec, godina)
        x_2, y_2 = plot.month_plot(grad_2, mjesec, godina)
        x_3, y_3 = plot.month_plot(grad_3, mjesec, godina)
        create_graph(graf, title, xLabel, yLabel, xyRange, x_1, y_1, 1)
        create_graph(graf, title, xLabel, yLabel, xyRange, x_2, y_2, 2)
        create_graph(graf, title, xLabel, yLabel, xyRange, x_3, y_3, 3)

def get_godina_data(graf, dataset):
        godina = graf.pickGodina.value()
        sumY = do.get_year_sum(dataset, godina)
        max_month, max_day, maxY = do.get_max_day_in_year(dataset, godina)

        graf.ui.valueYsum.setText(str(sumY))
        graf.ui.valueYmax.setText(str(maxY) + " (" + str(max_day) + "." + str(max_month) + ".)")

        title = "Rain for year: " + str(godina) + "."
        xLabel = "Months"
        yLabel = "Monthly sum of rain"
        xyRange = (0.5, 12.5)
        x, y = plot.year_plot(dataset, godina)
        create_graph(graf, title, xLabel, yLabel, xyRange, x, y, 1)

def get_raspon_data(graf, dataset):
        od = graf.rasponOd.text().split('.')
        do = graf.rasponDo.text().split('.')

        print(od)
        print(do)

        graf.ui.valueMsum.setText("Ovo je za raspon")

def get_usporedba_data(graf):
        graf.ui.valueMsum.setText("Ovo je za usporedbu")

def create_graph(graf, title, xLabel, yLabel, xyRange, x, y, id):
        style = {'color':'k', 'font-size':'15px'}

        graf.ui.Graf.setTitle(title, color="k", size="13pt")
        graf.ui.Graf.setLabel('bottom', xLabel, **style)
        graf.ui.Graf.setLabel('left', yLabel, **style)
        graf.ui.Graf.showGrid(x=True, y=True)
        graf.ui.Graf.setXRange(xyRange[0], xyRange[1], padding=0)

        if id == 1: graf.ui.Graf.plot(x, y, pen=graf.ui.pen_1)
        elif id == 2: graf.ui.Graf.plot(x, y, pen=graf.ui.pen_2)
        elif id == 3: graf.ui.Graf.plot(x, y, pen=graf.ui.pen_3, symbol='o', symbolSize=5, symbolBrush=(22, 19, 83))