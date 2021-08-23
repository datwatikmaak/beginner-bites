import os
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
    text = f.read().lower().split()
    # print(text)


def get_harry_most_common_word():

    no_stop_words = [word for word in text if word not in stop_words]

    isalnum_chars = [char for char in no_stop_words if char.isalnum()]

    # counter = Counter(isalnum_chars).most_common()[0]
    most_common_word = Counter(isalnum_chars).most_common()[0][0]
    frequency = Counter(isalnum_chars).most_common()[0][1]
    print(most_common_word, frequency)


get_harry_most_common_word()
