import re
import pandas as pd

def clean_doc(doc):
    print(doc)
    clean = re.sub(r'[^\wㄱ-ㅎ가-힣]', ' ', doc)
    
    return clean

def read_data(path):
    df = pd.read_csv(path)
    df = df.loc[:, ['title', 'summary']]
    df.summary = df.summary.str.rstrip('…').str.strip()
    
    df = df.dropna()
    df.title = df.title.apply(clean_doc)
    df.summary = df.summary.apply(clean_doc)
    
    return df

def to_corpus(path):
    df = read_data(path)
    corpus = df.values.flatten()
    return corpus
    
def tokenized_corpus(corpus):
    return [han.morphs(x) for x in corpus]