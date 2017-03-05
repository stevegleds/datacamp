# Following code are just snippets. They may run successfully in a Jupyter notebook:
# ************ Import modules ************
import pandas as pd
import numpy as np

# ************ Append a column to `df` ************
df.loc[:, 4] = pd.Series(['5', '6'], index=df.index)

# This will make an index labeled `2` and add the new values
df.loc[2] = [11, 12, 13]
print(df)

# ************ Drop columns ************

#Drop the column with label 'A'
df.drop('A', axis=1, inplace=True)
print('label A dropped:', df)

# Drop the column at position 1
df=df.drop(df.columns[[1]], axis=1)
print(' index 1 dropped: ', df)

# ************ Drop rows ************

# Drop row at index 1
# Check out the DataFrame `df`
print(df)

# Drop the row at index at position 1
df=df.drop(df.index[1])
print(df)

df=df.reset_index(drop=True)
print(df)

# ************ Drop Duplicates ************
# Drop the duplicates in `df` based on values in column labelled '48'. Keep the first occurrence.
df=df.drop_duplicates([48], keep='first')
print('new df: \n \n', df)

# ************ Removing duplicate data ************
# This dataframe has duplicate index value: 4.8. we can remove the duplicate but it also removes the duplicate entry.
# Need to be sure which row will be deleted. In this example it is the first one (lowest index) that is deleted.
# There is a keep=last parameter
df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [40, 50, 60], [23, 35, 37]]),
                  index= [2.5, 12.6, 4.8, 4.8, 2.5],
                  columns=[48, 49, 50])
print(df)
df = df.reset_index().drop_duplicates(subset='index', keep='last').set_index('index')
print(df)

# ************ Rename Columns ************

# Define the new names of your columns
newcols = {
    'A': 'new_column_1',
    'B': 'new_column_2',
    'C': 'new_column_3'
}
print(newcols)
# Use `rename()` to rename your columns
df.rename(columns=newcols, inplace=True)
print(df)
# Use `rename()` to your index
df=df.rename(index={1: 'a'})
print(df)

# ************ Dates ************

# Dates
pd.read_csv('yourFile', parse_dates=True)
#or
pd.read_csv('yourFile', parsse_dates=['columnName'])

# ************ Data manipulation ************
# Pivot data - like excel pivot

products = pd.DataFrame({'category': ['Cleaning', 'Cleaning', 'Entertainment', 'Entertainment', 'Tech', 'Tech'],
                        'store': ['Walmart', 'Dia', 'Walmart', 'Fnac', 'Dia','Walmart'],
                        'price':[11.42, 23.50, 19.99, 15.95, 55.75, 111.55],
                        'testscore': [4, 3, 5, 7, 5, 8]})
print('Original: \n\n\n\n', products, '\n\n')

# Use `pivot()` to pivot the DataFrame . This shows how much is spent in each store for each category
pivot_products = products.pivot(index='category', columns='store', values='price')
#Note: can also take the aggfunc='mean' function (in this case ' mean')

# Check out the result
print(pivot_products)

# ************ Iterate over data ************

#Simply use iterrows():

df = pd.DataFrame(data=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['A', 'B', 'C'])

for index, row in df.iterrows() :
    print(row['A'], row['B'])

# ************ Write to csv or excel ************

# creates file with tab delimiter and utf-8 encodingMore: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_csv.html

df.to_csv('myDataFrame.csv', sep='\t', encoding='utf-8')

# Uses excelwriter to create xls file.Also takes parameter for separator etc.More: http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_excel.html
writer = pd.ExcelWriter('myDataFrame.xlsx')
df.to_excel(writer, 'DataFrame')
writer.save()

