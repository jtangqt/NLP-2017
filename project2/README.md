# NLP 2018 Final Project 

I want to create a very simple sentiment analyzer. I learned about sentiment analysis during a hackathon this past summer and I have been fascinated ever since. I think it’s really important because it allows people to easily classify how well liked the document is. 
A basic sentiment analyzer has the following parts: 
Adding POS-tagging 
Adding a different “semantic level” 
Heuristics function at the end. 

Through this project, I would like to implement a POS-tagger where the POS-taggers are learned through training. This is part one for sentiment analysis. Then I would add a different semantic level. This “different semantic level” is a different type of tagger which includes “positive”, “negative”, etc. Creating the project with only positive and negative (along with some other basic tags) has been done before and I would like to add other emotions like sad and happy. The results would then be compared to other basic sentiment analysis tools on the web using the standard precision, recall, accuracy and f1 scores. 

## How to Run
python jasmineqtang_senti.py 


## Some Quality Sentences
As for the spectacle of the battle and showdowns, while not at the scale of Lord of the Rings, I honestly cant think how it could have been done better as the film makers have intertwined heart stopping action with dramatic progressions in the narrative. Its actually more visceral and dynamic than the rather smaller scale battle of the brilliant novels (not to take anything away from Rowlings writing). Do I have any gripes? Yes I do. Although I applaud Steve Kloves for a difficult screenplay adaption...I think he could still have done better at explaining some odd anomalies that only readers of the book will understand. This might annoy you if you havent read the books. But its a small gripe because what we get is delightful. What an amazing achievement to faithfully bring Rowlings epic saga to the big screen with the same cast and largely the same crew, maintaining the brilliant quality right to the end.

This is quite possibly the worst movie ever made. Even my 4 year old hated it and wanted to leave. I was using it as an excuse to nap in air-conditioning. Alas, it was so bad that my daughter insisted we leave. Not really a surprise for a Steven Paul film, but Im saddened that Jon Voights career has fallen so low...and Scott Baio??? ARGH! Believe me, Ive had to sit through some bad kid flix, but this one is an all time loser. There is a woman with very large lips (Vanessa Angel) who almost makes it bearable, just for the pure fascination of watching whether or not they will explode. However, my suggestion would be that all prints of this film be sent to President Bush so he can see how harmful his education budget cuts have been.

The weather was bad.

The weather was not bad.

The weather was not good.  


The library was quiet today.

The library was too quiet today.


## Final Presentation: 
I would showcase the heuristics function which is affected by the number of categories of feelings that creates a good score. I would then run a few excerpts of the data through the program after allowing people to read through it and allow people to determine if the sentiment analysis project is accurate. 

Some training data for sentiment analysis (in consideration):
https://stackoverflow.com/questions/7551262/training-data-for-sentiment-analysis 

Data for part of speech tagging will come from here: 
https://stackoverflow.com/questions/25330079/where-can-i-get-training-data-of-part-of-speech-tagger

The dictionary for negative/positive words: https://www.quora.com/Is-there-a-downloadable-database-of-positive-and-negative-words 

Data for Sentiment Analysis training: 
https://stackoverflow.com/questions/7551262/training-data-for-sentiment-analysis 


Other resources I’ve found: 
http://fjavieralba.com/basic-sentiment-analysis-with-python.html -- shows a tutorial of a very rudimentary sentimental analysis program
http://www.nltk.org/book/ch05.html -- shows more information about POS-tagging
http://nlpforhackers.io/training-pos-tagger/ -- more POS-tagging info
http://www.nltk.org/howto/wsd.html
http://www.nltk.org/howto/wordnet.html
https://web.stanford.edu/~jurafsky/slp3/18.pdf
https://github.com/kevincobain2000/sentiment_classifier/blob/master/src/senti_classifier/senti_classifier.py
http://text-processing.com/docs/sentiment.html
http://swat.cse.lehigh.edu/pubs/zhang10a.pdf
https://framenet.icsi.berkeley.edu/fndrupal/WhatIsFrameNet
https://www.nltk.org/book/ch05.html
https://www.cse.iitb.ac.in/~pb/papers/lrec16-slangnet.pdf

