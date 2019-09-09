#!/usr/bin/env python

"""This is an example of word wrap to fix the text overflow issues. """
import textwrap

agenda = (' -read', ' -write', ' -work on our grammar', ' -and play a game')
#a = agenda.splitlines()
new_agenda = []
for x in range(len(agenda)):
    wrapper = textwrap.fill(agenda [x], 6)
    w2 = '\n'.join(wrapper.split('\n'))
    new_agenda.append(w2)
a = '\n'.join(new_agenda)
#a = tuple(agenda.splitlines(0))
#q2='/n'.join(new_agenda)
#q3 = q2.split('/n')
a = tuple(a.splitlines(0))

print (a)

__author__ = "Jacob Roth-Ritchie"
__copyright__ = "Copyright 20019, RSquar3dT3ch"
__license__ = "GPL 3.0"
__version__ = ".01"
__maintainer__ = "Jacob Roth-Ritchie"
__email__ = "jrothritchie@hdsd.org"
__status__ = "Development"