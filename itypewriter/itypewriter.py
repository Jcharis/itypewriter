"""Character-A-A-Time-Print (caat print) is a simple package
designed to help printing or displaying text as one character at a time as if 
the system is typing.
"""

import time
import sys



# Function Based Prints
def itype(text: str, num_of_chars: int = 1, delay: float = 0.2):
    """
    itype (character-at-a-time): Stream object(s) supplied N character at a time.
    Params:
        text (str, any): Object.
        num_of_chars (int): Number of Characters to Print at a time
        delay: Delay between character printing
    Usage:
    >>> from itypewriter import itype
    >>> docx = "Some text to print out"
    >>> itype(docx)
    ....
    """
    text = "".join((text, "\n"))
    for i in range(0,len(text), num_of_chars):
        sys.stdout.write(text[i : i + num_of_chars])
        sys.stdout.flush()
        time.sleep(delay)


def iprint(text: str, num_of_chars: int = 1, delay=0.2):
    """
        iprint (character-at-a-time): Print object(s) supplied N character at a time.
    Params:
        text (str, any): Object.
        num_of_chars (int): Number of Characters to Print at a time
        delay: Delay between character printing
    Usage:
    >>> from itypewriter import iprint
    >>> docx = "Some text to print out"
    >>> iprint(docx)
    ....
    """
    text = "".join((text, "\n"))
    for i in range(0, len(text), num_of_chars):
        print(text[i : i + num_of_chars], end="", flush=True)
        time.sleep(delay)


def caat(text: str, num_of_chars: int = 1, delay: float = 0.2):
    """
    caat(character-at-a-time): Print object(s) supplied N character at a time.
    For more advanced features, see the :class:`~rich.console.Console` class.
    Params:
        text (str, any): Object.
        num_of_chars (int): Number of Characters to Print at a time
        delay: Delay between character printing
    Usage:
    >>> from itypewriter import caat
    >>> docx = "Some text to print out"
    >>> caat(docx)
    ....
    """
    text = "".join((text, "\n"))
    for i in range(0, len(text), num_of_chars):
        print(text[i : i + num_of_chars], end="", flush=True)
        time.sleep(delay)  # delay for 0.2 seconds


def type_text(text: str, num_of_chars: int = 1, delay: float = 0.2):
    """
        type_text(type one character-at-a-time): Print object(s) supplied N character at a time.
    For more advanced features, see the :class:`~rich.console.Console` class.
    Params:
        text (str, any): Object.
        num_of_chars (int): Number of Characters to Print at a time
        delay: Delay between character printing
    Usage:
    >>> from itypewriter import type_text
    >>> docx = "Some text to print out"
    >>> type_text(docx)
    ....
    """
    text = "".join((text, "\n"))
    for i in range(0, len(text), num_of_chars):
        print(text[i : i + num_of_chars], end="", flush=True)
        time.sleep(delay)  # delay for 0.2 seconds


class TypeText(object):
    """docstring for TypeText
    Usage:
    >>> from itypewriter import TypeText
    >>> text = "Hello world"
    >>> cp = TypeText(text)
    >>> cp.printc()
    """

    def __init__(self, text: str = None, num_of_chars: int = 1, delay: float = 0.2):
        super(TypeText, self).__init__()
        self.text = text
        self.num_of_chars = num_of_chars
        self.delay = delay

    def iprint(self):
        text = "".join((self.text, "\n"))  # add new line
        for i in range(0, len(text), self.num_of_chars):
            print(text[i : i + self.num_of_chars], end="", flush=True)
            time.sleep(self.delay)

    def itype(self):
        text = "".join((self.text, "\n")) 
        for c in text:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(self.delay)

    def __repr__(self) -> str:
        return "TypeText(text='{}',num_of_chars={},delay={})".format(self.text,self.num_of_chars,self.delay)


