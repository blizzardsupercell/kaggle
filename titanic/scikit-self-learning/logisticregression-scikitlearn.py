from sklearn import datasets, linear_model
import pandas as pd
import matplotlib.pyplot as plt

iris = datasets.load_iris()


train = pd.read_csv('../../csv/train.csv')
test = pd.read_csv('../../csv/test.csv')

lr = linear_model.LogisticRegression()
lr.fit()
train.to_dict()
