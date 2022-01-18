import matplotlib.pyplot as plt
import numpy


def visualize_year_month_data(dataset, year, month):
    values = dataset[year][month].values()

    print(values)

    plt.plot(values)
    plt.xlabel("months")
    plt.ylabel("Daily amount of rain")
    plt.title("Rain for:" + str(month) + " month, " + str(year))
    plt.show()

