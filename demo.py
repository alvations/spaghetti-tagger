#-*- coding: utf8 -*-
from __future__ import print_function
import spaghetti as sgt

sent1 = 'Mi colega me ayuda a programar cosas .'.split()
sent2 = 'Está embarazada .'.split()
sent3 = '¿ A lo mejor nos acercamos por fin a una odontología sin dolores ?'.split()
sent4 = '¿ A lo mejor nos acercamos por_fin a una odontología sin dolores ?'.split()
test_sents = [sent1, sent2, sent3]

# Default Spaghetti tagger.
print (sgt.pos_tag(sent1), end="\n\n")

# Tag multiple sentences.
print (sgt.pos_tag_sents(test_sents), end="\n\n")

spa_tagger = sgt.CESSTagger()
# POS tagger trained on unigrams of CESS corpus.
spa_unigram_tagger = spa_tagger.uni
print (spa_unigram_tagger.tag(sent1))
print (spa_unigram_tagger.tag(sent4))
# POS tagger traned on bigrams of CESS corpus.
spa_bigram_tagger = spa_tagger.bi
print (spa_bigram_tagger.tag(sent2))
print (spa_bigram_tagger.tag(sent4))
print (spa_bigram_tagger.tag_sents(test_sents), end="\n\n")

spamwe_tagger = sgt.CESSTagger(use_mwe=True) # Recognizes Multi-Word Expressions as one token.
# POS tagger trained on unigrams that includes MWEs from the CESS.
spamwe_unigram_tagger = spamwe_tagger.uni
print (spamwe_unigram_tagger.tag(sent3))
print (spamwe_unigram_tagger.tag(sent4))
# POS tagger trained on bigrams that includes MWEs from the CESS.
spamwe_bigram_tagger = spamwe_tagger.bi
print (spamwe_unigram_tagger.tag(sent3))
print (spamwe_unigram_tagger.tag(sent4))
print (spamwe_unigram_tagger.tag_sents(test_sents), end="\n\n")

