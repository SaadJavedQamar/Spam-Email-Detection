import nltk
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize
text = "Hello there. How are you doing today? I hope everything is well."
sentences = sent_tokenize(text)
print(sentences)
