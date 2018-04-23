#
## Development of Interactive Shell for the User
#
from os import system as sys_cmd
from config.CrudModule import UserCrud

class InteractiveShell:
    def __init__(self):
        self.user_object = UserCrud()
        self.prefetch_email()

    def prefetch_email(self):
        ## probable err for no data
        self.emails=self.user_object.fetch_email()

    def read_result_formatter_paginator(self,*args,**kwargs):
        pass
    
    @staticmethod
    def pause(msg):
        print(msg)
        input('Enter any key to continue . . .')

    #
    ## Refactoring infinite_loop to break it into multiple functions
    ## for reusability
    #

    def insert_into_user(self):
        uv = self.get_user_input()
        self.user_object.insert_query(**uv)

    def read_from_user(self):
        args=[]
        kwargs={}
        print('Enter fields to be displayed\nPress Enter to show all columns')
        while True:
            inp=input(self.prompt)
            if not inp:
                break
            if inp not in UserCrud.user_values:
                continue
            args.append(inp)
        args=['*'] if len(args)==0 else args
        # print('Enter filter fields to be selected seperated by space \nEnter to Quit ')
        # while True:
        #     inp=input(prompt)
        #     if not inp:
        #         break
        #     field,value = inp.split(' ')
        #     if field in self.user_object.user_values:
        #         kwargs[field]=value
        #     print('args: ',args)
        #     print('kwargs: ',kwargs)
        resultSet=self.user_object.read(*args,**kwargs)
        for row in resultSet:
            for ind,field in enumerate(row[1:]): # use slicing row[1:] if the table contains id
                print(self.user_object.user_values[ind],'\t\t',field)
        self.pause('')
    
    def update_user_info(self,email=None):
        if(not email):
            email = input('Enter email of the target row to be changed: ')
        res=self.user_object.read(*['*'],**{'email':email})
        if(email not in self.emails):
            self.pause('No Matching email')
            return
        else:
            print('Old Values\n')
            for index,fields in enumerate(self.user_object.user_values):
                print(fields,' : ',res[0][index+1]) 
                ## index+1 if id in table.
        updating_values=self.get_user_input()
        self.user_object.update(email,**updating_values)
        self.pause('User Details updated')
        self.prefetch_email()

    def delete_user_info(self,email=None):
        #
        ## Delete User Info
        #
        if(not email):
            email=input('Enter the email address of the row to be deleted: ')
        if email not in self.emails:
            self.pause('Email Does not Exist ')
            return
        self.user_object.delete(email)
        affected_rows=self.user_object.cursor_obj.rowcount
        print(affected_rows,' Rows Affefcted.')
        self.pause('')
        self.prefetch_email()

    def infinite_loop(self):
        self.prompt='root@web# '
        #
        ## Creates Table if does not exist
        #
        self.user_object.create()
        self.prefetch_email()
        while True:
            self.show_Menu()
            user_input=input(self.prompt)
            if(user_input=='1'):
                self.insert_into_user()
            elif(user_input=='2'):
                self.read_from_user()
            elif(user_input=='3'):
                # Update User Info
                self.update_user_info()
            elif(user_input=='4'):
                self.delete_user_info()
            elif(user_input=='quit'):
                break
    
    def show_Menu(self):
        sys_cmd('clear')
        print("============================================================")
        print("Interactive Database\nOptions:\n1. Insert INTO Database")
        print("2. Read FROM Database\n3. Update User Info\n4. Delete User Info\n")
        print("Type quit to close the program")

    def get_user_input(self):
        user_values={}
        for usv in self.user_object.user_values:
            user_values[usv]=input('Enter '+usv+'\t\t')
        return user_values

def main():
    ish=InteractiveShell()
    ish.infinite_loop()


if __name__ == '__main__':
    main()