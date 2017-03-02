import pandas as pd
from pylab import *


print('hello world')
# using numpy array as input
data_nparray = np.array([['', 'Col1', 'col2'],
                         ['Row1', 1, 2],
                         ['Row2', 3, 4]])
my_data = data_nparray
print(pd.DataFrame(data=my_data[1:, 1:],
                   index=my_data[1:, 0],
                   columns=my_data[0, 1:]))

# Using a 2D as input to dataframe
data_2darray = np.array([[1, 2, 3], [4, 5, 6]])
my_data = data_2darray
print(pd.DataFrame(data=my_data[0:, 0:]))

# Using a dictionary as input to dataframe
data_dict = {1: ['1', '3'], 2: ['1', '2'], 3: ['2', '4']}
my_data = data_dict
print(pd.DataFrame(data=my_data))

# using a dataframe as input to dataframe
data_dataframe = pd.DataFrame(data=[4, 5, 6, 7], index=range(0,4), columns=['A'])
my_data = data_dataframe
print(pd.DataFrame(data=my_data))

# using a series as input to dataframe
data_series = pd.Series({"United Kingdom":"London", "India":"New Delhi", "United States":"Washington", "Belgium":"Brussels"})
my_data = data_series
print(pd.DataFrame(data=my_data))

my_data = data_dataframe
print('dataframe shape is: ', my_data.shape)
print('columns in dataframe are: ', len(my_data.index))
