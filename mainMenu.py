# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 19:37:53 2020

@author: Mehwish Tariq Ameen
"""

#connection file for mongoDB
import mongoCon as con
import click

mydb = 'myDB'

con_str = 'mongodb+srv://Mehwish:khanfamily@cluster0-imf2y.mongodb.net/test'

#call connection file function to connect to MongoDB
conn = con.MongoDB(con_str,mydb)
conn.connect()

def options():
        
        print("Press: \n")
        print("1: To Enter Student Record \n")
        print("2: To Enter Teacher Record \n")
        print("3: To Enter Courses Record \n")
        print("4: To Enter Course Teacher \n")
        print("5: To Enter Student Count \n")
        print("6: To Enter Student Marks \n")
        print("7: To Delete Student Record \n")
        print("8: To Delete Teacher Record \n")
        print("9: To Delete Courses Record \n")
        print("10: To Delete Course Teacher \n")
        print("11: To Delete Student Count \n")
        print("12: To Delete Student Marks \n")
        print("13: To Update Student Record \n")
        print("14: To Update Teacher Record \n")
        print("15: To Update Courses Record \n")
        print("16: To Update Course Teacher \n")
        print("17: To Update Student Count \n")
        print("18: To Update Student Marks \n")
        print("\nPress 'q' to exit\n")
        
        ans = input() 
        if ans == 'q':
            exit()
        
    #call respective function on the basis of the selection above
        if int(ans) in range(1,7):#['1','2','3','4','5','6']:
            enter_record(ans)
        
        if int(ans) in range(7,13):#['7','8','9','10','11','12']:
            delete_record(ans)
            
        if int(ans) in range(13,19):#['13','14','15','16','17','18']:
            update_record(ans)
        
        
#call functions of respective classes 
#and insert records in db in their respective collections 

def enter_record(ans):
        
        if ans == '1':
            #import from studentData.py            
            import studentData as sd
            click.clear()
            #create object for StudentData class and class its function
            s_data = sd.StudentData()
            mycoll = conn.create_collection('Student')
            conn.insert(s_data.record_Dict(),mycoll)
            options()
                                    
        if ans == '2':
            #import from teacherData.py            
            import teacherData as td
            click.clear()
            #create object for TeacherData class and class its function
            t_data = td.TeacherData()
            mycoll = conn.create_collection('Teachers')
            conn.insert(t_data.record_Dict(),mycoll)
            options()
            
        if ans == '3':
            #import from courses.py            
            import courses as cd
            click.clear()
            #create object for Courses class and class its function
            c_data = cd.Courses()
            mycoll = conn.create_collection('Courses')
            conn.insert(c_data.record_Dict(),mycoll)
            options()
    
        if ans == '4':

            #import from courseTeacher.py
            import courseTeacher as ct
            click.clear()
            #create object for courseTeacher class and class its function
            ct_data = ct.CourseTeacher()
            mycoll = conn.create_collection('CourseTeacher')
            year,_class,cnic = ct_data.record_Dict()
            conn.insert_classTeacher(year,_class,cnic,mycoll)
            options()
'''        
        if ans == '5':
            
            #import from studentCount.py
            import studentCount as sc
            click.clear()
            #create object for StudentCount class and class its function
            sc_data = sc.StudentCount()
            mycoll = conn.create_collection('StudentCount')
            conn.insert(sc_data.record_Dict(),mycoll)
            options()
     
        if ans == '6':           
            #import from studentMarks.py
            import studentMarks as sm
            click.clear()
            #create object for StudentMarks class and class its function
            sm_data = sm.StudentMarks()
            mycoll = conn.create_collection('StudentMarks')
            conn.insert(sm_data.record_Dict(),mycoll)
            options()
'''
#call functions of respective classes 
#and delete records in db in their respective collections 

def delete_record(ans):
    
    if ans == '7':
            
        import studentData as sd
        click.clear()
        s_data = sd.StudentData()
        while True:
        #passing string as collection name  
            conn.delete(s_data.delete_data(),conn.create_collection('Student'))
            print("\n Deleted! Enter to delete more or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
        
    if ans == '8':
            
        import teacherData as td
        click.clear()
        t_data = td.TeacherData()
        while True:
            
            conn.delete(t_data.delete_data(),conn.create_collection('Teachers'))
            print("\n Deleted! Enter to delete more or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
            
            
    if ans == '9':
            
        import courses as cd
        click.clear()
        c_data = cd.Courses()
        while True:
           
            '''
            key,ans = c_data.delete_data()
            
            if ans == '1':
                _no = conn.delete_class(key,'Courses')
                
            if ans =='2':
                _no = conn.delete_course(key,'Courses')
            '''
 
            key = c_data.delete_data()
            _no = conn.delete_class(key,conn.create_collection('Courses'))

            if _no == '1':
                print("\n Deleted! Enter to delete more or Press 'q' to go back")

            if _no == '0':   
                print("\n Doesnot Exist! Enter to delete other or Press 'q' to go back")

            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
            
            
    if ans == '10':
            
        import courseTeacher as ct
        click.clear()
        ct_data = ct.CourseTeacher()
        while True:
            
            conn.delete(ct_data.delete_data(),conn.create_collection('CourseTeacher'))
            print("\n Deleted! Enter to delete more or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
            
'''           
    if ans == '11':
            
        import studentCount as sc
        click.clear()
        sc_data = sc.StudentCount()
        while True:
            
            conn.delete(sc_data.delete_data(),conn.create_collection('StudentCount'))
            print("\n Deleted! Enter to delete more or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
            
            
    if ans == '12':
        
        import studentMarks as sm
        click.clear()
        sm_data = sm.StudentMarks()
        while True:
            
            conn.delete(sm_data.delete_data(),conn.create_collection('StudentMarks'))
            print("\n Deleted! Enter to delete more or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
'''
#call functions of respective classes 
#and update records in db in their respective collections 
           
def update_record(ans):
       
    if ans == '13':
            
        import studentData as sd
        click.clear()
        s_data = sd.StudentData()
        set_fields = {}
        while True:
            
            _id,set_fields = s_data.update_data()
            #print(set_fields)
            conn.update(_id,set_fields,conn.create_collection('Student'))
            print("\nUpdate! Enter to Update more records or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
        
    if ans == '14':
            
        import teacherData as td
        click.clear()
        t_data = td.TeacherData()
        set_fields = {}

        while True:
            _id,set_fields = t_data.update_data()
            #print(set_fields)
            conn.update(_id,set_fields,conn.create_collection('Teachers'))
            print("\n Update! Enter to Update more records or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
            
'''        
    if ans == '15':
            
        import courseData as cd
        click.clear()
        c_data = cd.CourseData()
        set_fields = {}

        while True:
            _id,set_fields = c_data.update_data()
            #print(set_fields)
            conn.update(_id,set_fields,conn.create_collection('Courses'))
            print("\n Update! Enter to Update more records or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
     
            
    if ans == '16':
            
        import courseTeacher as ct
        click.clear()
        ct_data = ct.CourseTeacher()
        set_fields = {}

        while True:
            _id,set_fields = ct_data.update_data()
            #print(set_fields)
            conn.update(_id,set_fields,conn.create_collection('CourseTeacher'))
            print("\n Update! Enter to Update more records or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
            
            
    if ans == '17':
            
        import studentCount as sc
        click.clear()
        sc_data = sc.StudentCount()
        set_fields = {}

        while True:
            _id,set_fields = sc_data.update_data()
            #print(set_fields)
            conn.update(_id,set_fields,conn.create_collection('StudentCount'))
            print("\n Update! Enter to Update more records or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue
        options()
            
            
    if ans == '18':
        
        import studentMarks as sm
        click.clear()
        sm_data = sm.StudentMarks()
        set_fields = {}

        while True:
            _id,set_fields = sm_data.update_data()
            #print(set_fields)
            conn.update(_id,set_fields,conn.create_collection('StudentMarks'))
            print("\n Update! Enter to Update more records or Press 'q' to go back")
            #break loop if 'exit' is entered
            if input()=='q':
               break
            #if enter is pressed start the loop again
            else:      
                click.clear()
                continue    
        options()
'''
