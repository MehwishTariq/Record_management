# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 00:08:06 2020

@author: Mehwish Tariq Ameen
"""


import signUp as sp
import logIn as lg
import click
import os

#get path of the root directory for Accounts.xlsx file
path = os.getcwd()

print("\n\nLog In or Sign Up?\nPress:\n1: Login \n2: Signup\n\n")
ans = input()

#create object of these classes
log = lg.LogIn(path)
sUp = sp.SignUp(path)

if ans == '1':
    
    #clear console screen
    click.clear()
    #opens login area
    log.menu()

if ans == '2':

    #clear console screen
    click.clear()
    #opens signup area
    sUp.get_idPass()
    
    print("\n\nLog In?\nPress Enter to move to login area or press 'q' to quit\n\n")
    if input() == 'q':
        exit
    else:    
        #clear console screen
        click.clear()
        #opens login area
        log.menu()

else:
    exit
