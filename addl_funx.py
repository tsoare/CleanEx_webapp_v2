#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:32:55 2017

@author: tsoare

These are additional functions needed for Clean_Ex:
"""



# courtesy of @ericmjl:
def compute_alphabet(sequences):
    """
    Returns the alphabet used in a set of sequences.
    """
    alphabet = set()
    for s in sequences:
        alphabet = alphabet.union(set(s))

    return alphabet


# find n-grams:
def find_ngrams(input_list, n):
    """
    Returns the n-grams for a particular sequence:
    """
    return zip(*[input_list[i:] for i in range(n)])


# generate random sequence:
def generate_random_seq(seedno):
    alpha = ['A', 'C', 'T', 'G']
    # random number seed to be replicable for now:
    #seed = np.random.seed(seed=seedno)
    seed = np.random.seed(seed=4256)
    random_seq = np.random.choice(alpha, size=1000)
    return random_seq
