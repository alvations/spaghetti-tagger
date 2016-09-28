#-*- coding: utf8 -*-
from __future__ import print_function
import sys

from nltk import UnigramTagger, BigramTagger
from nltk.corpus import cess_esp as cess

try:
    import cPickle as pickle
except ImportError:
    import pickle

def load_tagger(filename):
    """ Function to load tagger. """
    with open(filename,'rb') as fin:
        tagger = pickle.load(fin)
    return tagger

def save_tagger(filename, tagger):
    """ Function to save tagger. """
    with open(filename, 'wb') as fout:
        pickle.dump(tagger, fout)

def train_tagger(corpus_name, corpus):
    """ Function to train tagger. """
    # Training UnigramTagger.
    uni_tag = UnigramTagger(corpus)
    save_tagger('{}_unigram.tagger'.format(corpus_name), uni_tag)
    # Training BigramTagger.
    bi_tag = BigramTagger(corpus, backoff=uni_tag)
    save_tagger('{}_bigram.tagger'.format(corpus_name), bi_tag)
    _msg = str("Tagger trained with {} using "
            "UnigramTagger and BigramTagger.").format(corpus_name)
    print (_msg, file=sys.stderr)

def unchunk(corpus): 
    """ Function to unchunk corpus. """
    nomwe_corpus = []
    for i in corpus:
        nomwe = " ".join([j[0].replace("_"," ") for j in i])
        nomwe_corpus.append(nomwe.split())
    return nomwe_corpus


class CESSTagger():
    def __init__(self,use_mwe=False):
        self.use_mwe = use_mwe
        # Train tagger if it's used for the first time.
        try:
            load_tagger('cess_unigram.tagger').tag(['estoy'])
            load_tagger('cess_bigram.tagger').tag(['estoy'])
        except IOError:
            print ("*** First-time use of cess tagger ***", file=sys.stderr)
            print ("Training tagger ...", file=sys.stderr)
            # Load CESS corpus.
            cess_sents = cess.tagged_sents()
            train_tagger('cess',cess_sents)
            # Trains the tagger with no MWE.
            cess_nomwe = unchunk(cess.tagged_sents())
            tagged_cess_nomwe = pos_tag_sents(cess_nomwe, False)
            train_tagger('cess_nomwe',tagged_cess_nomwe)
        # Load tagger.
        _mwe_option_name = "_nomwe_" if self.use_mwe == True else "_"
        self.uni = load_tagger('cess{}unigram.tagger'.format(_mwe_option_name))
        self.bi = load_tagger('cess{}bigram.tagger'.format(_mwe_option_name))


def pos_tag(tokens, use_mwe=False):
    tagger = CESSTagger(use_mwe)
    return tagger.uni.tag(tokens)
    
def pos_tag_sents(sentences, use_mwe=False):
    tagger = CESSTagger(use_mwe)
    return tagger.uni.tag_sents(sentences)
