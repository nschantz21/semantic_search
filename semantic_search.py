"""
semantic_search.py

Implementation of word2vec skip-gram model
"""
import pandas as pd
from gensim.models import KeyedVectors

def semantic_search(query_word: str):
    """
    Function to get the most similar trend terms
    """
    # cbow model
    cbow_wv = KeyedVectors.load("/content/drive/MyDrive/NWO Project/model1_vectors.kv", mmap='r')
    # skip gram model
    skipgram_wv = KeyedVectors.load("/content/drive/MyDrive/NWO Project/model2_vectors.kv", mmap='r')
    topn=1000
    cbow_sim = cbow_wv.most_similar(query_word, topn=100)
    sg_sim = skipgram_wv.most_similar(query_word, topn=100)
    cbow_sim_frame = pd.DataFrame(cbow_sim).set_index(0)
    sg_sim_frame = pd.DataFrame(sg_sim).set_index(0)
    average_score = (cbow_sim_frame.add(sg_sim_frame, fill_value=0.0).sort_values(by=1) / 2).head(topn)
    return average_score
  
