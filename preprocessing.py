import nltk
import string


class Preprocessing:

    stemmer = nltk.stem.porter.PorterStemmer()
    punctuation_map = dict((ord(char), None) for char in string.punctuation)
    stopwords = nltk.corpus.stopwords.words("german")

    def process_text(self, text):
        tokens = [word for sent in nltk.sent_tokenize(text)
                  for word in nltk.word_tokenize(sent.lower().translate(self.punctuation_map))
                  if word not in self.stopwords]

        stems = [self.stemmer.stem(item) for item in tokens]
        return " ".join(stems)
