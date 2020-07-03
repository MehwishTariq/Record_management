# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 21:04:01 2020

@author: Mehwish Tariq Ameen
"""

import getpass as gp
import pandas as pd
import click
import mainMenu as mm


class LogIn:
    
    def __init__(self,path):
        
        #append file name
        self.path = path + '/Accounts.xlsx'
        self.user = ''
        self.pwrd = ''
        
    def menu(self):
        
        print("\n\n\t\t\tLOG IN\n")        
        #input username
        print("\nUsername: ")
        self.user = input() 
        #input password for the id
        self.pwrd = gp.getpass() 
        #check credentials 
        self.checkAcc()
        
    def checkAcc(self):
               
        #get data in a data frame from excel file
        data = pd.read_excel(self.path)
               
        #compare the entered id and password with all username and passwords in df
        if self.user in data['Usernames'].values and self.pwrd in data['Passwords'].values:
            print("Logging In...")
            #clear console screen
            click.clear()
            #goto next page
            mm.options()            
            
        #clear console if wrong and again ask for login credentials
        else:
            print("Username or password is incorrect! Try again")
            input()
            click.clear()
            self.menu()
    