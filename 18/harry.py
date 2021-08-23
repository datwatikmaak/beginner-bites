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
    text = f.read().lower().split()

special_words = [special_word
                 for special_word in text
                 if "\'" in special_word]

# print(special_words)


def get_harry_most_common_word():

    list_of_words = [word
                     for word in text
                     if word not in stop_words
                     and word not in special_words
                     and word.isalpha()]
    # print(list_of_words)

    most_common_word = Counter(list_of_words).most_common(1)[0]

    print(most_common_word)


get_harry_most_common_word()
