import numpy
import numpy as np
import pandas as pd


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


def get_year_month_sum(dataset, year, month):
    mdict = dataset.get(year).get(month)

    msum = sum(mdict.values())

    return msum

# caseovi:
# suma za mjesec al za sve godine
# suma svih padalina za sve godine
# pogledaj dalje..

