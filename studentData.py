# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 21:25:35 2020

@author: Mehwish Tariq Ameen
"""

import click

class StudentData:
    
    #enter student data save in a list of dictionaries and return the list     
    def record_Dict(self):
        
        student_list = []
        while True:
            
            print("\nEnter Full name: ")
            name = input()
            print("\nEnter Father's name: ")
            f_name = input()
            print("\nEnter Gender: ")
            gen = input()
            print("\nEnter Age: ")
            age = input()
            print("\nEnter Address: ")
            add = input()
            print("\nEnter Contact: ")
            contact = input()
            while True:
                print("\nEnter CNIC: ")
                cnic = input()
                if len(cnic) != 13:
                    print("\nCNIC contains 13 digits, Please try again!")
                    continue
                else:
                    break
            
            s_dict = {"Name": name, "Father's Name":f_name, "Gender":gen,
                             "Age": age, "Address": add,"Contact": contact,"CNIC":cnic}
            
            student_list.append(s_dict)
            
            print("\n Entered! Enter to add more users or Press 'q' to go back")
            #break loop if 'q' is entered
            if input()=='q':
                break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        
        return student_list

#get unique id(i.e: CNIC) from user to delete the specific record one by one
    def delete_data(self):
        
        while True:
            
            print("\nEnter CNIC of student to delete his/her record: ")  
            
            cnic = input()
           
            if len(cnic) == 13 : #since cnic is 14 digits
        
                return cnic
            
            else:
                print("\nCNIC contains 14 digits, Please try again!")
                continue

#get unique id(i.e: CNIC) from user to update the specific record one by one
    def update_data(self):
         
        _dict = {}
        while True:
            
            print("\nEnter CNIC of student to update his/her record: ")  
            
            cnic = input()
           
            if len(cnic) == 13 : #since cnic is 14 digits
        
                while True:
                    
                    print("\nWhat would you like to update? Press\n")
                    print("1: Name")
                    print("2: Father's Name")
                    print("3: Gender")
                    print("4: Age")
                    print("5: Address")
                    print("6: Contact\n")
                    
                    while True:
                       
        #get the option and the new value and append it in dictionary with its key
                        ans = input()
                        print("\n\nEnter the new value: ")
                        n_val = input()
                        
                        if ans == '1':                            
                            _dict.update({"Name" : n_val})
                            #print(_dict)
                            
                        if ans == '2':                            
                            _dict.update({"Father's Name": n_val})
                            #print(_dict)
                            
                        if ans == '3':                            
                            _dict.update({"Gender" : n_val})
                            #print(_dict)
                            
                        if ans == '4':                            
                            _dict.update({"Age" : n_val})
                            #print(_dict)
                            
                        if ans == '5':                            
                            _dict.update({"Address" : n_val})
                            #print(_dict)
                            
                        if ans == '6':                            
                            _dict.update({"Contact" : n_val})
                            #print(_dict)
                            
                        print("\nEnter to update another field or Press 'q' to go back")
                        #break loop if 'q' is entered
                        if input()=='q':
                            break
                        #if enter is pressed start the loop again
                        else:   
                            print("\n\nPress: ")
                            continue
                    
                    click.clear()
                    break
                
                break
                              
            else:
                print("\nCNIC contains 13 digits, Please try again!")
                continue
          
    #return both cnic and dictionary of updated fields
        return cnic,_dict
        
        