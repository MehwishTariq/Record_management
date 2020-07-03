# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 17:12:01 2020

@author: Mehwish Tariq Ameen
"""

#from pymongo import MongoClient
import pymongo as pm

class MongoDB:
        
    def __init__(self,con_str,dbname):
        
        self.c_str = con_str
        self.db_name = dbname
        self.client = None
    
    #create database 
    def connect(self):
        
        myclient = pm.MongoClient(self.c_str)
        self.client = myclient[self.db_name]
                    
    #create collection a.k.a table in SQL
    def create_collection(self,col_name):
        
        mycol = self.client[col_name]
        return mycol
    
    #insert document a.k.a record in SQL
    def insert(self,data_dict,mycol):
        
        #check if the argument passed contains multiple records or single record
        if type(data_dict) == list:
            
            mycol.insert_many(data_dict)
            print("Record Inserted!")
            
        else:
            
            mycol.insert_one(data_dict)
            print("Records Inserted!")

    #delte document using unique id "CNIC"
    def delete(self,_id,my_col):

        _dict = {"CNIC" : _id}
        my_col.delete_one(_dict)
        print("Record Deleted!")

    #update document using unique id "CNIC" 
    def update(self,_id,set_fields,my_col):
        
        u_dict = {"$set" : set_fields} 
        _dict = {"CNIC" : _id}
        
        my_col.update_one(_dict , u_dict)
        print("Record Updated!")

#delete all courses from selected class   
    def delete_class(self,_key,my_col):
        
        index = 0
        key = _key
        mydoc = my_col.find({},{"_id":0,key:1})
        for x in mydoc:
            if len(x.keys()) == 1:
                index = x
            if len(x) != 0:
                my_col.delete_one(index)
                return '1'
            else:                    
                return '0'

    '''
#incomplete need to delete a specific course from the class        
    def delete_course(self,_key,my_col):
        #while True:
        mycol = self.client[my_col]
        key = _key
        index = []
        mydoc = mycol.find({},{"_id":0,key:1})
        for _class in mydoc:
            print(_class)
            
            if len(_class.keys()) == 1:
                _class = _class
                print(_class)
                for x in _class.values():
                    index = x
                print(index)
                course_list = []
                
                for i in range(len(index)):                    
                    no_ = i+1
                    course_list.append(str(no_)+":"+index[i])        
        
        print("\n\n\t"+str(course_list))
        print("Enter the number respective to the course you would like to delete from the list:")
        ans = int(input())-1
        print({key : ans})
        query = {key : [ans]}
        mycol.delete_one(query)
    '''

    def insert_classTeacher(self,year,_class,cnic,my_col):

        #display the courses respective to the class selected to help choose the course name
        key = _class
        index = []
        course_list = []
        mycoll = self.create_collection('Courses')
        mydoc = mycoll.find({},{"_id":0,key:1})
        #iterate over documents retrived from the query
        for _cl in mydoc:
            if len(_cl.keys()) == 1:
                _class1 = _cl
                
                for x in _class1.values():
                    index = x
                
                #display list of courses with numerals to help choose the course easily           
                for i in range(len(index)):                    
                    no_ = i+1
                    course_list.append(str(no_)+":"+index[i])   
                      
        print("\nWhich Course to assign the teacher?")
        print("\n\n\t"+str(course_list))
        print("Enter the number respective to the course you would like to assign from the list:")
        ans = input()        
        course_name = index[int(ans)-1]
        print(course_name)

        #check if the cnic provided exists in the database
        mycoll = self.create_collection('Teachers')
        mydoc = mycoll.find({ "CNIC" : { "$in" : [cnic] } } )
        #if exists get the name of the teacher and create a dictionary to insert in the db
        for x in mydoc:
            teacher_name = x['Name']
            print(teacher_name)
            class_dict = {"Year" : year , _class : [course_name , teacher_name]}
            my_col.insert_one(class_dict)
            print("Record Inserted!")
            input()

        #if doesnot exist then redirect to options page again
        if mydoc.count() == 0:
            print("CNIC is wrong please either add the record of the teacher or try addinng again!")
            input()
        

        

