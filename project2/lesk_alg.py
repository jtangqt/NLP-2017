from nltk.corpus import wordnet as wn
from nltk.wsd import lesk

string = 'that movie was shit'.split()

ss = lesk(string, 'shit', 'n')

print(ss, ss.definition())

val = wn.synsets('defecation')
print(val[0].name())

word, POS, rank = val[0].name().split(".")


# print(type(val[0]))
# print(type(wn.synset('defecation.n.01')))
# print(val[0].definition())