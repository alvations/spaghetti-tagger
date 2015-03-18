**Spaghetti tagger** is just a simple recipe for Spanish POS tagging using the CESS corpus with NLTK's implementation of bigram and unigram taggers. It's not perfect, nor state-of-art but it's useful =)

Usage
====

```
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

```

References
====

**CESS**

Antonia Martí, Mariona Taulé, Lluís Márquez, Manuel Bertran. 2007. CESS-ECE: A Multilingual and Multilevel Annotated Corpus. see http://www.lsi.upc.edu/~mbertran/cess-ece/publications

**NLTK**

Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc. see http://nltk.org/

----------------------------------------------------------------------------------------

See Also
====

* [Freeling Suite](https://nlp.lsi.upc.edu/freeling) - _with Spanish and other languages_

* [Deutsche Language ToolKit (DLTK)](https://github.com/alvations/dltk.github.io) - _for German NLP_



