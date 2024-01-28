import numpy as np

class DataParser:
    def __init__(self, path: str = None, separator = ","):
        if not path:
            raise Exception('Path must be a string')
        try:
            self.path = path
            file_array = np.loadtxt(path, delimiter=separator, dtype=str)
            self.headers = file_array[0][0:]
            self.data_array = np.array(file_array[1:])
        except:
            raise Exception('Can\'t open a file')
        self.data_enum = {}
        for i in range(len(self.headers)):
            self.data_enum[self.headers[i]] = i
        print(self.data_enum)

    def country_list(self):
        countries = []
        for row in self.data_array:
            countries.append(row[0])
        return countries

    def area_more_than_another_country_area(self, country_name = None):
        if not country_name:
            raise Exception('Country name must be provided')
        countries = []
        compare_row = []
        for row in self.data_array:
            if country_name in row[self.data_enum['Country']]:
                compare_row = row
                break
        compared_area = float(compare_row[self.data_enum['Area (sq. mi.)']])
        for row in self.data_array:
            if float(row[self.data_enum['Area (sq. mi.)']]) > compared_area:
                countries.append(row[self.data_enum['Country']])
        print(compared_area)
        return countries

    def countries_which_has_population_more_than(self, population = None):
        if not population:
            raise Exception('Population must be provided')
        countries = []
        for row in self.data_array:
            if int(row[self.data_enum['Population']]) > population:
                countries.append(row[self.data_enum['Country']])
        return countries

    def inner_join(self, arr_1 = [], arr_2 = []):
        countries = []
        for data in arr_1:
            if data in arr_2:
                countries.append(data)
        return countries

    def countries_without_sea(self):
        countries = []
        for row in self.data_array:
            arable = row[self.data_enum['Arable (%)']]
            if arable == '':
                continue
            crops = row[self.data_enum['Crops (%)']]
            if crops == '':
                continue
            other = row[self.data_enum['Other (%)']]
            if other == '':
                continue
            if float(arable) + float(crops) + float(other) != 100:
                countries.append(row[self.data_enum['Country']])
        return countries

    def top_population_countries(self, limit = 10):
        if limit < 1:
            raise Exception('Limit must be a positive number')
        arr = np.copy(self.data_array)
        for i in range(len(arr) - 1):
            for j in range(i, len(arr) - 1):
                if arr[i][self.data_enum['Pop. Density (per sq. mi.)']] == '' or arr[j][self.data_enum['Pop. Density (per sq. mi.)']] == '':
                    continue
                if float(arr[i][self.data_enum['Pop. Density (per sq. mi.)']]) < float(arr[j][self.data_enum['Pop. Density (per sq. mi.)']]):
                    arr[i], arr[j] = np.copy(arr[j]), np.copy(arr[i])
        countries = []
        limit = limit if limit <= len(arr) else len(arr)
        for i in range(limit):
            countries.append(arr[i][self.data_enum['Country']])
        return countries




try:
    dp_error = DataParser()
except:
    print('Exception')
try:
    dp_not_correct_file = DataParser("qwe")
except:
    print('Exception')
dp = DataParser("countries_of_the_world.csv", ",")
print(dp.data_array[0])
# print(dp.data_array)

# print(dp.country_list())
area_more_than_Ukraine_area = dp.area_more_than_another_country_area('Ukraine')
print(area_more_than_Ukraine_area)

countries_which_has_population_more_than_10_millions = dp.countries_which_has_population_more_than(10000000)
print(dp.inner_join(area_more_than_Ukraine_area, countries_which_has_population_more_than_10_millions))

print(dp.countries_without_sea())

print(dp.top_population_countries())