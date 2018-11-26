# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 19:21:58 2018
This is a skeleton with the function headers for
the functions you should implement.
You can add more functions

@author: weissr
"""

import nltk
#nltk.download()
from nltk.book import *
from nltk.corpus import gutenberg
import csv


'''
-------------------------
Features
-------------------------
'''
def avg_word_len(words):
    char = 0
    for w in words:
        char = char + len(w)
    return char / len(words)

    
def lexical_div(words):
    '''
    compute the lexical diversity for a list of words
    '''  
    n_words = len(words)
    textlow = [w.lower() for w in words]
    n_vocab = len(set(textlow))
    l_div = n_vocab / n_words  
    return l_div

def n_hapax(words):

    return 0

def hapax_ratio(words):
    file = words
    textlow = [w.lower() for w in file]
    fdist = FreqDist(textlow)
    hapax1 = fdist.hapaxes()
    
    return len(hapax1) / len(file)


def avg_sent_len(words, sentences):
    ''' fill in your code'''
    
    return len(words) / len(sentences)

def avg_sent_complexity(words, sentences):
    file = words
    phrase = file.count(',') + file.count(':') + file.count(';') + len(sentences)
    return phrase / len(sentences)


'''
--------------------------
Compare Signatures
--------------------------
'''

def compute_signature(words, sentences, author):
    sig = [author]
    sig.append(avg_word_len(words))
    sig.append(lexical_div(words))
    sig.append(hapax_ratio(words))
    sig.append(avg_sent_len(words, sentences))
    sig.append(avg_sent_complexity(words, sentences))
    return sig
    
    

def compare_signatures(sig1, sig2, weights):
    '''Return a non-negative real number indicating the similarity of two 
    linguistic signatures. The smaller the number the more similar the 
    signatures. Zero indicates identical signatures.
    sig1 and sig2 are 6 element lists with the following elements
    0  : author name (a string)
    1  : average word length (float)
    2  : lexical diversity (float)
    3  : Hapax Legomana Ratio (float)
    4  : average sentence length (float)
    5  : average sentence complexity (float)
    weight is a list of multiplicative weights to apply to each
    linguistic feature. weight[0] is ignored.
    '''
    
    n_fields = len(sig1)
    score = 0.0
    for i in range(1, n_fields):
        score = score + (abs(sig1[i] - sig2[i])*weights[i-1])
        
    return  score


'''
--------------------------
Reading and Writing files
--------------------------
'''

def write_signatures(sig_list, o_filename):
    f_out = open(o_filename, 'w', newline = '')

    f_out.close()
   
def read_signatures(in_filename):
    f_in = open(in_filename)

    f_in.close()
    
    
def read_text(in_filename):
    try:
        path = 'corpora/gutenberg/' + in_filename
        file = nltk.data.find(path)
        f_in = open(file)
        raw = f_in.read()
        f_in.close()        
    except:
        print('failed to open', in_filename)
        return '' 
    return raw


'''
--------------------------
Printing the output
--------------------------
'''

def print_sig_table(sig_list):
    '''
    for debugging
    '''
    print('list of signatures')
    
def print_scores(sig_list, m_sig_list, weights):
    print('table of scores')
    for i in range(len(sig_list)):
        for x in range(len(m_sig_list)):
            score = compare_signatures(sig_list[i], m_sig_list[x], weights)
            print(sig_list[i][0], m_sig_list[x][0])
            print(str('score = ') + str(score))

            

'''
-------------------------
main
-------------------------
'''
if __name__ == '__main__':
    weights = [11, 33, 50, 0.04, 4]
    sig_list = []
    fileids = gutenberg.fileids()[:2]
    for fid in fileids: 
        # compute features, make a list of features
        words = gutenberg.words(fid)
        sents = gutenberg.sents(fid)
        signature = compute_signature(words, sents, fid)
        sig_list.append(signature)
    print_sig_table(sig_list)
    write_signatures(sig_list, 'test.csv')
    
    n_files = int(input('enter numbr of mystery files: '))
    m_sig_list = []
    for f in range(n_files):
        filename = input('enter name of mystery file: ')
        raw_text = read_text(filename)
    
        '''
        put mystery files in corpora/gutenberg
        '''
        m_words = gutenberg.words(filename)
        m_sents = gutenberg.sents(filename)
        m_sig = compute_signature(m_words, m_sents, filename)
        m_sig_list.append(m_sig)
    
    print_scores(sig_list, m_sig_list, weights)
