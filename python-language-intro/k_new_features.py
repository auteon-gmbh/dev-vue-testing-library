"""
New Features 3.8

https://docs.python.org/3/whatsnew/3.8.html
https://docs.python.org/3/whatsnew/3.9.html
"""

import re
from typing import List

lorem_ipsum = '''Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
                industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type 
                and scrambled it to make a type specimen book. It has survived not only five centuries, but also the 
                leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s 
                with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop 
                publishing software like Aldus PageMaker including versions of Lorem Ipsum.'''


def basic(text: str) -> List[str]:
    matches = re.findall('Ipsum', text)

    if matches:
        # do something here
        pass

    return matches


def assign_expr(text: str) -> List[str]:
    """
    # Assignment expressions
    # https://www.python.org/dev/peps/pep-0572/

    Demo of assignment expressions by matching the input text to a regex
    and returning the matches.

    :param str text: input text to check matches against
    :return: list of string matches
    :rtype: List[str]
    """

    if matches := re.findall('Ipsum', text):
        # do something here
        pass

    return matches


if __name__ == '__main__':
    print(assign_expr(lorem_ipsum))
