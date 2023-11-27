import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import nltk
import io
import unicodedata
import numpy as np
import re
import os
import string
from numpy import linalg
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import webtext
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

def twitter_sentiment_score():

    current_directory = os.path.dirname(__file__)

    text_file = 'twitt.txt'
    
    # Create the full path to the CSV file
    text_file_path = os.path.join(current_directory, text_file)

    with open(text_file_path, 'r') as f:
        text = f.read()
        
    sent_tokenizer = PunktSentenceTokenizer(text)
    sents = sent_tokenizer.tokenize(text)

    #print(word_tokenize(text))
    #print(sent_tokenize(text))

    porter_stemmer = PorterStemmer()

    nltk_tokens = nltk.word_tokenize(text)

    # for w in nltk_tokens:
    # 	print ("Actual: % s Stem: % s" % (w, porter_stemmer.stem(w)))
        

    wordnet_lemmatizer = WordNetLemmatizer()
    nltk_tokens = nltk.word_tokenize(text)

    #for w in nltk_tokens:
    #	print ("Actual: % s Lemma: % s" % (w, wordnet_lemmatizer.lemmatize(w)))
        
    text = nltk.word_tokenize(text)
    #print(nltk.pos_tag(text))

    sid = SentimentIntensityAnalyzer() 
    tokenizer = nltk.data.load('tokenizers\punkt\english.pickle')


    overall_scores = {"neg": 0, "neu": 0, "pos": 0}
    with open(text_file_path,'r') as f:
        for text in f.read().split('\n'):
            #print(text)
            scores = sid.polarity_scores(text)
            del scores["compound"]
            for key in sorted(scores):
                #print('{0}: {1}, '.format(key, scores[key]), end ='')
                overall_scores[key] += scores[key]

    print()		
    print("Overall Sentiment Scores:")
    for key in sorted(overall_scores):
        print('{0}: {1}'.format(key, overall_scores[key]))
        
    print()
    labels = list(overall_scores.keys())
    scores = list(overall_scores.values())

    plt.bar(labels, scores, color=['red', 'gray', 'green'])
    plt.title('Overall Sentiment Score Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Score')
    plt.show()

    return overall_scores
