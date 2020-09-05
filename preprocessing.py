import nltk
import string


class Preprocessing:

    stemmer = nltk.stem.porter.PorterStemmer()
    punctuation_map = dict((ord(char), None) for char in string.punctuation)
    stopwords = nltk.corpus.stopwords.words("german")

    def tokenize(self, text):
        return [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]

    def stem_tokens(self, tokens):
        return [self.stemmer.stem(item) for item in tokens]

    def normalize(self, text):
        return self.stem_tokens(nltk.word_tokenize(text.lower().translate(self.punctuation_map)))

    def remove_stop_word(self, tokens):
        return [word for word in tokens if word not in self.stopwords]
