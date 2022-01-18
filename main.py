# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import data_operations as do
import visualization as vis


def main():
    rijeka_data = do.load_dataset("data/Rijeka.csv")
    marcelji_data = do.load_dataset("data/Marcelji.csv")
    matulji_data = do.load_dataset("data/Matulji.csv")

    # print(do.get_year_sum(rijeka_data, 2010))
    # print(do.get_year_month_sum(marcelji_data, 2008, 1))
    # print(do.get_year_max_day(matulji_data, 2015))
    # print(do.get_year_max_month(rijeka_data, 2012))
    # print(do.get_year_month_max_day(marcelji_data, 2017, 12))
    vis.visualize_year_month_data(rijeka_data, 2008, 1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    # test('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
