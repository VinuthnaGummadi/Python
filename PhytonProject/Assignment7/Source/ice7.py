import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import sent_tokenize, word_tokenize, wordpunct_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.util import ngrams
from collections import Counter
from nltk import pos_tag, ne_chunk
import numpy

words = file('text.txt').read()
print words

#nltk.download('all')
print "wordnet"

for syns in wn.synsets('Computer'):
    for l in syns.lemmas():
        print l.name()
print "\n\n"
print "Sentence Tokenization"
test_text = sent_tokenize(words)
print test_text
print "\n\n"
print "Word Tokenization"
tokens = nltk.word_tokenize(words)
print tokens
print "\n\n"
print  "POS"
print pos_tag(tokens)
print "\n\n"
print "Steming"
stemmer = PorterStemmer()
print(stemmer.stem('Programming'))
print "\n\n"
print "Lemmatization"
lemmatize = WordNetLemmatizer()
print lemmatize.lemmatize('Programming', pos='v')

print "\n\n"
print "Trigrams"
token = nltk.word_tokenize(words)
trigrams = ngrams(token,3)
print Counter(trigrams)
print "\n\n"
print "Named Entity"

print ne_chunk(pos_tag(wordpunct_tokenize(words)))