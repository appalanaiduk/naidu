Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tuple=(6,"name",44,56)
>>> tuple(0)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    tuple(0)
TypeError: 'tuple' object is not callable
>>> tuple=(6,"name",44,56)
... tuple[0]
SyntaxError: multiple statements found while compiling a single statement
