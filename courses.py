# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:25:35 2020

@author: Mehwish Tariq Ameen
"""

import click

class Courses:
    
    #enter courses of each class save in a list of dictionaries and return the list     
    def record_Dict(self):
        
        course = []
        record = []
     
        print("\nEnter Course names for following classes: ")
        print("\n Instruction: Enter all courses in one line with comma(,) as a separator.")
        print("\n e.g: Maths,Science,Urdu..etc")
        
        #using split as all courses are being entered in one line
        #append in a list and then append it in another list as a dictionary
        
        print("\n\nFor class-I: ")
        course = input().split(',')
        record.append({"Class- I" : course})
        
        print("\nFor class-II: ")
        #II.append(input().split(','))
        course = input().split(',')
        record.append({"Class- II" : course})
        
        print("\nFor class-III: ")
        #III.append(input().split(','))
        course = input().split(',')
        record.append({"Class- III" : course})
        
        print("\nFor class-IV: ")
        #IV.append(input().split(','))
        course = input().split(',')
        record.append({"Class- IV" : course})
        
        print("\nFor class-V: ")
        #V.append(input().split(','))
        course = input().split(',')
        record.append({"Class- V" : course})
                    
        click.clear()
        return record
        
        
#get unique id(i.e: CNIC) from user to delete the specific record one by one
    def delete_data(self):
                    
        print("\n Which class course would you like to delete?\nPress:\n")
        print("\n1: Class-I")
        print("2: Class-II")
        print("3: Class-III")
        print("4: Class-IV")
        print("5: Class-V")
        ans1 = input()
    
        #if ans =='1':
                
        if ans1 == '1':
            return "Class- I"#,1
            
        if ans1 == '2':
            return "Class- II"#,1
    
        if ans1 == '3':
            return "Class- III"#,1            
    
        if ans1 == '4':
            return "Class- IV"#,1
        
        if ans1 == '5':
            return "Class- V"#,1
    
        '''
        if ans =='2':
                
            if ans1 == '1':
                return "Class- I",'2'
                
            if ans1 == '2':
                return "Class- II",'2'
        
            if ans1 == '3':
                return "Class- III",'2'            
        
            if ans1 == '4':
                return "Class- IV",'2'
            
            if ans1 == '5':
                return "Class- V",'2'
        '''