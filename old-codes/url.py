#!/usr/bin/env python3
'http://sixty-north.com/c/t.txt'

import sys

from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list of words from URL.
    ARGS:
        URL: the url of a UTF-8 text document
    Returns:
        A list of words from the url"""
    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                story_words.append(word)
    return story_words


def print_words(items):

    for item in items:
        print("hello world!")
        print(item, end=' ')
        


def main():
    url = sys.argv[1]
    words = fetch_words(url)
    print_words(words)

   
if __name__ == '__main__':
    main()
