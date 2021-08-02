import nltk
# nltk.download('punckt')
# from nltk.stem.porter import PorterStemmer
import numpy as np
from nltk.stem.isri import ISRIStemmer
stemmer = ISRIStemmer()

#Here is the actual tokenization for the trained dataset using nltk
def tokenize(sentense):
    return nltk.tokenize.wordpunct_tokenize(sentense)
    #Stemming the words
def stem(word):
    return stemmer.stem(str(word).encode('utf-8').decode('utf-8'))
#Getting the bag of words 
def bag_of_words(tokenized_sentense, all_words):
    tokenized_sentense = [stem(word) for word in tokenized_sentense]
    bag  = np.zeros(len(all_words), dtype=np.float32)
    for index, word in enumerate(all_words):
        if word in tokenized_sentense:
            bag[index] = 1.0
    return bag
