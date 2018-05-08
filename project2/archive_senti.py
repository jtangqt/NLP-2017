import nltk
from nltk.corpus import wordnet as wn
from nltk.wsd import lesk
import pickle
import sentiwordnet


#sentence = 'As for the spectacle of the battle and showdowns, while not at the scale of Lord of the Rings, I honestly cant think how it could have been done better as the film makers have intertwined heart stopping action with dramatic progressions in the narrative. Its actually more visceral and dynamic than the rather smaller scale battle of the brilliant novels (not to take anything away from Rowlings writing). Do I have any gripes? Yes I do. Although I applaud Steve Kloves for a difficult screenplay adaption...I think he could still have done better at explaining some odd anomalies that only readers of the book will understand. This might annoy you if you havent read the books. But its a small gripe because what we get is delightful. What an amazing achievement to faithfully bring Rowlings epic saga to the big screen with the same cast and largely the same crew, maintaining the brilliant quality right to the end.'.split()
#sentence = 'This is quite possibly the worst movie ever made. Even my 4 year old hated it and wanted to leave. I was using it as an excuse to nap in air-conditioning. Alas, it was so bad that my daughter insisted we leave. Not really a surprise for a Steven Paul film, but Im saddened that Jon Voights career has fallen so low...and Scott Baio??? ARGH! Believe me, Ive had to sit through some bad kid flix, but this one is an all time loser. There is a woman with very large lips (Vanessa Angel) who almost makes it bearable, just for the pure fascination of watching whether or not they will explode. However, my suggestion would be that all prints of this film be sent to President Bush so he can see how harmful his education budget cuts have been.'.split()
#sentence = 'BAD MOVIE, I HATED IT, IT WAS TERRIBLE. NO ONE CAN TOLERATE THIS'.split()
sentence = raw_input("Please specify a sentence. ")
split_sentence = sentence.split()
pos = [nltk.pos_tag(split_sentence)]

hehe = pickle.load(open("sentiwordnet.p", "rb"))

val_neg = 0
val_pos = 0
val_obj = 0 
num = 0

for char, val in pos[0]:
	ss = lesk(sentence, char)
	if ss:
		#print(char, ss.name(), ss.definition())
		word, POS, rank = ss.name().split(".")
		if POS == 's':
			POS = 'a'
		synterm = word + "#" + POS
		print hehe[synterm][rank.lstrip("0")].pos + " " + hehe[synterm][rank.lstrip("0")].neg
		tmp_neg = float(hehe[synterm][rank.lstrip("0")].neg)
		tmp_pos = float(hehe[synterm][rank.lstrip("0")].pos)
		val_neg += tmp_neg
		val_pos += tmp_pos
		if tmp_neg or tmp_pos:
			val_obj += 1 - (tmp_pos + tmp_neg)
			num += 1
		#print ss.definition()
if num == 0: 
	print "Seems like a pretty objective sentence!"
else: 
	tot_pos = val_pos/num
	tot_neg = val_neg/num
	tot_obj = val_obj/num
	print "pos = %.3f, neg = %.3f, obj = %.3f" %(tot_pos, tot_neg, tot_obj)