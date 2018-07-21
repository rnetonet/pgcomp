import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# load data
df = pd.read_csv("data_2014.csv")
data = df.iloc[:, 1:]

# finding the best number of clusters (k)
best_k = 0
best_silhouette = 0

for k in range(2, 10):
    estimator = KMeans(n_clusters=k)
    estimator.fit(data)

    silhouette = silhouette_score(data, estimator.labels_)

    if silhouette > best_silhouette:
        best_silhouette = silhouette
        best_k = k

    print(f"for k = {k} silhouette = {silhouette}")

print(f"Best silhouette = {best_silhouette}, besk k = {best_k}")

# creating the model with best_k clusters
estimator = KMeans(n_clusters=best_k)
estimator.fit(data)

# plot
pca = PCA(n_components=2)
pcomponents = pca.fit_transform(data)
pdata = pd.DataFrame(data = pcomponents, columns = ['x', 'y'])

pestimator = KMeans(n_clusters=best_k)
pestimator.fit(pdata)

# init sns
sns.set(style="whitegrid", palette="bright")

ax = sns.scatterplot(x='x', y='y', data=pdata, hue=pestimator.labels_)

for i in range(len(pdata)):
    x = pdata.iloc[i]["x"]
    y = pdata.iloc[i]["y"]
    ax.text(x, y, df.iloc[i]["partido"], verticalalignment='bottom', horizontalalignment='center', size='small', color='gray')

plt.show()