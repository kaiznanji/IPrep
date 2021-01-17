import os
import re
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def get_similarity_score(topic, question, answer):
    for path in os.listdir("dataframes"):
        if path.replace(".csv","") == topic:
            df = pd.read_csv("dataframes/path")
            real_answer = df.loc[df['Question'] == question, 'Answer'].iloc[0]
    
    # pre-proccess real answer for better comparison results
    real_answer = re.sub(r'\W+', ' ', real_answer)
    real_answer = re.sub(r'\b\w{,3}\b', '', real_answer)
    real_answer = re.sub(r'\b\w{13,}\b', '', real_answer)
    real_answer = re.sub(r'\b(\w+)( \1\b)+', r'\1', real_answer)

    # pre-proccess user answer
    answer = re.sub(r'[0-9]+', '', answer)
    answer = re.sub(r'\W+', ' ', answer)
    answer = re.sub(r'\b\w{,3}\b', '', answer)
    answer = re.sub(r'\b\w{13,}\b', '', answer)
    answer = re.sub(r'\b(\w+)( \1\b)+', r'\1', answer)

    # Find similarity
    vectorizer = CountVectorizer()
    score = vectorizer.fit_transform([real_answer, answer])
    score = score[0][1]
    score = round(score * 100)
    
    return score








