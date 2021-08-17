import os
import re
from collections import Counter
import urllib.request
import xml.etree.ElementTree as ET

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'feed')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/feed',
    tempfile
)

with open(tempfile) as f:
    content = f.read().lower()


def get_pybites_top_tags(n=10):
    """use Counter to get the top 10 PyBites tags from the feed
       data already loaded into the content variable"""

    # find all the categories with regex
    categories = (re.findall("<category>(.*?)</category>", content))

    # count the number of occurence of each category
    top_tags = Counter(categories)

    # return the n most common tags
    return top_tags.most_common(n)
