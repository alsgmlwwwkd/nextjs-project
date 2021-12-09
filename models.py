import gensim
import requests

def run_bow(lexicon, tokenized_corpus):
    for doc in tokenized_corpus:
        print(lexicon.doc2bow(doc))


def run_one_hot_encoding(lexicon, tokenized_corpus):
    for doc in tokenized_corpus:
        vector = lexicon.doc2bow(doc)
        vector = [(x[0], 1) for x in vector]
        print(vector)

def run_tf_idf(lexicon, tokenized_corpus):
    tfidf = gensim.models.TfidfModel(dictionary=lexicon, normalize=True)
    for doc in tokenized_corpus:
        vector = tfidf[lexicon.doc2bow(doc)]
        print(vector)

def draw_word_cloud():
    requests.post()

if __name__ == '__main__':
    import pandas as pd 

    tokenized_corpus = pd.read_csv('corpus_news.csv')
    lexicon = gensim.corpora.Dictionary(tokenized_corpus)

