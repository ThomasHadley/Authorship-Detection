# -*- coding: utf-8 -*-
"""
template for authorship_part1.py
You can print out a table with one row for each files,
and the columns are the features, e.g. lexical diversity.
You can add your own features.  Each feature should have its own function.

"""

import nltk
#nltk.download()
from nltk.book import *
from nltk.corpus import gutenberg

emma = nltk.corpus.gutenberg.words('austen-emma.txt')

def avgwordlen(file_id):
    char = 0
    for w in gutenberg.words(file_id):
        char = char + len(w)
    return char / len(gutenberg.words(file_id))

def hapax(file_id):
    file = sorted(gutenberg.words(file_id))
    textlow = [w.lower() for w in file]
    single = [w for w in textlow if textlow.count(w) == 1]
    return len(single) / len(file)

def lexical_div(file_id):
    '''
    compute the lexical diversity for a files in 
    the gutenberg corpus.  
    '''
    n_words = len(gutenberg.words(file_id))
    textlow = [w.lower() for w in gutenberg.words(file_id)]
    n_vocab = len(set(textlow))
    l_div = n_vocab / n_words  
    return l_div

def words_per_sent(file_id):
    ''' fill in your code'''
    sents = len(gutenberg.sents(file_id))
    words = len(gutenberg.words(file_id))
    return words/sents

def phrasePerSent(file_id):
    file = gutenberg.words(file_id)
    phrase = file.count(',') + file.count(':') + file.count(';') + len(gutenberg.sents(fid))
    return phrase / len(gutenberg.sents(file_id))
    
def compare_signatures(sig1, sig2, weight):
    '''Return a non-negative real number indicating the similarity of two 
    linguistic signatures. The smaller the number the more similar the 
    signatures. Zero indicates identical signatures.
    sig1 and sig2 are 6 element lists with the following elements
    0  : author name (a string)
    1  : average word length (float)
    2  : TTR (float)
    3  : Hapax Legomana Ratio (float)
    4  : average sentence length (float)
    5  : average sentence complexity (float)
    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.
    '''
    n_fields = len(sig1)
    score = 0.0
    for i in range(1,n_fields):
        score += abs(sig1[i] - sig2[i])*weight[i]
        
    return  score

            

if __name__ == '__main__':
    for fid in gutenberg.fileids(): 
        # compute features, make a list of features
        features = []
        features.append('LD: ')
        features.append(round(lexical_div(fid), 3))
        features.append('WPS: ')
        features.append(round(words_per_sent(fid), 3))
        features.append('AWL: ')
        features.append(round(avgwordlen(fid), 3))
        features.append('PPS: ')
        features.append(round(phrasePerSent(fid), 3))
        
        #features.append(round(words_per_sent(fid), 3))
        #features.append(round(phrasePerSent(fid), 3))
       # features.append(hapax(fid))
        print(fid, features)

    
