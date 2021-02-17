from sklearn import datasets
from sklearn.linear_model import LogisticRegression

import pandas as pd

iris = datasets.load_iris()
type(iris['data'])
features = pd.DataFrame(iris['data'])
target = iris['target']
model = LogisticRegression(max_iter=1000)
model.fit(features, target)

import pickle
import os

cwd = os.getcwd()
pickle.dump(model, open('model_iris', 'wb'))

pr = pd.read_csv("D:\dev\python\medium\practical guide build and deploy a ML web app\\test_csv_file.csv")

print(cwd)
filename = "file.csv"
fullpath = os.path.join(os.getcwd(), filename)
print(fullpath)
pr = pd.read_csv(fullpath, header=None)



from iris_model import predict_iris
print(predict_iris(pr))