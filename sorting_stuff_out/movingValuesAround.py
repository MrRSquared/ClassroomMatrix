#!/usr/bin/env python
# Display a runtext with double-buffering.

def text():
    #this method will create a text string
    text_string = 'What is up?'
    return text_string
    # if you want to return multiple items, you must use an 
    # iterable format for one instead (tuple, list, dict, etc)

def print_text(text_to_print):
    print(text_to_print)

print_text(text())