#-*- coding: utf8 -*-

from nltk import UnigramTagger as ut
from nltk import BigramTagger as bt
from cPickle import dump,load
		
def loadtagger(taggerfilename):
	infile = open(taggerfilename,'rb')
	tagger = load(infile); infile.close()
	return tagger

def traintag(corpusname, corpus):
	# Function to save tagger.
	def savetagger(tagfilename,tagger):
		outfile = open(tagfilename, 'wb')
		dump(tagger,outfile,-1); outfile.close()
		return
	# Training UnigramTagger.
	uni_tag = ut(corpus)
	savetagger(corpusname+'_unigram.tagger',uni_tag)
	# Training BigramTagger.
	bi_tag = bt(corpus)
	savetagger(corpusname+'_bigram.tagger',bi_tag)
	print "Tagger trained with",corpusname,"using" +\
				"UnigramTagger and BigramTagger."
	return
	
# Function to unchunk corpus.
def unchunk(corpus):
	nomwe_corpus = []
	for i in corpus:
		nomwe = " ".join([j[0].replace("_"," ") for j in i])
		nomwe_corpus.append(nomwe.split())
	return nomwe_corpus

class cesstag():
	def __init__(self,mwe=True):
		self.mwe = mwe
		# Train tagger if it's used for the first time.
		try:
			loadtagger('cess_unigram.tagger').tag(['estoy'])
			loadtagger('cess_bigram.tagger').tag(['estoy'])
		except IOError:
			print "*** First-time use of cess tagger ***"
			print "Training tagger ..."
			from nltk.corpus import cess_esp as cess
			cess_sents = cess.tagged_sents()
			traintag('cess',cess_sents)
			# Trains the tagger with no MWE.
			cess_nomwe = unchunk(cess.tagged_sents())
			tagged_cess_nomwe = batch_pos_tag(cess_nomwe)
			traintag('cess_nomwe',tagged_cess_nomwe)
			print
		# Load tagger.
		if self.mwe == True:
			self.uni = loadtagger('cess_unigram.tagger')
			self.bi = loadtagger('cess_bigram.tagger')
		elif self.mwe == False:
			self.uni = loadtagger('cess_nomwe_unigram.tagger')
			self.bi = loadtagger('cess_nomwe_bigram.tagger')

def pos_tag(tokens, mmwe=True):
	tagger = cesstag(mmwe)
	return tagger.uni.tag(tokens)
	
def batch_pos_tag(sentences, mmwe=True):
	tagger = cesstag(mmwe)
	return tagger.uni.batch_tag(sentences)

