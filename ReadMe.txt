Name: Krishna Sreenivas
Student ID: 800984436

ReadMe file:

Performance:
------------

Laplace Unigram Language Model: 
correct: 52 total: 471 accuracy: 0.110403
Laplace Bigram Language Model: 
correct: 61 total: 471 accuracy: 0.129512

Difficulties faced:
-------------------

1) Dealing with errors when keys didn't exists in dictionaries.
2) To calculate bigram accuracy, unigram counts of the first word in the bigram had to be calculated.
3) Apart from these, trivial coding errors were encountered, which were handled.

Decription of Custom model:
---------------------------

Chose to implement Laplace Bigram Language Model as my Custom model. 
Used two dictionaries to store the counts of unigram and bigrams.
Scored each sentence based on Laplace bigram model and summed them up to calculate the final accuracy score.

