import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords

sentence = "what is the capital of United States"
tokens = word_tokenize(sentence)
stop_words = set(stopwords.words('english'))
clean_tokens = [w for w in tokens if not w in stop_words]
#tagged = nltk.pos_tag(clean_tokens)
#print(nltk.ne_chunk(tagged))
print(tokens)
print(clean_tokens)