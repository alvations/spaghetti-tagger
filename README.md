**Spaghetti tagger** is just a simple recipe for Spanish POS tagging using the CESS corpus with NLTK's implementation of bigram and unigram taggers. It's not perfect, nor state-of-art but it's useful =)

Usage
====

```python
from __future__ import print_function
import spaghetti as sgt

sent1 = 'Mi colega me ayuda a programar cosas .'.split()
sent2 = 'Está embarazada .'.split()
test_sents = [sent1, sent2]

# Default Spaghetti tagger.
print (sgt.pos_tag(test_sent))

# Tag multiple sentences.
print (sgt.pos_tag_sents(test_sents))

spa_tagger = sgt.CESSTagger()
# POS tagger trained on unigrams of CESS corpus.
spa_unigram_tagger = spa_tagger.uni
print (spa_unigram_tagger.tag(sent1))
# POS tagger traned on bigrams of CESS corpus.
spa_bigram_tagger = spa_tagger.bi
print (spa_bigram_tagger.tag(sent2))
print (spa_bigram_tagger.tag_sents(test_sents))
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



