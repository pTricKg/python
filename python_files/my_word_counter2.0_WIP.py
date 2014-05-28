Python 3.4.0 (default, Apr 11 2014, 13:05:18) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 13, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 4, in lwr_py
    lst = [python_files/from_py_2_class]
NameError: name 'python_files' is not defined
>>> open(python_files)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    open(python_files)
NameError: name 'python_files' is not defined
>>> opn = open(~python/python_files)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    opn = open(~python/python_files)
NameError: name 'python' is not defined
>>> ls
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    ls
NameError: name 'ls' is not defined
>>> open(python/)
SyntaxError: invalid syntax
>>> open(python)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    open(python)
NameError: name 'python' is not defined
>>> opn = open(os.path.python)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    opn = open(os.path.python)
NameError: name 'os' is not defined
>>> os.path.python
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.path.python
NameError: name 'os' is not defined
>>> opn = open(os.path.dirname(python))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    opn = open(os.path.dirname(python))
NameError: name 'os' is not defined
>>> import os.path
>>> os.path.dirname(python)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    os.path.dirname(python)
NameError: name 'python' is not defined
>>> os.path.dirname(path)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    os.path.dirname(path)
NameError: name 'path' is not defined
>>> os.path
<module 'posixpath' from '/usr/lib/python3.4/posixpath.py'>
>>> os.path.dirname
<function dirname at 0xb71c3c44>
>>> os.path.dirname(p)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    os.path.dirname(p)
NameError: name 'p' is not defined
>>> os.path.dirname(home/ptrickg/python)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    os.path.dirname(home/ptrickg/python)
NameError: name 'home' is not defined
>>> os.path.dirname('python')
''
>>> os.path.dirname('home')
''
>>> os.path.dirname('~home')
''
>>> os.path.dirname('home/ptrickg/python')
'home/ptrickg'
>>> opn = open(os.path.dirname('home/ptrickg/python/python_files')






	   
KeyboardInterrupt
>>> print(opn)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(opn)
NameError: name 'opn' is not defined
>>> os.path.dirname('HOME')
''
>>> os.path.dirname(pwd)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    os.path.dirname(pwd)
NameError: name 'pwd' is not defined
>>> os.path.dirname('pwd')
''
>>> pwd
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    pwd
NameError: name 'pwd' is not defined
>>> pwd()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    pwd()
NameError: name 'pwd' is not defined
>>> import fileinput
>>> for line in fileinput.input():
	process(line)

	

















Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    for line in fileinput.input():
  File "/usr/lib/python3.4/fileinput.py", line 263, in __next__
    line = self.readline()
  File "/usr/lib/python3.4/fileinput.py", line 360, in readline
    self._buffer = self._file.readlines(self._bufsize)
  File "/usr/lib/python3.4/idlelib/PyShell.py", line 1384, in readline
    line = self._line_buffer or self.shell.readline()
TypeError: 'int' object is not callable
>>> help()

Welcome to Python 3.4!  This is the interactive help utility.

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at http://docs.python.org/3.4/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> argv
no Python documentation found for 'argv'

help> argv()
no Python documentation found for 'argv()'

help> 'argv'
no Python documentation found for 'argv'

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> for line in fileinput.input(/home/ptrickg/python)
SyntaxError: invalid syntax
>>> for line in fileinput.input('home/ptrickg/python')
SyntaxError: invalid syntax
>>> for line in fileinput.input('home/ptrickg/python'):
	process(line)
	print(line)

	
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    for line in fileinput.input('home/ptrickg/python'):
  File "/usr/lib/python3.4/fileinput.py", line 101, in input
    raise RuntimeError("input() already active")
RuntimeError: input() already active
>>> fileinput.close()
>>> fileinput.input('home/ptrickg/python/python_files')
<fileinput.FileInput object at 0xb54e9b2c>
>>> fileinput.close()
>>> os.open('home/ptrickg/python/python_files')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    os.open('home/ptrickg/python/python_files')
TypeError: Required argument 'flags' (pos 2) not found
>>> os.open('home/ptrickg/python/python_files',r)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    os.open('home/ptrickg/python/python_files',r)
NameError: name 'r' is not defined
>>> os.open('home/ptrickg/python/python_files',)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    os.open('home/ptrickg/python/python_files',)
TypeError: Required argument 'flags' (pos 2) not found
>>> os.open('home/ptrickg/python/python_files','r')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    os.open('home/ptrickg/python/python_files','r')
TypeError: an integer is required (got type str)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 17, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 6, in lwr_py
    opn = open('home/ptrickg/python/python_files' , 'rw')
ValueError: must have exactly one of create/read/write/append mode
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 17, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 6, in lwr_py
    opn = open('home/ptrickg/python/python_files' , 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'home/ptrickg/python/python_files'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 17, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 6, in lwr_py
    opn = open('~home/ptrickg/python/python_files' , 'r')
FileNotFoundError: [Errno 2] No such file or directory: '~home/ptrickg/python/python_files'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 17, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 6, in lwr_py
    opn = open('/home/ptrickg/python/python_files' , 'r')
IsADirectoryError: [Errno 21] Is a directory: '/home/ptrickg/python/python_files'
>>> os.getcwd()
'/home/ptrickg/python'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 17, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 6, in lwr_py
    opn = open('/python_files' , 'r')
FileNotFoundError: [Errno 2] No such file or directory: '/python_files'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 17, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 6, in lwr_py
    opn = open('/python_files' , 'r')
FileNotFoundError: [Errno 2] No such file or directory: '/python_files'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 17, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 6, in lwr_py
    opn = open('/home/ptrickg/python/python_files' , 'r')
IsADirectoryError: [Errno 21] Is a directory: '/home/ptrickg/python/python_files'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 17, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 6, in lwr_py
    opn = os.open('/home/ptrickg/python/python_files' , 'r')
TypeError: an integer is required (got type str)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 17, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 7, in lwr_py
    rd = opn.read()
AttributeError: 'str' object has no attribute 'read'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 18, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 7, in lwr_py
    opnf= os.open(opn)
TypeError: Required argument 'flags' (pos 2) not found
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 18, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 7, in lwr_py
    opnf= os.open(opn,'r')
TypeError: an integer is required (got type str)
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 18, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 7, in lwr_py
    opnf= open(opn,'r')
IsADirectoryError: [Errno 21] Is a directory: '/home/ptrickg/python'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 18, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 7, in lwr_py
    opnf= open(opn,'r')
FileNotFoundError: [Errno 2] No such file or directory: '/home/ptrickg/python/python_files/*'
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python/python_files/animal_hangman.py
#!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 18, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 7, in lwr_py
    opnf= open(opn,'r')
FileNotFoundError: [Errno 2] No such file or directory: '/home/ptrickg/python/python_files/*.py'
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python/python_files/animal_hangman.py
#!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
#!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python/python_files/animal_hangman.py
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python/python_files/animal_hangman.py
 Following is the Program  #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


     #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


 #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


 
 #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


 #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


 #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 30, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 8, in lwr_py
    for files in python_files:
TypeError: 'NoneType' object is not iterable
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 30, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 8, in lwr_py
    for files in python_files:
TypeError: 'NoneType' object is not iterable
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 30, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 8, in lwr_py
    for files in python_files:
TypeError: 'NoneType' object is not iterable
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 29, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 9, in lwr_py
    opnf= open(opn,'r')
TypeError: invalid file: (None, '*.py')
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 29, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 9, in lwr_py
    opnf= open(opn,'r')
FileNotFoundError: [Errno 2] No such file or directory: '*.py'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 29, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 9, in lwr_py
    opnf= open(opn,'r')
FileNotFoundError: [Errno 2] No such file or directory: '"".py'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 29, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 9, in lwr_py
    opnf= open(opn,'r')
FileNotFoundError: [Errno 2] No such file or directory: 'None.py'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 29, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 9, in lwr_py
    opnf= open(opn,'r')
FileNotFoundError: [Errno 2] No such file or directory: '.py'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 29, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 9, in lwr_py
    opnf= open(opn,'r')
TypeError: invalid file: None
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 29, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 9, in lwr_py
    opnf= open(python_files,'r')
TypeError: invalid file: None
>>> ================================ RESTART ================================
>>> 
None
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


 #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
None
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


 #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


 #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 33, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 8, in lwr_py
    python_files = chdir("~/python_files")
NameError: name 'chdir' is not defined
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 33, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 8, in lwr_py
    python_files = os.chdir("~/python_files")
FileNotFoundError: [Errno 2] No such file or directory: '~/python_files'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 33, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 8, in lwr_py
    python_files = os.chdir("/python_files")
FileNotFoundError: [Errno 2] No such file or directory: '/python_files'
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python
None
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


 #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 33, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 8, in lwr_py
    python_files = os.chdir("HOME/python_files")
FileNotFoundError: [Errno 2] No such file or directory: 'HOME/python_files'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 33, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 8, in lwr_py
    python_files = os.chdir("~python_files")
FileNotFoundError: [Errno 2] No such file or directory: '~python_files'
>>> ================================ RESTART ================================
>>> 
Traceback (most recent call last):
  File "/home/ptrickg/python/lowercase_my_py.py", line 33, in <module>
    lwr_py()
  File "/home/ptrickg/python/lowercase_my_py.py", line 8, in lwr_py
    python_files = os.chdir("home/ptrickg/python/python_files")
FileNotFoundError: [Errno 2] No such file or directory: 'home/ptrickg/python/python_files'
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python
None
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


 #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
/home/ptrickg/python
/home/ptrickg/python/python_files
/home/ptrickg/python/python_files/animal_hangman.py



    Following is the Program


 #!/usr/bin/env python

import random
import urllib

print 'time to play hangman'
animals = urllib.urlopen('http://davidbau.com/data/animals').read().split()
secret = random.choice(animals)
guesses = 'aeiou'
turns = 5

while turns > 0:
  missed = 0
  for letter in secret:
    if letter in guesses:
      print letter,
    else:
      print '_',
      missed += 1

  print

  if missed == 0:
    print 'You win!'
    break

  guess = raw_input('guess a letter: ')
  guesses += guess

  if guess not in secret:
    turns -= 1
    print 'Nope.'
    print turns, 'more turns'
    if turns < 5: print '   O   '
    if turns < 4: print ' \_|_/ '
    if turns < 3: print '   |   '
    if turns < 2: print '  / \  '
    if turns < 1: print ' d   b '
    if turns == 0:
      print 'The answer is', secret
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/lowercase_my_py.py
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 27, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 6, in my_counter
    file_open = os.chdir(name)
NameError: name 'os' is not defined
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/lowercase_my_py.py
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 28, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 7, in my_counter
    file_open = os.chdir(name)
NotADirectoryError: [Errno 20] Not a directory: '/home/ptrickg/python/lowercase_my_py.py'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 28, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 7, in my_counter
    file_open = os.chdir(name)
NotADirectoryError: [Errno 20] Not a directory: '/home/ptrickg/python/python_files/animal_hangman.py'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 28, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 7, in my_counter
    file_open = os.chdir(name)
NotADirectoryError: [Errno 20] Not a directory: '/home/ptrickg/python/python_files/animal_hangman.py'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 30, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 7, in my_counter
    file_open = os.chdir(name)
NotADirectoryError: [Errno 20] Not a directory: '/home/ptrickg/python/python_files/animal_hangman.py'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.p
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 30, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 7, in my_counter
    file_open = os.chdir(str(name))
FileNotFoundError: [Errno 2] No such file or directory: '/home/ptrickg/python/python_files/animal_hangman.p'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 30, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 7, in my_counter
    file_open = os.chdir(str(name))
NotADirectoryError: [Errno 20] Not a directory: '/home/ptrickg/python/python_files/animal_hangman.py'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.p
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 31, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 7, in my_counter
    file_open = os.chdir(name)
FileNotFoundError: [Errno 2] No such file or directory: '/home/ptrickg/python/python_files/animal_hangman.p'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 31, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 7, in my_counter
    file_open = os.chdir(name)
NotADirectoryError: [Errno 20] Not a directory: '/home/ptrickg/python/python_files/animal_hangman.py'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 35, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 5, in my_counter
    file_open = os.chdir(name)
NotADirectoryError: [Errno 20] Not a directory: '/home/ptrickg/python/python_files/animal_hangman.py'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 35, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 5, in my_counter
    file_open = os.chdir(name)
NotADirectoryError: [Errno 20] Not a directory: '/home/ptrickg/python/python_files/animal_hangman.py'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
/home/ptrickg/python/python_files/animal_hangman.py
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
/home/ptrickg/python/python_files/animal_hangman.py
There are 129 words in this document.
Would you like to count more?:no
Good Bye
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: animal_hangman.py
animal_hangman.py
There are 129 words in this document.
Would you like to count more?:no
Good Bye
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
/home/ptrickg/python/python_files
/home/ptrickg/python/python_files/animal_hangman.py
There are 129 words in this document.
Would you like to count more?:no
Good Bye
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
/home/ptrickg/python/python_files
213.doc
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 38, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 21, in my_counter
    handle = open(name, 'r')
FileNotFoundError: [Errno 2] No such file or directory: '213.doc'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
/home/ptrickg/python/python_files
/home/ptrickg/python/python_files/animal_hangman.py
There are 129 words in this document.
Would you like to count more?:no
Good Bye
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: /home/ptrickg/python/python_files/animal_hangman.py
/home/ptrickg/python/python_files
/home/ptrickg/python/python_files/animal_hangman.py
There are 129 words in this document.
Would you like to count more?:213.doc
Good Bye
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
/home/ptrickg/python/python_files
213.doc
/home/ptrickg/python/python_files
Something isn't right.  Please start again
Enter file or path to file: 
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
/home/ptrickg/python/python_files
213.doc
/home/ptrickg/python/python_files
Something isn't right.  Please start again
Enter file or path to file: 
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
/home/ptrickg/python/python_files
213.doc
/home/ptrickg/python/python_files
Something isn't right.  Please start again
Enter file or path to file: 
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
/home/ptrickg/python/python_files
213.doc is your input
/home/ptrickg/python/python_files
Something isn't right.  Please start again
Enter file or path to file: 
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
You are here /home/ptrickg/python/python_files
213.doc is your input
/home/ptrickg/python/python_files
Something isn't right.  Please start again
Enter file or path to file: 
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
You are here: /home/ptrickg/python/python_files
213.doc is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
Something isn't right.  Please start again
Enter file or path to file: 
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
You are here: /home/ptrickg/python/python_files
213.doc is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 47, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 22, in my_counter
    file_open)
TypeError: input expected at most 1 arguments, got 2
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
You are here: /home/ptrickg/python/python_files
213.doc is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
You must clarify where your file is./home/ptrickg/Documents
/home/ptrickg/Documents
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 46, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 23, in my_counter
    opn = open(file_open, 'r')
IsADirectoryError: [Errno 21] Is a directory: '/home/ptrickg/python/python_files'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
You are here: /home/ptrickg/python/python_files
213.doc is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
You must clarify where your file is./home/ptrickg/Documents
/home/ptrickg/Documents
None
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 48, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 25, in my_counter
    opn = open(file_open, 'r')
IsADirectoryError: [Errno 21] Is a directory: '/home/ptrickg/python/python_files'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
You are here: /home/ptrickg/python/python_files
213.doc is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
You must clarify where your file is./home/ptrickg/Documents
/home/ptrickg/Documents
None
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 49, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 26, in my_counter
    opn = open(file_open, 'r')
TypeError: invalid file: None
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
You are here: /home/ptrickg/python/python_files
213.doc is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
You must clarify where your file is./home/ptrickg/Documents
/home/ptrickg/Documents
None
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 49, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 26, in my_counter
    opn = open(file_open + name, 'r')
TypeError: unsupported operand type(s) for +: 'NoneType' and 'str'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
You are here: /home/ptrickg/python/python_files
213.doc is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
You must clarify where your file is./home/ptrickg/Documents
/home/ptrickg/Documents
None
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 49, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 26, in my_counter
    opn = open(file_open + name, 'r')
FileNotFoundError: [Errno 2] No such file or directory: '/home/ptrickg/Documents213.doc'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 212.doc
You are here: /home/ptrickg/python/python_files
212.doc is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
You must clarify where your file is./home/ptrickg/Documents
/home/ptrickg/Documents
None
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 49, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 26, in my_counter
    opn = open(file_open + "/" + name, 'r')
FileNotFoundError: [Errno 2] No such file or directory: '/home/ptrickg/Documents/212.doc'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
You are here: /home/ptrickg/python/python_files
213.doc is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
You must clarify where your file is./home/ptrickg/Documents
/home/ptrickg/Documents
None
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 49, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 27, in my_counter
    text = handle.read()
UnboundLocalError: local variable 'handle' referenced before assignment
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.org
You are here: /home/ptrickg/python/python_files
213.org is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
You must clarify where your file is./home/ptrickg/Documents
/home/ptrickg/Documents
None
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 49, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 26, in my_counter
    handle = open(file_open.strip() + "/" + name, 'r')
FileNotFoundError: [Errno 2] No such file or directory: '/home/ptrickg/Documents/213.org'
>>> ================================ RESTART ================================
>>> 
Enter file or path to file: 213.doc
You are here: /home/ptrickg/python/python_files
213.doc is your input
Your file isn't located in this directory: /home/ptrickg/python/python_files
You must clarify where your file is./home/ptrickg/Documents
/home/ptrickg/Documents
None
Traceback (most recent call last):
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 49, in <module>
    my_counter()
  File "/home/ptrickg/python/python_files/my_word_counter.py", line 27, in my_counter
    text = handle.read()
  File "/usr/lib/python3.4/codecs.py", line 313, in decode
    (result, consumed) = self._buffer_decode(data, self.errors, final)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xd0 in position 0: invalid continuation byte
>>> 
