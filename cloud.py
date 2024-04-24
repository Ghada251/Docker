import warnings
warnings.filterwarnings('ignore')
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('stopwords')
nltk.download('punkt')
with open("paragraphs.txt", "r") as f:
    content=f.read()
content
type(content)
print("The Stop Words Are:\n")
print(stopwords.words('english'))
stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(content)

filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

filtered_sentence = []

for w in word_tokens:
	if w not in stop_words:
		filtered_sentence.append(w)
        
print("The Original Data Is\n")
print(word_tokens[0:100])
print("\n\n And The Filtered Data Is\n")
print(filtered_sentence[0:100])
print("The Frequency Of Each Word In The Processed Text.\n\n")
freqTable = {}
for word in filtered_sentence:
    word = word.lower()
    if word in stop_words:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1


# Display word frequency count
for word, freq in freqTable.items():
    print(f"{word}: {freq}")
