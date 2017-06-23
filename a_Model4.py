#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:34:24 2017

@author: tsoare

Version 4: Most updated model classifying genes as liver-specific.

"""

import pandas as pd
import numpy as np
from collections import Counter
from nltk import FreqDist
from sklearn.linear_model import LogisticRegression
from .addl_funx import find_ngrams, compute_alphabet
from Bio import SeqIO
import pickle


def ModelIt(pass_records):
    
    
    # load model and input parameters:
    modelfile = 'clean_ex2/logreg_model_basic.sav'
    meansfile = 'clean_ex2/feature_means.sav'
    SDsfile = 'clean_ex2/feature_SDs.sav'
    
    print modelfile
    print meansfile
    print SDsfile
    
    my_logreg2 = pickle.load(open(modelfile, 'rb'))
    print my_logreg2
    means = pickle.load(open(meansfile, 'rb'))
    print means
    SDs = pickle.load(open(SDsfile, 'rb'))
    print SDs

    
    grams = [2, 3, 4]
    motifs = {('A', 'C'), ('A', 'G', 'G'), ('A', 'G', 'G', 'G'), 
                  ('C', 'C'), ('C', 'G'), ('C', 'G', 'A', 'A'), 
                  ('C', 'T'), ('C', 'T', 'G'), ('T', 'C', 'A'), 
                  ('T', 'C', 'T'), ('T', 'G', 'G')}
    
    results = []
    
    #print SeqIO.parse(user_file, "fasta")
    for seq_record in pass_records:
        bfs = dict()
            
        # find g-grams:
        for g in grams:
            ng = find_ngrams(seq_record.seq, g)
            s = pd.Series( list(ng) )
            s_sort = s.sort_values(ascending=True)
            bgm_freq = FreqDist(s_sort)
    
            # concatenate across multiple g's:
            bfs.update(bgm_freq)
        
        # subset to relevant features:
        bm = []
        for m in motifs:
            b = bfs.get(m)
            if b is None:
                b = 0
            bm.append(b)
    
        # convert to array and normalize features:
        X_test = np.asarray(bm)
        X_test = X_test - means / SDs
        
        # return probability of being highly expressed:
        r = my_logreg2.predict_proba(X=X_test.reshape(1, -1)).flatten()
        results.append([seq_record.id, r[1]])
    
    results2 = pd.DataFrame(results)
    #print(results2)
    results2.columns = ['FASTA file header', 'Probability sequence\nis liver specific']

    #print results2.to_html()
    results2.index = results2.index + 1
    
    
    return results2.round(4).to_html(classes=["table table-striped table-hover table-responsive"])




