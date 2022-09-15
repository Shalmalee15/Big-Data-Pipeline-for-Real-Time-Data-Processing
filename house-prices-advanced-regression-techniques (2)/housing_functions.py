import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def scale_data(original_data):
    
    """
    Scale the data to make it generalised

    Parameters
    ----------
    original_data: Original ABS census data

    Returns
    ----------
    A numpy array of scaled data in the form of an array and a dataframe 
    A dataframe of scaled data
    """
    
    data_rescaled = StandardScaler().fit_transform(original_data.values) 
    scaled_features_df = pd.DataFrame(data_rescaled, index=original_data.index, columns=original_data.columns)
    return data_rescaled, scaled_features_df


def calc_pca(scaled_data, num_components): 
    
    """
    Reduce the dimensionality using principal component analysis

    Parameters
    ----------
    scaled_data: Original ABS data scaled using StandardScalar
    n_components: Number of components

    Returns
    ----------
    Explained variance for a given principal component analysis
    Explained variance ratio for a given principal component analysis
    sklearn.decomposition.PCA object
    A numpy array with reduced dimensionality
    
    """
    
    pca = PCA(num_components)
    pca_fit = pca.fit(scaled_data)
    
    return pca


def calc_loadings(pca,census_data): 
    
    """
    Calculate loadings: Contribution from the original variables to the principal components

    Parameters
    ----------

    pca: get pca decomposition parameter from calc_pca() function
    census_data: Original combined census dataset 

    Returns
    ----------
    Loadings 
    """
    
    PCnames = ['PC'+str(i+1) for i in range(pca.n_components_)]
    Loadings = pd.DataFrame(pca.components_.T,columns=PCnames,index=census_data.columns)
    
    return Loadings


def calc_kmeans(X, n_clust, df_scaled): 
    
    """
    Calculate Kmeans clusters

    Parameters
    ----------
    X: PCA reduced array
    n_clust: Number of clusters 
    df_scaled: Original scaled dataframe

    Returns
    ----------
    sklearn.cluster KMeans object
    Pandas dataframe including KMeans clusters
    """
    
    model = KMeans(n_clust)
    label = model.fit_predict(X)
    centers = model.cluster_centers_
    return model, pd.DataFrame(data=label, columns=['cluster'], index=df_scaled.index)


