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

    k = st.number_input("insert the number of clusters you want:", min_value=1, max_value=11, value=3)    

    kmeans=KMeans(n_clusters=k)

    labels=kmeans.fit_predict(X)
    scaled_X['label']=labels
    lable_filtered0=scaled_X.loc[scaled_X['label'] == 0]
    lable_filtered1=scaled_X.loc[scaled_X['label'] == 1]
    lable_filtered2=scaled_X.loc[scaled_X['label'] == 2]
    lable_filtered3=scaled_X.loc[scaled_X['label'] == 3]
    lable_filtered4=scaled_X.loc[scaled_X['label'] == 4]
    lable_filtered5=scaled_X.loc[scaled_X['label'] == 5]
    lable_filtered6=scaled_X.loc[scaled_X['label'] == 6]
    lable_filtered7=scaled_X.loc[scaled_X['label'] == 7]
    lable_filtered8=scaled_X.loc[scaled_X['label'] == 8]
    lable_filtered9=scaled_X.loc[scaled_X['label'] == 9]
    lable_filtered10=scaled_X.loc[scaled_X['label'] == 10]
    lable_filtered11=scaled_X.loc[scaled_X['label'] == 11]


    fig, ax = plt.subplots()
    ax.scatter(x=lable_filtered0[0], y=lable_filtered0[1], c='red')
    ax.scatter(x=lable_filtered1[0], y=lable_filtered1[1], c='blue')
    ax.scatter(x=lable_filtered2[0], y=lable_filtered2[1], c='black')
    ax.scatter(x=lable_filtered3[0], y=lable_filtered3[1], c='yellow')
    ax.scatter(x=lable_filtered4[0], y=lable_filtered4[1], c='purple')
    ax.scatter(x=lable_filtered5[0], y=lable_filtered5[1], c='brown')
    ax.scatter(x=lable_filtered6[0], y=lable_filtered6[1], c='green')
    ax.scatter(x=lable_filtered7[0], y=lable_filtered7[1], c='aqua')
    ax.scatter(x=lable_filtered8[0], y=lable_filtered8[1], c='violet')
    ax.scatter(x=lable_filtered9[0], y=lable_filtered9[1], c='pink')
    ax.scatter(x=lable_filtered10[0], y=lable_filtered10[1], c='lightsteelblue')
    ax.scatter(x=lable_filtered11[0], y=lable_filtered11[1], c='thistle')

    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')
    ax.set_title('Scatter Plot')
    ax.legend()

    st.pyplot(fig)


if __name__=="__main__":
    main()



