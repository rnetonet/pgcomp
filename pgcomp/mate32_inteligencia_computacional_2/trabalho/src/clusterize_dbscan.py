import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.preprocessing import StandardScaler

# load data
df = pd.read_csv("data_2005_2006.csv")
data = df.iloc[:, 1:]

estimator = DBSCAN(eps=5, min_samples=3)
estimator.fit(data)
print(estimator.labels_)

pca = PCA(n_components=2)
pcomponents = pca.fit_transform(data)
pdata = pd.DataFrame(data=pcomponents, columns=["x", "y"])

pestimator = DBSCAN()
pestimator.fit(pdata)

print(pestimator.labels_)

colors = pestimator.labels_

plt.scatter(pdata.loc[:, "x"], pdata.loc[:, "y"], c=colors, alpha=0.5)
plt.show()
