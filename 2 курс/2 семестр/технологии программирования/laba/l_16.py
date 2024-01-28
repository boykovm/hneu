import numpy as np

class DataParser:
    def __int__(self, path = "countries_of_the_world.csv", delimiter = ","):
        self.file_path = path
        self.data_array = np.loadtxt(path, delimiter=delimiter, dtype=str)

    def get_data(self):
        return self.data_array


dp = DataParser("countries_of_the_world.csv", ",")

print(dp.get_data())