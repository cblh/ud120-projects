import pickle

### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl"
authors_file = "../text_learning/your_email_authors.pkl"

word_data = pickle.load( open(words_file, "r"))

### in Part 4, do TfIdf vectorization here
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer(stop_words="english")
vectorizer.fit_transform(word_data)
feature_words = vectorizer.get_feature_names()
print "number of words:", len(feature_words)
print "word number 34597:", feature_words[34597]
