import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
import pickle
import sentiwordnet


	
def calculate_score(hehe, sentence, prev_token, curr_token, neg, pos, num):
	if curr_token == len(sentence):
		return neg, pos, num
 	too = wn.synset('excessively.r.01')
	very = wn.synset('very.r.01')
	sorely = wn.synset('sorely.r.01')
	barely = wn.synset('scantily.r.01')
	little = wn.synset('little.a.02')
	inv_not = wn.synset('not.r.01')

	ss_prev = lesk(sentence, prev_token)
	ss = lesk(sentence, sentence[curr_token])
	tmp_neg = 0
	tmp_pos = 0
	if ss:
		pos_tok = ''
		if ss_prev: 
			if ss_prev == too or ss_prev == very or ss_prev == sorely: 
				pos_tok = 'inc'
			elif ss_prev == barely or ss_prev == little: 
				pos_tok = 'dec'
			elif ss_prev == inv_not:
				pos_tok = 'inv'
			
		word, POS, rank = ss.name().split(".")
		if POS == 's':
			POS = 'a'
		synterm = word + "#" + POS
		#print word + " " + hehe[synterm][rank.lstrip("0")].pos + " " + hehe[synterm][rank.lstrip("0")].neg
		
		if pos_tok == 'inc':
			tmp_neg = 2*float(hehe[synterm][rank.lstrip("0")].neg)
			tmp_pos = 2*float(hehe[synterm][rank.lstrip("0")].pos)
		elif pos_tok == 'dec':
			tmp_neg = 0.5*float(hehe[synterm][rank.lstrip("0")].neg)
			tmp_pos = 0.5*float(hehe[synterm][rank.lstrip("0")].pos)		
		elif pos_tok == 'inv':
			tmp_neg = float(hehe[synterm][rank.lstrip("0")].pos)
			tmp_pos = float(hehe[synterm][rank.lstrip("0")].neg)
		else: 
			tmp_neg = float(hehe[synterm][rank.lstrip("0")].neg)
			tmp_pos = float(hehe[synterm][rank.lstrip("0")].pos)
		
		if tmp_neg or tmp_pos:
			num += 1
	return calculate_score(hehe, sentence, sentence[curr_token], curr_token + 1, neg + tmp_neg, pos + tmp_pos, num)



if __name__ == "__main__":
	hehe = pickle.load(open("sentiwordnet.p", "rb"))
	while 1: 
		sentence = raw_input("Please specify a sentence. ")
		split_sentence = sentence.split()
		#pos = [nltk.pos_tag(split_sentence)]

		val_neg, val_pos, num = calculate_score(hehe, split_sentence, split_sentence[0], 1, 0, 0, 0)
		
		if num == 0: 
			print "Seems like a pretty objective sentence"
		else: 
			tot_pos = val_pos/num
			tot_neg = val_neg/num
			tot_obj = 1 - (tot_pos + tot_neg)
			print "pos = %.3f, neg = %.3f, obj = %.3f" %(tot_pos, tot_neg, tot_obj)