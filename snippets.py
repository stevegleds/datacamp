# Following code are just snippets. They wont run successfully:
# Append a column to `df`
df.loc[:, 4] = pd.Series(['5', '6'], index=df.index)

# This will make an index labeled `2` and add the new values
df.loc[2] = [11, 12, 13]
print(df)

# Drop the column with label 'A'
df.drop('A', axis=1, inplace=True)
print('label A dropped:', df)

# Drop the column at position 1
df=df.drop(df.columns[[1]], axis=1)
print(' index 1 dropped: ', df)

# Drop row at index 1
# Check out the DataFrame `df`
print(df)

# Drop the row at index at position 1
df=df.drop(df.index[1])
print(df)

df=df.reset_index(drop=True)
print(df)

# Drop the duplicates in `df` based on values in column labelled '48'. Keep the first occurrence.
df=df.drop_duplicates([48], keep='first')
print('new df: \n \n', df)

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