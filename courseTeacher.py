import click

class CourseTeacher:
    
    #enter course teacher data save in a list of dictionaries and return the list     
    def record_Dict(self):
        
        _class = ''
        while True:

            print("\nEnter the Year of Assigning: ")
            year = input()

            while True:
                print("\nEnter CNIC: ")
                cnic = input()
                if len(cnic) != 13:
                    print("\nCNIC contains 13 digits, Please try again!")
                    continue
                else:
                    break
            
            print("\nWhich class to assign the teacher?")
            print("\n1: Class-I")
            print("2: Class-II")
            print("3: Class-III")
            print("4: Class-IV")
            print("5: Class-V")
            ans = input()

            if ans == '1':
                _class = "Class- I"
            
            if ans == '2':
                _class = "Class- II"
        
            if ans == '3':
                _class = "Class- III"            
        
            if ans == '4':
                _class = "Class- IV"
            
            if ans == '5':
                _class = "Class- V"
            
            return year,_class,cnic

#get unique id(i.e: CNIC) from user to delete the specific record one by one
    def delete_data(self):
        
        while True:
            
            print("\nEnter CNIC of teacher to delete his/her record: ")  
            
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
            
            print("\nEnter CNIC of teacher to update his/her record: ")  
            
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
          
        #print(_dict)
        return cnic,_dict
        
        