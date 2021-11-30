# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import pandas as pd


def main():
    rijeka_data = load_dataset("data/Rijeka.csv")
    marcelji_data = load_dataset("data/Marcelji.csv")
    matulji_data = load_dataset("data/Matulji.csv")

    print(rijeka_data.shape)
    print(marcelji_data.shape)
    print(matulji_data.shape)
    print(matulji_data[0])


def load_dataset(filename):
    df = pd.read_csv(filename)
    df = df.drop(['G'], axis=1)
    df = df[df.index % 32 != 0]

    data = np.array(df.values)
    data = np.reshape(data, (10, 31, 12))
    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    # test('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
