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

# This dataframe has duplicate index value: 4.8. we can remove the duplicate but it also removes the duplicate entry.
# Need to be sure which row will be deleted. In this example it is the first one (lowest index) that is deleted.
# There is a keep=last parameter
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]),
                  index= [2.5, 12.6, 4.8, 4.8, 2.5],
                  columns=[48, 49, 50])
print(df)
df = df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index')
print(df)

