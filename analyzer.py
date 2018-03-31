import nltk

class Analyzer():
    """Implements sentiment analysis."""
    pset = set()
    nset = set()
    pos =0
    neg = 0
    neu =0
    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        file_p = open(positives , "r")
        file_n = open(negatives , "r")
        i=0
        for line in file_p :
            i+=1
            if i>=36:
                self.pset.add(line.rstrip('\n'))
        i=0
        for line in file_n :
            i+=1
            if i>=36:
                self.nset.add(line.rstrip('\n'))
              
    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        posi =0
        negi = 0
        neu =0
        
        for i in tokens:
            i = i.lower()
            if i in self.pset:
                posi+=1
                self.pos +=1
            elif i in self.nset:
                negi+=1
                self.neg+=1
            else:
                self.neu+=1
                
        return posi - negi
        
