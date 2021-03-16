# dimensionality reductioin can be done by feature selection and feature extraction
# covariance matrix and heatmap
from sklearn import datasets
from sklearn.preprocessing import StandardScaler

iris_data = datasets.load_iris()
print(dir(iris_data))
print(iris_data.data)
print(type(iris_data.data))

import numpy as np

cov_data = np.corrcoef(iris_data.data.T)
print(cov_data)

# visualization for correlation
import matplotlib.pylab as plt

img = plt.matshow(cov_data, cmap=plt.cm.rainbow)
plt.colorbar(img, ticks=[-1, 0, 1], fraction=0.045)

for x in range(cov_data.shape[0]):
    for y in range(cov_data.shape[1]):
        plt.text(x, y, f"{cov_data[x, y]:,.2f}", color="black",
                 ha="center", va="center")

plt.show(block=False)

import pandas as pd

iris_data = datasets.load_iris()
dir(iris_data)
df = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
df['class'] = iris_data.target

# separate input and output.value
x = df.drop(labels='class', axis=1)
y = df['class'].values
y_ = df['class']
type(y)
type(y_)
y.shape

y_.shape


class convers_pca():
    def __init__(self, no_of_components):
        self.no_of_components = no_of_components
        self.eigen_values = None
        self.eigen_vectors = None

    def transform(self, x):
        return np.dot(x-self.mean, self.projection_matrix.T)

    def inverse_transform(self, x):
        return np.dot(x,self.projection_matrix)+self.mean

    def fit(self, x):
        self.no_of_components = x.shape[1]  # axis=1 is feature
        self.mean = np.mean(x, axis=0)  # also axis is columns
        cov_matrix = np.cov(x - self.mean, rowvar=False)
        self.eigen_values, self.eigen_vectors = np.linalg.eig(cov_matrix)
        self.eigen_vectors = self.eigen_vectors.T  # why?
        self.sorted_components = np.argsort(self.eigen_values)[::-1]
        self.projection_matrix = self.eigen_vectors[self.sorted_components[:self.no_of_components]]
        self.explained_variance = self.eigen_values[self.sorted_components]
        self.explained_variance_ratio = self.explained_variance / self.eigen_values.sum()


std = StandardScaler()
transformed=StandardScaler().fit_transform(x)


cov_pca=convers_pca(no_of_components=2)
cov_pca.fit(transformed)

print(cov_pca.eigen_vectors)

print(cov_pca.eigen_values)

print(cov_pca.sorted_components)

x_std=cov_pca.transform(transformed)

plt.figure()
plt.scatter(x_std[:,0], x_std[:,1],c=y)

plt.show(block=False)


from pandas.plotting import scatter_matrix

iris = datasets.load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
colors=np.array(50*['r']+50*['g']+50*['b'])  #총 150개 데이터, 50개씩 순서대로


scatter_matrix(df, alpha=0.7, figsize=(10,10), color=colors)

plt.show()
iris.data.shape
iris_target=iris.target