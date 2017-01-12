import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_csv = pd.read_csv('../csv/train.csv', header=0)

print df_csv

s = pd.Series([1, 3, 4, np.nan, 6, 8])
print s

dates = pd.date_range('20130101', periods=6)
print dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print df

df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(["test", "train", "test", "train"]),
    'F': 'foo'
})

#print df2.head(2)
#print df2.tail(2)
#
#print df2.index
#
#print df2.columns
#print df2.values
#
#print df.describe()
#
#print df.T
#
#print df2
#
#print df.sort_index(axis=0, ascending=False)
#df.sort_values

#df['A'].hist()
df_csv.hist()
print df_csv