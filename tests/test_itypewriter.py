from itypewriter import __version__
from itypewriter import TypeText
from itypewriter import iprint


import io
import sys


def test_version():
    assert __version__ == '0.0.1'


def test_type_text_class():
    output = io.StringIO()
    sys.stdout = output

    cp = TypeText("Hello, World!", num_of_chars=3, delay=1)
    cp.iprint()

    sys.stdout = sys.__stdout__
    assert output.getvalue() == "Hello, World!\n"


def test_stream_print():
    output = io.StringIO()
    sys.stdout = output

    cp = TypeText("Hello, World!", delay=1)
    cp.itype()

    sys.stdout = sys.__stdout__
    assert output.getvalue() == "Hello, World!\n"


def test_iprint():
    output = io.StringIO()
    sys.stdout = output

    cp = iprint("Hello, World!", delay=1)
   
    sys.stdout = sys.__stdout__
    assert output.getvalue() == "Hello, World!\n"