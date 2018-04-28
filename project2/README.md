# NLP 2018 Final Project 

I want to create a very simple sentiment analyzer. I learned about sentiment analysis during a hackathon this past summer and I have been fascinated ever since. I think it’s really important because it allows people to easily classify how well liked the document is. 
A basic sentiment analyzer has the following parts: 
Adding POS-tagging 
Adding a different “semantic level” 
Heuristics function at the end. 

Through this project, I would like to implement a POS-tagger where the POS-taggers are learned through training. This is part one for sentiment analysis. Then I would add a different semantic level. This “different semantic level” is a different type of tagger which includes “positive”, “negative”, etc. Creating the project with only positive and negative (along with some other basic tags) has been done before and I would like to add other emotions like sad and happy. The results would then be compared to other basic sentiment analysis tools on the web using the standard precision, recall, accuracy and f1 scores. 

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