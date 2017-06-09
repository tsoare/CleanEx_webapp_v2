#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
These is the function for generating liver expression prediction.
"""

from Bio import SeqIO
import pandas as pd
import numpy as np
from collections import Counter
from nltk import *
from sklearn import linear_model
from .addl_funx import find_ngrams


def ModelIt(user_sequence = [], rand_bf = []):
    #import data and make training model:
    dat = pd.read_csv(open("clean_ex/input_data.csv"))
    dat_X_train = dat.iloc[:, 1:17]
    dat_Y_train = dat['liver']
    regr = linear_model.LinearRegression()
    regr.fit(dat_X_train, dat_Y_train)
    
     # find bi-grams of novel sequence:
    ng = find_ngrams(user_sequence, 2)
    s = pd.Series( list(ng) )
    s_sort = s.sort_values(ascending=True)
    bgm_freq = FreqDist(s_sort)
    #rand_bf.append(bgm_freq)
    #rand_seq_preds = pd.DataFrame(rand_bf)
    #rand_values = rand_seq_preds.values.reshape((16, 1))
    #rand_values = rand_values.reshape(1, -1)
    #print 'The bigrams for this sequence are %i' % rand_seq_preds
    #return ng[0]
    
    # predict expression:
    preds = np.array(bgm_freq.values()).reshape(1, -1)
    result = regr.predict(preds)
    return np.exp2(result[0])
    #if fromUser != 'Default':
    #    return result
    #else:
    #    return 'check your input'

    