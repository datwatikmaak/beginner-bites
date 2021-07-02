import re
import urllib.parse


def generate_affiliation_link(url):
    url = url
    parsed = urllib.parse.urlparse(url)
    scheme = "http://"
    netloc = "www.amazon.com"

    entries = re.split("/+", url)
    params = entries[3]
    slug = entries[4]

    query = "?tag=pyb0f-20"

    affil_link = f"{scheme}{netloc}/{params}/{slug}/{query}"

    return affil_link


generate_affiliation_link('https://www.amazon.com/War-Art-Through-Creative-Battles/dp/1936891026/'
                          '?keywords=war+of+art')
