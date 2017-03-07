import pandas as pd
from sklearn.decomposition import RandomizedPCA
import matplotlib.pyplot as plt

csv_path = '../../csv/'

df_train = pd.read_csv(csv_path + 'train.csv')
df_test = pd.read_csv(csv_path + 'test.csv')

print df_train.shape
print df_test.shape

print df_train.head(0)

print df_train
digits = df_train[['Survived', 'Sex', 'Age']]['Sex'].map({'female': 0, 'male': 1})
print digits

# rpca = RandomizedPCA(n_components=2)
print '----------'
print digits[1:,]
# rpca_reduced_data = rpca.fit_transform(digits[1:,])

# print type(rpca_reduced_data)
