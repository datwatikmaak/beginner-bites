import re
from collections import Counter, namedtuple
import os
import urllib.request

# prep
tmp = os.getenv("TMP", "/tmp")
tempfile = os.path.join(tmp, 'dirnames')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/dirnames.txt',
    tempfile
)

IGNORE = 'static templates data pybites bbelderbos hobojoe1848'.split()

Stats = namedtuple('Stats', 'user challenge')


# code

def gen_files(tempfile=tempfile):
    """
    Parse the tempfile passed in, filtering out directory names
    (first column) using the last "is_dir" column.

    Lowercase these directory names and return them as a generator.

    "tempfile" has the following format:
    challenge<int>/file_or_dir<str>,is_dir<bool>

    For example:
    03/rss.xml,False
    03/tags.html,False
    03/Mridubhatnagar,True
    03/aleksandarknezevic,True

    => Here you would return 03/mridubhatnagar (lowercased!)
       followed by 03/aleksandarknezevic
    """
    with open(tempfile) as f:
        data = f.read()
        data = data.lower()

    challenges = [re.split(r'[/,]+', line)
                  for line in data.splitlines()]

    filtered_filenames = [challenge
                          for challenge in challenges
                          if challenge[-1] != "false"]

    return [
        f"{challenge[0].strip()}/{challenge[1].strip()}"
        for challenge in filtered_filenames
    ]


gen_files(tempfile=tempfile)


def diehard_pybites(files=None):
    """
    Return a Stats namedtuple (defined above) that contains:
    1. the user that made the most pull requests (ignoring the users in IGNORE), and
    2. a tuple of:
        ("most popular challenge id", "amount of pull requests for that challenge")

    Calling this function on the default dirnames.txt should return:

    Stats(user='clamytoe', challenge=('01', 7))
    """
    if files is None:
        files = gen_files()

    users = Counter()
    popular_challenges = Counter()

    # your code

    popular_challenges = []
    for challenge in files:
        challenge = re.split(r'[/]+', challenge)
        popular_challenges.append(challenge[0])

    usernames = []
    for username in files:
        username = re.split(r'[/]+', username)
        usernames.append(username[1])

    non_ignored_usernames = [item for item in usernames if item not in IGNORE]

    popular_challenges = Counter(popular_challenges).most_common(10)

    users = Counter(non_ignored_usernames).most_common(10)
    print(users[0][0])

    # Stats(user='clamytoe', challenge=('01', 7))
    # return Stats(stats, popular_challenges[0])
    print(Stats(users[0][0], popular_challenges[0]))


diehard_pybites(
        files=[
            "22/wonderfulboyx",
            "25/bbelderbos",  # ignored
            "25/clamytoe",
            "21/wonderfulboyx",
            "25/santiagobenitez",
            "23/santiagobenitez",
            "07/santiagobenitez"
        ])
