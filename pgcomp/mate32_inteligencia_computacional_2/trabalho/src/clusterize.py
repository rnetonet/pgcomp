import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

# load data
df = pd.read_csv("data_2017.csv")
data = df.iloc[:, 1:]

# pca
pca = PCA(n_components=2)
pcomponents = pca.fit_transform(data)
pdata = pd.DataFrame(data=pcomponents, columns=["x", "y"])

print(pdata)

# finding the best number of clusters (k)
best_k = 2
best_silhouette = 0

pestimator = None

for k in range(2, 10):
    pestimator = KMeans(n_clusters=k)
    pestimator.fit(pdata)

    silhouette = silhouette_score(pdata, pestimator.labels_)

    if silhouette >= best_silhouette:
        best_silhouette = silhouette
        best_k = k

    print(f"for k = {k} silhouette = {silhouette}")

print(f"Best silhouette = {best_silhouette}, best k = {best_k}")

# init sns
sns.set_style("whitegrid")
ax = sns.scatterplot(x="x", y="y", data=pdata, hue=pestimator.labels_, palette="Set1")

for i in range(len(pdata)):
    x = pdata.iloc[i]["x"]
    y = pdata.iloc[i]["y"]
    ax.text(
        x,
        y,
        df.iloc[i]["partido"],
        verticalalignment="bottom",
        horizontalalignment="center",
        size="small",
        color="gray",
    )

plt.show()
