# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import data_operations as do
import visualization as vis


def main():
    rijeka_data = do.load_dataset("data/Rijeka.csv", "Rijeka")
    marcelji_data = do.load_dataset("data/Marcelji.csv", "Marčelji")
    matulji_data = do.load_dataset("data/Matulji.csv", "Matulji")

    # vis.visualize_monthly_rain_sum(rijeka_data, 2017)
    # vis.visualize_yearly_rain_sum(marcelji_data)
    # vis.visualize_comparison_by_day(matulji_data, 2008, 12, 1, marcelji_data, 2008, 12, 1)
    # vis.visualize_comparison_by_month(rijeka_data, 2010, 1, marcelji_data, 2011, 1)
    # vis.visualize_sum_comparison_by_month(rijeka_data, 2010, 1, marcelji_data, 2011, 1)
    # vis.visualize_comparison_by_year(matulji_data, 2008, matulji_data, 2017)
    # vis.visualize_sum_comparison_by_year(matulji_data, 2008, matulji_data, 2017)
    vis.visualize_range(rijeka_data, 2008, 1, 1, 2010, 2, 12)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
    # test('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
