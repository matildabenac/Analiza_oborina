import matplotlib.pyplot as plt
import numpy as np
import data_operations as do
from calendar import monthrange


def month_plot(dataset_name, month, year):
    num = monthrange(year, month)
    days = range(1, num[1]+1)
    values = []

    for day in days:
        values.append(do.get_day_value(dataset_name, day, month, year))

    return days, values

def year_plot(dataset, year):
    months = range(1, 13)
    sums = do.get_year_sums_by_months(dataset, year)

    return months, sums

# - mjesečne sume padalina
def visualize_monthly_rain_sum(dataset, year):
    sums = do.get_year_sums_by_months(dataset, year)
    months = range(1, 13)

    plt.title("Rain for year: " + str(year))

    plt.bar(months, sums)

    plt.xlabel("Months")
    plt.xticks(months)

    plt.ylabel("Monthly sum of rain")

    plt.show()

# - godišnje sume padalina
def visualize_yearly_rain_sum(dataset, from_year = 2008, to_year = 2017):
    if from_year < 2008 or to_year > 2017:
        return "Unable to process"

    sums = do.get_sum_by_years(dataset, from_year, to_year)
    years = range(from_year, to_year+1)

    plt.title("Rain for years: " + str(from_year) + " - " + str(to_year))

    plt.bar(years, sums)

    plt.xlabel("Years")
    plt.xticks(years)

    plt.ylabel("Yearly sum of rain")

    plt.show()


# - usporedba razlike padalina po danu
def visualize_comparison_by_day(dataset1, year1, month1, day1, dataset2, year2, month2, day2):
    x1 = dataset1[year1][month1][day1]
    x2 = dataset2[year2][month2][day2]
    print(x1, x2)

    plt.title("Usporedba")

    plt.bar("Day 1", x1)
    plt.bar("Day 2", x2)

    plt.ylabel("Amount of rain")

    plt.show()


# - usporedba razlike padalina po mjesecu
# sum comparison graph
def visualize_sum_comparison_by_month(dataset1, year1, month1, dataset2, year2, month2):
    x1 = do.get_month_sum(dataset1, year1, month1)
    x2 = do.get_month_sum(dataset2, year2, month2)

    plt.title("Usporedba")

    plt.bar("Month 1", x1)
    plt.bar("Month 2", x2)

    plt.ylabel("Amount of rain")

    plt.show()


# day by day comparison graph
def visualize_comparison_by_month(dataset1, year1, month1, dataset2, year2, month2):
    x1 = dataset1[year1][month1].values()
    x2 = dataset2[year2][month2].values()
    days = max(len(x1), len(x2))

    plt.figure(figsize=(10, 5))
    plt.title("Usporedba po mjesecu")
    plt.plot(x1)
    plt.plot(x2)

    plt.xlabel("Days")
    plt.xticks(range(0, days), range(1, days + 1))

    plt.ylabel("Daily amount of rain")

    plt.show()


# - usporedba razlike padalina po godini
 # sum comparison graph
def visualize_sum_comparison_by_year(dataset1, year1, dataset2, year2):
    x1 = do.get_year_sum(dataset1, year1)
    x2 = do.get_year_sum(dataset2, year2)

    plt.title("Usporedba")

    plt.bar("Year 1", x1)
    plt.bar("Month 2", x2)

    plt.ylabel("Amount of rain")

    plt.show()


# month by month comparison graph
def visualize_comparison_by_year(dataset1, year1, dataset2, year2):
    x1 = do.get_year_sums_by_months(dataset1, year1)
    x2 = do.get_year_sums_by_months(dataset2, year2)
    months = max(len(x1), len(x2))

    plt.figure(figsize=(10, 5))
    plt.title("Usporedba po godini")
    plt.plot(x1)
    plt.plot(x2)

    plt.xlabel("Months")
    plt.xticks(range(0, months), range(1, months + 1))

    plt.ylabel("Monthly amount of rain")

    plt.show()


# - prikaz proizvoljnog raspona
# TODO

# - sumarna razlika po odabranom periodu
# TODO
# - graf usporedbe razlike po odabranom periodu
# TODO
