import os
import re
import urllib.request
import string
from collections import Counter

# data provided
tmp = os.getenv("TMP", "/tmp")
stopwords_file = os.path.join(tmp, 'stopwords')
harry_text = os.path.join(tmp, 'harry')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/stopwords.txt',
    stopwords_file
)
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/harry.txt',
    harry_text
)

with open(stopwords_file) as f:
    stop_words = f.read().lower().split()
    # print(stop_words)

with open(harry_text, 'r', encoding='utf-8') as f:
    text = f.read().lower()
    words = re.split(r'\W+', text)
    print(words[:100])


def get_harry_most_common_word():

    non_stop_words = [word for word in words if word not in stop_words and len(word) > 6 and word.startswith("du")]
    print(non_stop_words)

    most_common_word = Counter(non_stop_words).most_common()[0]
    frequency = Counter(non_stop_words).most_common()[1]

    print(most_common_word, frequency)


get_harry_most_common_word()
