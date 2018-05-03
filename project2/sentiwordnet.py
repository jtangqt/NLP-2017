## Read in info 
## Parse POS, ID, positive score, negative score, and end string 
## map of synterms (key = term, element = hash map of synterm rank as key and score object)
## return map from above and use it as a lookup table after POS tagging and Lesk Algorithm 

import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk


class score:
	def __init__(self, pos, neg):
		self.pos = pos
		self.neg = neg

def create_senti_dict():
	senti_file = open('SentiWordNet_3.0.0_20130122.txt')
	senti_line = senti_file.readlines()
	senti_file.close()

	senti_dict = dict()
	for line in senti_line:
		if(line[0] == '#'):
			continue
		POS, ID, p_score, n_score, group_words, defn = line.split("\t")
		
		synterm_split = group_words.split(" ")
		for synterm_and_rank in synterm_split:
			term_and_rank = synterm_and_rank.split("#")
			synterm = term_and_rank[0] + "#" + POS
	 		rank = term_and_rank[1]
	 		tmp_score = score(p_score, n_score)
	 		if synterm in senti_dict:
	 			senti_dict[synterm][rank] = tmp_score
	 			# print("hi")
	 			# print rank + " " + tmp_score.pos + " " + tmp_score.neg
	 		else:
	 			senti_dict[synterm] = {rank: tmp_score}

	return senti_dict



sentence = 'that book is atrocious and i hope that no one ever reads it!!!'.split()
pos = [nltk.pos_tag(sentence)]
print(pos)
print sentence
        #adapt format
pos = [[(word, word, [postag]) for (word, postag) in val] for val in pos]
print(pos)

print sentence

hehe = create_senti_dict()

print wn.synsets('atrocious')
for word in wn.synsets('atrocious'):
	ss = lesk(sentence, 'atrocious')
	print word.definition()
	word, POS, rank = ss.name().split(".")
	if POS == 's':
		POS = 'a'
	synterm = word + "#" + POS
	print hehe[synterm][rank.lstrip("0")].pos + " " + hehe[synterm][rank.lstrip("0")].neg
	print ss.definition()
#print hehe['atrocious#s']

for char in sentence:
	ss = lesk(sentence, char)
	if ss:
		print(ss.name())
		word, POS, rank = ss.name().split(".")
		if POS == 's':
			POS = 'a'
		synterm = word + "#" + POS
		print hehe[synterm][rank.lstrip("0")].pos + " " + hehe[synterm][rank.lstrip("0")].neg
		print ss.definition()
