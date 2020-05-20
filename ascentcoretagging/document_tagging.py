import tensorflow as tf
import pandas as pd
import numpy as np
from scipy import spatial
from sklearn.manifold import TSNE
import spacy
from nltk.cluster import KMeansClusterer
import nltk
from sklearn import cluster
from scipy.spatial import distance
from sklearn.cluster import KMeans
from bs4 import BeautifulSoup
from markdown import markdown
import os
import markdown
import itertools
import json
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize
from sklearn.metrics import pairwise_distances
from sklearn.metrics import silhouette_score
from nltk.corpus import words
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('words')
from collections import Counter
import re
nlp = spacy.load("en_core_web_sm")
stopwords_list = list(set(stopwords.words('english')))


# Markdown to text

def markdown_to_text(markdown_string):
    # md -> html -> text since BeautifulSoup can extract text cleanly
    html = markdown.markdown(markdown_string)

    # extract text
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(text=True))

    return text


# Parse documents

def parse_documents(md_documents):
    vocabulary = []
    data = []
    filenames = []
    for filename in os.listdir(md_documents):
        f = open(md_documents + '/' + filename, 'r')
        markdown2text = markdown_to_text( f.read() )
        
        wordlist = re.findall(r'\w+', markdown2text)
        wordlist_lower = [word.lower() for word in wordlist]
        
        wordlist_english = [word for word in wordlist_lower if word in words.words()]
        wordlist_english_without_stopwords = [word for word in wordlist_english if word not in stopwords_list]

        wordlist_english_without_stopwords_nouns = []
        for word in wordlist_english_without_stopwords:
            for token in nlp(word):
                if (token.tag_ == 'NN' or token.tag_ == 'NNP'):
                    wordlist_english_without_stopwords_nouns.append(token.lemma_)

        wordlist_english_without_stopwords_nouns_no_duplicates = list(set(wordlist_english_without_stopwords_nouns))
        wordlist_english_without_stopwords_nouns_no_duplicates.sort()

        # nouns from all documents
        vocabulary.append(wordlist_english_without_stopwords_nouns_no_duplicates)

        word_english_without_stopwords_nouns_no_duplicates = ' '.join(wordlist_english_without_stopwords_nouns_no_duplicates)
        data.append(word_english_without_stopwords_nouns_no_duplicates)
        filenames.append(filename)

    vocabulary = list(itertools.chain.from_iterable(vocabulary))
    vocabulary = list(set(vocabulary))
    vocabulary.sort()

    return data, vocabulary, filenames


# Parse NEW documents - testing

def parse_new_documents_test(md_documents, vocabulary):
    data = []
    filenames = []
    for filename in os.listdir(md_documents):
        f = open(md_documents + '/' + filename, 'r')
        markdown2text = markdown_to_text( f.read() )
        
        wordlist = re.findall(r'\w+', markdown2text)
        wordlist_lower = [word.lower() for word in wordlist]
        
        wordlist_english = [word for word in wordlist_lower if word in words.words()]
        wordlist_english_without_stopwords = [word for word in wordlist_english if word not in stopwords_list]

        wordlist_english_without_stopwords_nouns = []
        for word in wordlist_english_without_stopwords:
            for token in nlp(word):
                if (token.lemma_ in vocabulary and (token.tag_ == 'NN' or token.tag_ == 'NNP')):
                    wordlist_english_without_stopwords_nouns.append(token.lemma_)

        wordlist_english_without_stopwords_nouns_no_duplicates = list(set(wordlist_english_without_stopwords_nouns))
        wordlist_english_without_stopwords_nouns_no_duplicates.sort()

        word_english_without_stopwords_nouns_no_duplicates = ' '.join(wordlist_english_without_stopwords_nouns_no_duplicates)
        data.append(word_english_without_stopwords_nouns_no_duplicates)
        filenames.append(filename)

    return data, filenames


# TfidfVectorizer

def tfidfVectorizer(data, vocabulary):
    tf_idf_vectorizor = TfidfVectorizer(vocabulary = vocabulary)

    tf_idf = tf_idf_vectorizor.fit_transform(data)
    tf_idf_norm = normalize(tf_idf)
    tf_idf_array = tf_idf_norm.toarray()

    return tf_idf_array, tf_idf_vectorizor


# TfidfVectorizer - testing

def tfidfVectorizer_testing(tf_idf_vectorizor, data_test):
    tf_idf_test = tf_idf_vectorizor.transform(data_test)
    tf_idf_norm_test = normalize(tf_idf_test)
    tf_idf_array_test = tf_idf_norm_test.toarray()

    return tf_idf_array_test


# PCA

def pca(tf_idf_array):
    sklearn_pca = PCA(n_components = 2)
    Y_sklearn = sklearn_pca.fit_transform(tf_idf_array)

    return sklearn_pca, Y_sklearn


# PCA - testing

def pca_testing(sklearn_pca, tf_idf_array_test):
    Y_sklearn_test = sklearn_pca.transform(tf_idf_array_test)

    return Y_sklearn_test


# Silhouette

def silhouette(Y_sklearn):
    range_n_clusters = range(2, 10)
    scores = []
    number_clusters_list = []
    for n_clusters in range_n_clusters:
        clusterer = KMeans(n_clusters=n_clusters)
        preds = clusterer.fit_predict(Y_sklearn)

        score = silhouette_score(Y_sklearn, preds)
        scores.append(score)
        number_clusters_list.append(n_clusters)

    max_score = max(scores)
    index = scores.index(max_score)
    optimal_number_cluster = number_clusters_list[index]

    return optimal_number_cluster


