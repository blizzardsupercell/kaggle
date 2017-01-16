from sklearn import datasets
import pandas as pd
import numpy as np
import csv as csv

csv_path = '../../csv/'

df_train = pd.read_csv(csv_path + 'train.csv')
df_test = pd.read_csv(csv_path + 'test.csv')

print df_train.shape
print df_test.shape
