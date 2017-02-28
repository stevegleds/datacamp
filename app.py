import numpy as np
import pandas as pd

print('hello world')

data = np.array([['', 'Col1', 'col2'],
                 ['Row1', 1, 2],
                 ['Row2', 3, 4]])

print(data)
print(pd.DataFrame(data=data[1:,1:],
                   index=data[1:,0],
                   columns=data[0,1:]))
