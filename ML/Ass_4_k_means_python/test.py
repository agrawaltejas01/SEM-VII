"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

#Get default dataset
iris = datasets.load_iris()

#Convert into dataframe
x = pd.DataFrame(iris.data)
x.head()
#Name the columns
x.columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width' ]
x.head()

#K-Mean clustering
a = KMeans(n_clusters = 3)
#Classify
a.fit(x)
#label the target
a.labels_

#plot graph
colormap = np.array(['Red', 'Green', 'Blue'])
z = plt.scatter(x.sepal_length, x.sepal_width, x.petal_length, c = colormap[a.labels_])

#accuracy
accuracy_score(iris.target, a.labels_)
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from sklearn import datasets
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

data = pd.read_csv("/home/test/BE/CL-7_practice/ML/Datasets/Breast-cancer Dataset/breast-cancer-wisconsin.data", na_values = "?")
#breast_data = datasets.load_breast_cancer()
x = pd.DataFrame(data)
x.head() 
x.columns = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H', 'I', 'J', 'K']

x.isnull().sum()
x.fillna(0, inplace = True)
x.isna().sum()

plt.scatter(x.A,x.K )

a = KMeans(n_clusters=3)
a.fit(x)
a.labels_
colormap = np.array(['Red', 'Blue', 'Green'])
z = plt.scatter(x.A,x.H, c = colormap[a.labels_] )

accuracy_score(x.H, a.labels_)