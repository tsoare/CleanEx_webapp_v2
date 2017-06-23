#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:34:24 2017

@author: tsoare

Version 3: Most updated model classifying genes as liver-specific.

"""

import pandas as pd
import numpy as np
from collections import Counter
from nltk import *
from sklearn.linear_model import LogisticRegression
from .addl_funx import find_ngrams
from Bio import SeqIO
import pickle

#user_file = 'my_promoters_to_test.fa'

def ModelIt(user_file):
    #if len(user_sequence) < 998:
    #    return 'ERROR: Sequence must be 1000bp or greater'
    #else:
    #print user_file
    filename = 'clean_ex2/logreg_model_basic.sav'
    my_logreg2 = pickle.load(open(filename, 'rb'))
    #print my_logreg2.coef_
    
    grams = [2, 3, 4]
    motifs = {('A', 'C'), ('A', 'G', 'G'), ('A', 'G', 'G', 'G'), 
                  ('C', 'C'), ('C', 'G'), ('C', 'G', 'A', 'A'), 
                  ('C', 'T'), ('C', 'T', 'G'), ('T', 'C', 'A'), 
                  ('T', 'C', 'T'), ('T', 'G', 'G')}
    
    results = []
    #print SeqIO.parse(user_file, "fasta")
    for seq_record in SeqIO.parse(user_file, "fasta"):
        #print seq_record.id
        bfs = dict()
        
        for g in grams:
            # find g-grams:
            ng = find_ngrams(seq_record.seq, g)
            s = pd.Series( list(ng) )
            s_sort = s.sort_values(ascending=True)
            bgm_freq = FreqDist(s_sort)
            
            # concatenate across multiple g's:
            bfs.update(bgm_freq)
        #print g
        
        # subset to relevant features:
        bm = []
        for m in motifs:
            b = bfs.get(m)
            if b is None:
                b = 0
            bm.append(b)
        
        X_test = np.asarray(bm)
        #print X_test
        # return probability of being highly expressed:
        r = my_logreg2.predict_proba(X=X_test.reshape(1, -1)).flatten()
        #print r
        #r = my_logreg2.predict(X=X_test.reshape(1, -1))
        results.append([seq_record.id, r[1]])
        #results.append([seq_record.id, r[0]])
    
    results2 = pd.DataFrame(results)
    results2.columns = ['Fasta_header', 'Probability_liver_specific']
    #results2.columns = ['Fasta_header', 'Class_prediction']
    #print list(results2)
    #print results2.to_html()
    return results2.round(4).to_html()




