import spaghetti as spa

test_sent = 'Mi colega me ayuda a programar cosas .'.split()
tests = [test_sent, 'Está embarazada .'.split()]

# Default Spaghetti tagger.
print spa.pos_tag(test_sent)

# Tag multiple sentences.
print spa.batch_pos_tag(tests)

spa_tagger = spa.cesstag()
# POS tagger trained on unigrams of CESS corpus.
print spa_tagger.uni(test_sent)
# POS tagger traned on bigrams of CESS corpus.
print spa_tagger.bi(test_sent)

spa_mwe_tagger = spa.cesstag(mwe=True) # Recognizes Multi-Word Expressions as one token.
# POS tagger trained on unigrams that includes MWEs from the CESS.
print spa_tagger.uni(test_sent)
# POS tagger trained on bigrams that includes MWEs from the CESS.
print spa_tagger.bi(test_sent)
