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
    file = gutenberg.words(file_id)
    textlow = [w.lower() for w in file]
    fdist = FreqDist(textlow)
    hapax1 = fdist.hapaxes()
    #textlow = [w.lower() for w in file]
    #single = [w for w in textlow if textlow.count(w) == 1]
    return len(hapax1) / len(file)

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


def minmax(category):
    maxi = 0
    mini = textDict['emma'][category]
    for key in textDict:
        if textDict[key][category] > maxi:
            maxi = textDict[key][category]
        if textDict[key][category] < mini:
            mini = textDict[key][category]
    diff = maxi - mini
    print('max is ' + str(maxi) + ' and min is ' + str(mini) + ' and diff is ' + str(diff))
    for key in textDict:
        ratio = (textDict[key][category] - mini) / diff
        rounded = round(ratio, 3)
        print(textDict[key][0] + ' weighted score is ' + str(rounded))

            

if __name__ == '__main__':
    for fid in gutenberg.fileids(): 
        # compute features, make a list of features
        features = []
        #features.append('AWL: ')
        features.append(round(avgwordlen(fid), 3))
       # features.append('LD: ')
        features.append(round(lexical_div(fid), 3))
        #features.append('HLR: ')
        features.append(round(hapax(fid), 3))
       # features.append('WPS: ')
        features.append(round(words_per_sent(fid), 3))      
       # features.append('PPS: ')
        features.append(round(phrasePerSent(fid), 3))
        #name = ''
        #for char in fid:
        #    while char != '-':
        #        name = name + str(char)
        
        
        
        
        #features.append(round(words_per_sent(fid), 3))
        #features.append(round(phrasePerSent(fid), 3))
       
        print(fid, features)
        
        
        textDict = {'emma': ['austen', 3.755, .038, .015, 24.823, 2.778],
        'persuasion': ['austen', 3.871, .059, .026, 26.2, 3.179],
        'sense': ['austen', 3.881, 0.045, 0.017, 28.321, 3.174],
        'kjv': ['bible', 3.448, 0.013, 0.004, 33.573, 5.131],
        'poems': ['blake', 3.503, 0.184, 0.097, 19.073, 2.947],
        'stories': ['bryant', 3.5, 0.071, 0.03, 19.407, 2.411],
        'busterbrown': ['burgess', 3.517, 0.082, 0.033, 17.991, 1.8],
        'alice': ['carroll', 3.401, 0.077, 0.033, 20.029, 2.406],
        'ball': ['chesterton', 3.825, 0.086, 0.042, 20.296, 2.122],
       'brown': ['chesterton', 3.791, 0.091, 0.044, 22.612, 2.315],
        'thursday': ['chesterton', 3.774, 0.092, 0.045, 18.496, 2.024],
        'parents': ['edgeworth', 3.509, 0.04, 0.015, 20.593, 2.754],
        'moby_dick': ['melville', 3.509, 0.04, 0.015, 20.593, 2.754],
        'paradise': ['milton', 3.887, 0.093, 0.044, 52.31, 8.165],
        'caesar': ['shakespeare', 3.444, 0.117, 0.064, 11.943, 2.299],
        'hamlet': ['shakespeare', 3.464, 0.126, 0.076, 12.028, 2.209],
        'macbeth': ['shakespeare', 3.465, 0.15, 0.09, 12.134, 2.306],
        'leaves': ['whitman', 3.696, 0.08, 0.037, 36.443, 5.262]}
        
        
        emma = ['austen', 3.755, .038, .015, 24.823, 2.778]
        persuasion = ['austen', 3.871, .059, .026, 26.2, 3.179]
        sense = ['austen', 3.881, 0.045, 0.017, 28.321, 3.174]
        kjv = ['bible', 3.448, 0.013, 0.004, 33.573, 5.131]
        poems = ['blake', 3.503, 0.184, 0.097, 19.073, 2.947]
        stories = ['bryant', 3.5, 0.071, 0.03, 19.407, 2.411]
        busterbrown = ['burgess', 3.517, 0.082, 0.033, 17.991, 1.8]
        alice = ['carroll', 3.401, 0.077, 0.033, 20.029, 2.406]
        ball = ['chesterton', 3.825, 0.086, 0.042, 20.296, 2.122]
        brown = ['chesterton', 3.791, 0.091, 0.044, 22.612, 2.315]
        thursday = ['chesterton', 3.774, 0.092, 0.045, 18.496, 2.024]
        parents = ['edgeworth', 3.509, 0.04, 0.015, 20.593, 2.754]
        moby_dick = ['melville', 3.509, 0.04, 0.015, 20.593, 2.754]
        paradise = ['milton', 3.887, 0.093, 0.044, 52.31, 8.165]
        caesar = ['shakespeare', 3.444, 0.117, 0.064, 11.943, 2.299]
        hamlet = ['shakespeare', 3.464, 0.126, 0.076, 12.028, 2.209]
        macbeth = ['shakespeare', 3.465, 0.15, 0.09, 12.134, 2.306]
        leaves = ['whitman', 3.696, 0.08, 0.037, 36.443, 5.262]
        weight = [0, 30, 30, 30, 10, 20]
