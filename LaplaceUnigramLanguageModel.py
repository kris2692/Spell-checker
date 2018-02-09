#Name: Krishna Sreenivas
#Student ID: 800984436


import math
class LaplaceUnigramLanguageModel:

  def __init__(self, corpus):
    self.unigramCounts = {} #to store unigram count values
    self.total = 0
    self.train(corpus)

  def train(self, corpus):
    """Takes a HolbrookCorpus corpus, does whatever training is needed."""
    for sentence in corpus.corpus:
      for word in sentence.data:  
        self.unigramCounts.setdefault(word.word,0) #setting dictionary to 0
        self.unigramCounts[word.word] = self.unigramCounts[word.word] + 1 #incrementing unigram count by 1
        self.total += 1
  
  def score(self, sentence):
    """Takes a list of strings, returns a score of that sentence."""
    score = 0.0 
    for word in sentence:
      if word not in self.unigramCounts: #if word not present in unigram dictionary
        score += math.log(1)
      else: #if word is present in unigram dictionary
        count = self.unigramCounts[word]
        score += math.log(count + 1)
      score -= math.log(self.total + len(self.unigramCounts)) #calculating final score
    return score
