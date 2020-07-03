# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 20:43:30 2020

@author: Mehwish Tariq Ameen
"""

import getpass as gp
import pandas as pd
from openpyxl import load_workbook
import os


class SignUp:
    
    def __init__(self,path):
        self.path = path
        
    #Create accounts for teachers
    def get_idPass(self):
        
        #create lists for all user and passwords
        ids = []
        psd = []
        print('SIGN UP')
        #loop to create accounts until 'q' is entered
        while True:
            
            #input username
            print("\nUsername: ")
            user = input() 
            #add to id's list
            ids.append(user)
            #input password for the id
            pwd = gp.getpass() 
            #add to psd list
            psd.append(pwd)
            print("\n Entered! Enter to add more users or Press 'q' to go back")
            #break loop if 'q' is entered
            if input()=='q':
                break
            #if enter is pressed start the loop again
            else:            
                continue
        
        #create a dictionary to contain all username with respective passwords
        all_id = pd.DataFrame({'Usernames' : ids,'Passwords' : psd})
        
        #call function to create and save id password to an excel file
        self.createXlsx(all_id,'Accounts.xlsx')
       
    #create excel file to store accounts
    def createXlsx(self,all_id,filename):
        
        path = self.path + '/' + filename
        
        #call append function to append id pass to excel file if file already exists
        if os.path.exists(path):
            self.appendXlsx(all_id,path)
        
        else:    
            # Create a Pandas Excel writer using XlsxWriter as the engine.
            writer = pd.ExcelWriter(path, engine='openpyxl')
            all_id.to_excel(writer, sheet_name='Sheet1', index=False)
            # Close the Pandas Excel writer and output the Excel file.
            writer.save()
            
    #append any newly created account in the excel file
    def appendXlsx(self,all_id,path):   
        
        writer = pd.ExcelWriter(path, engine='openpyxl')
        # try to open an existing workbook
        writer.book = load_workbook(path)
        # copy existing sheets
        writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
        # read existing file
        reader = pd.read_excel(path)
        # write out the new sheet
        all_id.to_excel(writer, index=False,header=False,startrow=len(reader)+1)     
        writer.close()
    
    
