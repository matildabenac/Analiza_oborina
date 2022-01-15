# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import data_operations as do


def main():
    rijeka_data = do.load_dataset("data/Rijeka.csv")
    marcelji_data = do.load_dataset("data/Marcelji.csv")
    matulji_data = do.load_dataset("data/Matulji.csv")

    print(do.get_year_sum(rijeka_data, 2010))
    print(do.get_year_month_sum(marcelji_data, 2008, 1))



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    # test('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
