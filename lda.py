# Justin Smilan, Ben Drews, Joseph Oh

from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
import glob, os, codecs

# Global variables
docs = []
clean_list = []

def tokenize(doc):
    # Tokenize the document
    tokens_list = []
    for line in doc:
        tokens = line.split()
        tokens_list.append(tokens)
        print tokens
    return tokens_list
    

def removeStopWords(tokens_list):
    # List of English stop words
    stop_words = get_stop_words('en')
    # Remove stop words from doc
    for i, tokens in enumerate(tokens_list):
        tokens_list[i] = [x for x in tokens if x not in stop_words]
        print tokens_list[i]
    return tokens_list


def stem(tokens_list):
    # Stem the tokens in doc
    p_stemmer = PorterStemmer()
    for i, tokens in enumerate(tokens_list):
        tokens_list[i] = [p_stemmer.stem(i) for i in tokens]
        print tokens_list[i]
    return tokens_list


def clean(docs):
    # Clean each document
    for i, doc in enumerate(docs):
        tokens_list = tokenize(doc)
        stopped_tokens = removeStopWords(tokens_list)
        stemmed_tokens = stem(stopped_tokens)
        docs[i] = stemmed_tokens

    print docs


if __name__ == "__main__":
    # Gather all the lyric files
    docs = []
    for filename in glob.glob('lyrics/*'):
        doc = []
        with codecs.open(filename, 'r', encoding='utf-8') as lyrics:
            doc.append(lyrics.read())
            docs.append(doc)
            print doc
            break

    #clean(docs)
        
