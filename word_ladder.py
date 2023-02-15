#!/bin/python3

from collections import deque
import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    lists = []
    stack = []
    stack.append(start_word)
    word_queue = deque()
    word_queue.append(stack)
    if len(start_word) != len(end_word):
        return None
    if start_word == end_word:
        return [start_word]
    with open(dictionary_file, 'r') as x:
        for word in x.readlines():
            lists.append(word.strip('\n'))

    while len(word_queue) > 0:
        newstack = word_queue.popleft()
        for word in set(lists):
            if _adjacent(word, newstack[-1]):
                if word == end_word:
                    newstack.append(word)
                    return newstack
                newerstack = copy.deepcopy(newstack)
                newerstack.append(word)
                word_queue.append(newerstack)
                lists.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if not ladder:
        return False
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    if len(word1) != len(word2):
        return False
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False
