import numpy
import numpy as np
import pandas as pd
import operator


def load_dataset(filename):
    # get dataframes
    df = pd.read_csv(filename)
    df = df.drop(['G'], axis=1)
    df = df[df.index % 32 != 0]

    # shape to array
    dt = np.array(df.values)
    dt = np.reshape(dt, (10, 31, 12))
    dt = np.transpose(dt, (0, 2, 1))

    # turn to dictionary of shape: "year": "month": "day": value"
    data = {}
    for year in range(2008, 2018):
        ydict = {}
        for month in range(1, 13):
            mdict = {}
            for day in range(1, 32):
                value = dt[year-2008][month-1][day-1]
                try:
                    value = float(value)
                except ValueError:
                    value = 0.

                # if value does not exist do not add to dict
                if np.isnan(value):
                    continue

                mdict.update({day: value})
            ydict.update({month: mdict})

        data.update({year: ydict})

    return data


def get_year_sum(dataset, year):
    ydict = dataset.get(year)

    ysum = 0
    for month in ydict:
        ysum += sum(ydict[month].values())

    return ysum


def get_sum_by_years(dataset, from_year = 2008, to_year = 2017):
    if from_year < 2008: from_year = 2008
    if to_year > 2017: to_year = 2017

    sums = []
    for year in range(from_year, to_year+1):
        sums.append(get_year_sum(dataset, year))

    return sums


def get_month_sum(dataset, year, month):
    mdict = dataset.get(year).get(month)

    msum = sum(mdict.values())

    return msum


def get_year_sums_by_months(dataset, year):
    sums = []
    for month in dataset[year]:
        sums.append(get_month_sum(dataset, year, month))

    return sums


def get_max_day_in_year(dataset, year):
    max_month, max_day = (1, 1)

    for month in range(1, 13):
        for day in dataset[year][month]:

            if dataset[year][month][day] > dataset[year][max_month][max_day]:
                max_month, max_day = (month, day)

    return max_month, max_day, dataset[year][max_month][max_day]


def get_max_month_in_year(dataset, year):
    max_month = 1
    max_month_val = 0

    for month in range(1, 13):
        month_val = get_month_sum(dataset, year, month)

        if month_val > max_month_val:
            max_month = month
            max_month_val = month_val

    return max_month, max_month_val


def get_max_day_in_month(dataset, year, month):
    max_day = 1

    for day in dataset[year][month]:
        if dataset[year][month][day] > dataset[year][month][max_day]:
            max_day = day

    return max_day, dataset[year][month][max_day]


# def get_data_from_to_date(dataset, from_year, from_month = 1, from_day = 1, to_year = 2017, to_month = 12, to_day = 31):