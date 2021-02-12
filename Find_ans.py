from numpy import dot
import numpy as np
from konlpy.tag import Okt
from gensim.models import Word2Vec
from numpy.linalg import norm
from testFile import lfr, listm
import MeCab
import json

def cos_sim(vec1, vec2):
    return dot(vec1, vec2)/(norm(vec1)*norm(vec2))

def make_term_doc_mat(sentence_bow, word_dics):
    freq_mat = {}
    for word in word_dics:
        freq_mat[word]=0
        
    for word in word_dics:
        if word in sentence_bow:
            freq_mat[word] +=1

    return freq_mat

# 단어 벡터 만들기
def make_vector(tdm):
    vec=[]
    for key in tdm:
        vec.append(tdm[key])
    return vec




def engine(qu):
    
    m=MeCab.Tagger("-d C:/mecab/mecab-ko-dic")
    
    r1 = 0
    # for j in range(0, len(BOW)):
    #     sBOW = list(BOW[j])
    #     qus = list(qu)
    #     count = 0
    #     for k in range(0, len(qus)):
    #         for n in range(0, len(sBOW)):
    #             if qus[k] == sBOW[n]:
    #                 count += 1
    #             else:
    #                 pass
    #     cos[j] = sum(sBOW)
    #     maxcos = max(cos)
    #     idx = cos.index(maxcos)
    vecto = [k for k in range(0, len(listm))]
    sente = [q for q in range(0, len(listm))]
    sente2 = m.parse(qu)
    for i in range(0, len(listm)):
        sente[i] = m.parse(listm[i])

    for j in range(0, len(listm)):
        sent = sente2+sente[j]
        word_dics = []
        for token in sent:
            if token not in word_dics:
                word_dics.append(token)    
        freq_list1 = make_term_doc_mat(sente2, word_dics)
        freq_list2 = make_term_doc_mat(sente[j], word_dics)

        vec1 = np.array(make_vector(freq_list1))
        vec2 = np.array(make_vector(freq_list2))

        r1 = cos_sim(vec1, vec2)
        vecto[j] = r1                
            
        rmax = max(vecto)
        idx = vecto.index(rmax)
    print(vecto[idx])
    return listm[idx]
        
        

                
        
# print(len(listm))