# K-means algorithm methods

class Kmeans:
    
    def __init__(self, k, seed = None, max_iter = 200):
        self.k = k
        self.seed = seed
        if self.seed is not None:
            np.random.seed(self.seed)
        self.max_iter = max_iter
    

    def initialise_centroids(self, data):
        initial_centroids = np.random.permutation(data.shape[0])[:self.k]
        self.centroids = data[initial_centroids]

        return self.centroids
    
    
    def assign_clusters(self, data):
        if data.ndim == 1:
            data = data.reshape(-1, 1)
        
        dist_to_centroid =  pairwise_distances(data, self.centroids, metric = 'euclidean')
        self.cluster_labels = np.argmin(dist_to_centroid, axis = 1)
        
        return  self.cluster_labels
    
    
    def update_centroids(self, data):
        self.centroids = np.array([data[self.cluster_labels == i].mean(axis = 0) for i in range(self.k)])
        
        return self.centroids
    
    
    def convergence_calculation(self):
        pass
    

    def predict(self, data):
        return self.assign_clusters(data)
    
    
    def fit_kmeans(self, data):
        self.centroids = self.initialise_centroids(data)
        
        # Main kmeans loop
        for iter in range(self.max_iter):

            self.cluster_labels = self.assign_clusters(data)
            self.centroids = self.update_centroids(data)          
            if iter % 100 == 0:
                print("Running Model Iteration %d " %iter)
        print("Model finished running")
        return self


# K-means applied

def kmeansAlg(Y_sklearn, optimal_number_cluster):
    test_e = Kmeans(optimal_number_cluster, 1, 600)
    _ = test_e.fit_kmeans(Y_sklearn)
    predicted_values = test_e.predict(Y_sklearn)

    return test_e, predicted_values


# K-means applied - testing

def kmeansAlg_testing(test_e, Y_sklearn_test):
    predicted_values_test = test_e.predict(Y_sklearn_test)

    return predicted_values_test


# Get Top Features Cluster

def get_top_features_cluster(tf_idf_array, tf_idf_vectorizor, prediction, n_feats):
    labels = np.unique(prediction)
    dfs = []
    for label in labels:
        id_temp = np.where(prediction==label) # indices for each cluster
        x_means = np.mean(tf_idf_array[id_temp], axis = 0) # returns average score across cluster
        sorted_means = np.argsort(x_means)[::-1][:n_feats] # indices with top 20 scores
        features = tf_idf_vectorizor.get_feature_names()
        best_features = [(features[i], x_means[i]) for i in sorted_means]
        
        df = pd.DataFrame(best_features, columns = ['features', 'score'])
        dfs.append(df)
    return dfs


# Create JSON with clusters

def createJSON(predicted_values, optimal_number_cluster, filenames):
    clusters = {}
    predicted_values = list(predicted_values)
    for i in range(0, optimal_number_cluster):
        indexs = [idx for idx, predicted_value in enumerate(predicted_values) if predicted_value == i]
        docs = [filename for idx, filename in enumerate(filenames) if idx in indexs]
        clusters['cluster_{}'.format(i)] = docs

    return clusters


# Create JSON with clusters - testing

def createJSON_test(predicted_values_test, filenames_test):
    clusters = {}
    predicted_values_test = list(predicted_values_test)
    for i in Counter(predicted_values_test).keys():
        indexs = [idx for idx, predicted_value in enumerate(predicted_values_test) if predicted_value == i]
        docs = [filename for idx, filename in enumerate(filenames_test) if idx in indexs]
        clusters['cluster_{}'.format(i)] = docs

    return clusters


# Save features to csv

def saveFeaturesToCSV(dfs):
    for i, df in enumerate(dfs):
        df.to_csv('cluster'+str(i)+'_features.csv')


# Flow "train"

vocabulary_aux = []
def train(md_documents):
    data, vocabulary, filenames = parse_documents(md_documents)
    global vocabulary_aux
    vocabulary_aux = vocabulary
    global tf_idf_vectorizor
    tf_idf_array, tf_idf_vectorizor = tfidfVectorizer(data, vocabulary)
    global sklearn_pca
    sklearn_pca, Y_sklearn = pca(tf_idf_array)
    optimal_number_cluster = silhouette(Y_sklearn)
    global test_e
    test_e, predicted_values = kmeansAlg(Y_sklearn, optimal_number_cluster)
    clusters = createJSON(predicted_values, optimal_number_cluster, filenames)

    json_dump = json.dumps(clusters)
    json_object = json.loads(json_dump)

    dfs = get_top_features_cluster(tf_idf_array, tf_idf_vectorizor, np.array(predicted_values), 10)
    saveFeaturesToCSV(dfs)

    return json_object


# Flow "test"

def test(md_documents_test):
    data_test, filenames_test = parse_new_documents_test(md_documents_test, vocabulary_aux)
    tf_idf_array_test = tfidfVectorizer_testing(tf_idf_vectorizor, data_test)
    Y_sklearn_test = pca_testing(sklearn_pca, tf_idf_array_test)
    predicted_values_test = kmeansAlg_testing(test_e, Y_sklearn_test)
    clusters = createJSON_test(predicted_values_test, filenames_test)

    json_dump = json.dumps(clusters)
    json_object = json.loads(json_dump)

    return json_object