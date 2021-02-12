import numpy as np
import tensorflow as tf
import pandas as pd
import re
from tensorflow.python.keras.preprocessing.text import Tokenizer
from tensorflow.python.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras import preprocessing
from konlpy.tag import Okt
import json
physical_devices = tf.config.list_physical_devices('GPU') 
tf.config.experimental.set_memory_growth(physical_devices[0], True)
model = tf.keras.models.load_model('sentiment_classifier.h5')
tokenizer = preprocessing.text.Tokenizer()
okt = Okt()
word_index = json.load(open('./data_configs.json', 'r', encoding='utf-8'))

def preprocessing(review,okt, remove_stopwords=False, stop_words=[]):
    review_data = re.sub("[^가-힣ㄱ-ㅎㅏ-ㅣ\\s]","",review)
    review_token = okt.morphs(review_data)
    if remove_stopwords:
        word_review = [token for token in review_token if not token in stop_words]
    return word_review

def sequencing(text):    
    stop_words = ['은', '는', '이', '가', '더', '완전', '아', '진짜', '의', '그', '를', '에', '게']
    sample_token = preprocessing(text, okt, remove_stopwords=True, stop_words=stop_words)
    w = word_index['vocab']
    sample_box = []
    wv = list(w.keys())
    for token in sample_token:
        if "'{}'".format(token) not in wv:
            sample_box.append([0])
        else:
            sample_box.append([w["'{}'".format(token)]])
    return sample_box

def find_sentiment(sample_box):
    sample_input = np.array(sample_box)
    inputs=np.transpose(sample_input)
    sample_seq = pad_sequences(inputs, maxlen=13, padding='post')
    output = model.predict(inputs)
    x=np.where(output==np.max(output))
    return str(x[1][0])