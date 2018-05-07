import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
import pickle



'''
inc = too, very, sorely

dec = barely, little

inv = not
'''

too = wn.synset('excessively.r.01')
very = wn.synset('very.r.01')
sorely = wn.synset('sorely.r.01')
barely = wn.synset('scantily.r.01')
little = wn.synset('little.a.02')
inv_not = wn.synset('not.r.01')


print wn.path_similarity(very, barely)
print wn.lch_similarity(too, barely)