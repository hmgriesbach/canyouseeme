# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt # standard short name
plt.ion() # sets “interactive on”: figures redrawn when updated
import random 


def hangman_display(secret, guessed):
    '''create a comparitor of guessed letters from the secret group of letters'''
    
    reveal = ' '
    for letter in secret:
        if letter == ' ':
            reveal += ' '
        elif letter in guessed:
            reveal += letter
        else:
            reveal += '_' 
    return reveal 
    
