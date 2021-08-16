"""A palindrome is a word, phrase, number, or other sequence of characters
which reads the same backward as forward"""
import os
import urllib.request

tmp = os.getenv("TMP", "/tmp")
DICTIONARY = os.path.join(tmp, 'dictionary_m_words.txt')
urllib.request.urlretrieve('http://bit.ly/2Cbj6zn', DICTIONARY)


def load_dictionary():
    """Load dictionary (sample) and return as generator (done)"""
    with open(DICTIONARY) as f:
        return (word.lower().strip() for word in f.readlines())


def is_palindrome(word):
    """Return if word is palindrome, 'madam' would be one.
       Case insensitive, so Madam is valid too.
       It should work for phrases too so strip all but alphanumeric chars.
       So "No 'x' in 'Nixon'" should pass (see tests for more)"""

    # strip out all non alpha chars from lowercase word
    delchars = ''.join(char for char in word.lower() if char.isalnum())

    # write the word backwards
    reverse_word = delchars[::-1]

    # return True if delchars == reverse_word
    return delchars == reverse_word


def get_longest_palindrome(words=None):
    """Given a list of words return the longest palindrome
       If called without argument use the load_dictionary helper
       to populate the words list"""

    count = 0
    longest_palindrome = ""

    if words is None:
        words = load_dictionary()

    for word in words:
        if is_palindrome(word) and len(word) > count:
            count = len(word)
            longest_palindrome = word

    return longest_palindrome
