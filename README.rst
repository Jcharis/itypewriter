iTypeWriter
~~~~~~~~~~~

-  A simple package for printing and displaying characters one at a time
   as if you were typing.
-  With ``itypewriter`` you can display values as if you were typing a
   text.

Installation
^^^^^^^^^^^^

.. code:: bash

   pip install itypewriter

Usage
^^^^^

``itypewriter`` can be used either via the functional approach or via
the object oriented approach.

Via Functional Approach
'''''''''''''''''''''''

.. code:: python

   >>> import itypewriter
   >>> itypewriter.itype("Hello Sentient Typing")

There is also the ``iprint`` option

.. code:: python

   >>> from itypewriter import iprint
   >>> iprint("Hello Sentient Typing")

   >>> iprint("Hello",num_of_chars=3)

Each of these functions accepts optional params for customising the
number of characters (``num_of_chars``) and the delay inbetween the
appearance of characters (``delay``).

Specifying the Delay Time
'''''''''''''''''''''''''

.. code:: python

   >>> from itypewriter import iprint
   >>> iprint("Hello Sentient Typing",delay=0.2)

OOP Approach
^^^^^^^^^^^^

.. code:: python

   >>> from itypewriter import TypeText
   >>> docx = """Some wonderful text"""
   >>> tt = TypeText(docx,num_of_chars=1)
   >>> tt.iprint()
