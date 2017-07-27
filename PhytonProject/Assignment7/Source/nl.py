import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

words = file('text.txt').read()
print "Words in the file are: \n"
print words

#nltk.download('all')
print "After removing all stopwords: \n"

stop_words = set(stopwords.words("english"))
custom_stopwords = set(('(', ')', '.',',','?','The','[',']'))
all_stopwords = stop_words | custom_stopwords
swords =word_tokenize(words)
filtered_sentence = []
for w in swords:
    if w not in all_stopwords and not w.isdigit() and len(w)>1:
        filtered_sentence.append(w)

print filtered_sentence

print "\n\n"
print "After Lemmatization:\n"
lemmatize = WordNetLemmatizer()
lem_words = []
for w in filtered_sentence:
    lem_words.append(lemmatize.lemmatize(w, pos='v'))
print lem_words

print "\n\n"
print "POS verbs are:"

print nltk.pos_tag(lem_words)
print "After removal of POS verbs:\n"
for tag in nltk.pos_tag(lem_words):
    if(tag[1].startswith('VB')):
        lem_words.remove(tag[0])
print lem_words

print "\n\n"
print "Most Common words are:\n"
fdist = nltk.FreqDist(lem_words)

for w, frequency in fdist.most_common(50):
    print(u'{}-{}'.format(w, frequency))

print "\n\n"

print "Top 5 most frequent words"
print "\n"

for w, frequency in fdist.most_common(5):
    print(u'{}-{}'.format(w, frequency))

print "Most repeated words in the file:\n"
filedist = nltk.FreqDist(swords)
file_rep_words=[]
for w, frequency in filedist.most_common(5):
    print(u'{}-{}'.format(w, frequency))
    file_rep_words.append(w)

print "Most Frequent Words in file are:\n"
print file_rep_words


