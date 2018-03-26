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

## ML Method 
The method used is Naive Bayes

## Tokenizer 
Porter Stemmer tokenizer

## Weighting Scheme 


## Smoothing 
Laplacian Smoothing

## Optional Parameters


## Performance for Second and Third Data Set
The training set for corpus 2 and corpus 3 were split to about 75% for the training set and 25% for the test set. The code in create_cv.py takes the training sets, randomizes the order, and creates a new training set, test set list and test set. 
With the new sets generated locally by create_cv.py, corpus 2 had an 80.9% ratio of correct. The F1 of I was 0.74 while the F1 of O was 0.85. As for corpus 3, the ratio was 85% correct. And the F1 of science and sports was 100%. With the lowest percentage as 71% for the label of Ent. 