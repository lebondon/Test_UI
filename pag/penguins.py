import pandas as pd
import streamlit as st
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def main():
    path = "https://frenzy86.s3.eu-west-2.amazonaws.com/python/penguins.csv"

    df=pd.read_csv(path)

    X=df.drop("species",axis=1)
    island={'Biscoe':0,'Dream':1,'Torgensen':2}
    sex={'male':0,'female':1}
    X['island']=X['island'].map(island)
    X['sex']=X['sex'].map(sex)
    pca=PCA(2)
    X=X.dropna()
    scaled_X=pca.fit_transform(X)
    scaled_X = StandardScaler().fit_transform(scaled_X)
    scaled_X=pd.DataFrame(scaled_X)

    sse = []
    for k in range(1, 11):
        kmeans = KMeans(n_clusters=k)
        kmeans.fit(scaled_X)
        sse.append(kmeans.inertia_)

    st.title("Penguins Species Clustering")

    k = st.number_input("insert the number of clusters you want:", min_value=1, max_value=30)    

    kmeans=KMeans(n_clusters=k)

    labels=kmeans.fit_predict(X)
    scaled_X['label']=labels
    lable_filtered0=scaled_X.loc[scaled_X['label'] == 0]
    lable_filtered1=scaled_X.loc[scaled_X['label'] == 1]
    lable_filtered2=scaled_X.loc[scaled_X['label'] == 2]

    fig, ax = plt.subplots()
    ax.scatter(x=lable_filtered0[0], y=lable_filtered0[1], c='red')
    ax.scatter(x=lable_filtered1[0], y=lable_filtered1[1], c='blue')
    ax.scatter(x=lable_filtered2[0], y=lable_filtered2[1], c='black')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Scatter Plot')
    ax.legend()

    st.pyplot(fig)


if __name__=="__main__":
    main()



