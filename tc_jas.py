import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from math import log
import string

nltk.download('popular')

def tc(training_file_name, test_file_name):
	k = 0.06

	##Training
	stemmer = PorterStemmer() #begin stemmers
	d_word_cat = dict() #dictionary that stores the word count/category
	d_cat = dict() #dictionary that stores the token count/category
	d_prior = dict() #dictionary that counts files per category

	#Read in file name
	training_file = open(training_file_name, 'r')
	training_lines = training_file.read().splitlines()

	for line in training_lines:
		#parse (file name vs category)
		cat_file = line.split()
		
		#add one to the category 
		cat = cat_file[1] 
		if cat in d_prior:
			d_prior[cat] += 1.
		else: 
			d_prior[cat] = 1.

		#read in training file and tokenize 
		train_file = open('TC_provided/' + cat_file[0], 'r')
		train_file_tok = word_tokenize(train_file.read())
		
		#loop through words in this file
		i = 1
		for tok in train_file_tok:
			#first find the stem of the token
			tok = stemmer.stem(tok)
			if tok in list(string.punctuation):
				continue

			#find number of times this word appears in this category
			if(cat, tok) in d_word_cat:
				d_word_cat[(cat, tok)] += 1.
			else:
				d_word_cat[(cat, tok)] = 1.
 			
 			#count number of tokens in this category 
 			i += 1

 		if cat in d_cat:
 			d_cat[cat] += i
 		else: 
 			d_cat[cat] = i

	training_file.close()

	##Testing
	testing_file = open(test_file_name, 'r')
	testing_lines = testing_file.read().splitlines()

	##Finding output file
	output_name = raw_input('Please specify the output file name: ')
	output_file = open(output_name, 'w')

	num_train_files = sum(d_prior.values())
 	set_cat = d_cat.keys()

	#Loop through each test file
	for line in testing_lines: 
		#read in training file and tokenize
		test_file = open('TC_provided/' + line, 'r')
		test_file_tok = word_tokenize(test_file.read())

		#create a temp dictionary
		d_tmp = dict()

		for tmp_tok in test_file_tok:
			#apply stemmer to token
			tmp_tok = stemmer.stem(tmp_tok)

			if tmp_tok in list(string.punctuation):
				continue
			
			#add to temporary dictionary 
			if tmp_tok in d_tmp:
				d_tmp[tmp_tok] += 1.
			else: 
				d_tmp[tmp_tok] = 1.				

		len_vocab = len(d_tmp)
		cat_prob = dict()

		#Do Naive Bayes
		for cat in set_cat:
			total_cat_prob = 0
			prior = d_prior[cat]/num_train_files
			normalizer = d_cat[cat] + k*len_vocab

			for word, count in d_tmp.iteritems():
				if(cat, word) in d_word_cat:
					word_count_given_cat = d_word_cat[(cat, word)] + k
				else:
					word_count_given_cat = k

				total_cat_prob += count*log(word_count_given_cat/normalizer)
			cat_prob[cat] = total_cat_prob + log(prior)

		res = max(cat_prob, key = cat_prob.get)

		#Print out prediction into output file 
		output_file.write(line + ' ' + res + '\n')

	testing_file.close()
	output_file.close()

	return


training_name = raw_input('Please specify the training file name: ')
test_name = raw_input('Please specify the test file name: ')

tc(training_name, test_name)