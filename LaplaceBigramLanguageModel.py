#Name: Krishna Sreenivas
#Student ID: 800984436


import math
import nltk

class LaplaceBigramLanguageModel:

  def __init__(self, corpus):
    self.bigramCounts = {} #default dictionary to hold bigram counts
    self.total = 0
    self.unigramCounts= {} #default dictionary to hold unigram counts
    self.train(corpus)
    

  def train(self, corpus):
    """Takes a HolbrookCorpus corpus, does whatever training is needed."""
    for sentence in corpus.corpus:
      for word in sentence.data:
        self.unigramCounts.setdefault(word.word,0) #setting unigram dictionary to 0
        self.unigramCounts[word.word] = self.unigramCounts[word.word] + 1 #incrementing unigram count by 1
      for bigram in nltk.bigrams(str(sentence).split(" ")):
        self.bigramCounts.setdefault(bigram,0) #setting bigram dictionary to 0
        self.bigramCounts[bigram] = self.bigramCounts[bigram] + 1 #incrementing bigram count by 1
        self.total += 1

  def score(self, sentence):
    """Takes a list of strings, returns a score of that sentence."""
    score = 0.0 
    for bigram in nltk.bigrams(sentence):
      if self.bigramCounts.get(bigram)==None: #if bigram not present in dictionary count is 0
        score += math.log(0 + 1)
      elif self.bigramCounts.get(bigram)!=None: #if it is present count will be obtained from bigram dictionary
        count = self.bigramCounts[bigram]
        score += math.log(count + 1)
      elif self.unigramCounts.get(bigram[0])==None: #if unigram not present in the unigram dictionary count is 0
        score -= math.log(0 + len(self.bigramCounts))
      else: #if unigram is present
        score -= math.log(self.unigramCounts.get(bigram[0]) + len(self.bigramCounts)) 
    return score
