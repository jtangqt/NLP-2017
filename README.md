# NLP-2017
Sable's NLP Class Spring 2018


## Dependency list:
requires python & pip

```
$ git clone git@github.com:jtangqt/NLP-2017.git
$ cd NLP-2017
$ pip install -r requirements.txt
$ python jasmineqtang_TC.py
```
All training/test files should stay in TC_provided directory.


## ML Method 
The method used is Naive Bayes as shown in class. 

## Parsing/Tokenizer then Stemming
For training and test sets, the document was taken in and the command 'splitlines()' was used. From there, the training sets would use word tokenizer, which is a built in tool in thes nltk library, to split between the names of the article and it's label. __
In the article, word tokenizer would also be used to determine the word. Then the word was then put into the Porter Stemmer to obtain the stem of the word. The Porter Stemmer is considered a gentler stemmer in comparison to the Lancaster Stemmer. With the stem of the word, we can associate words with the category for the Naive Bayes Approach. __
The last step before adding words to any form of hash table/having it factor into the probabilities, 'if tok in list[string.punctuation]' got rid of the punctuation and continued to the next iteration of the for loop. 

## Weighting Scheme 


## Smoothing 
Laplacian Smoothing with k at 0.05. 

## Optional Parameters


## Performance for Second and Third Data Set
The training set for corpus 2 and corpus 3 were split to about 75% for the training set and 25% for the test set. The code in create_cv.py takes the training sets, randomizes the order, and creates a new training set, test set list and test set. 
With the new sets generated locally by create_cv.py, corpus 2 had an 80.9% ratio of correct. The F1 of I was 0.74 while the F1 of O was 0.85. As for corpus 3, the ratio was 85% correct. And the F1 of science and sports was 100%. With the lowest percentage as 71% for the label of Ent. 