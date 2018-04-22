#
## Development of Interactive Shell for the User
#
from os import system as sys_cmd
from config.CrudModule import UserCrud

class Interactive_Shell:
    def __init__(self):
        self.user_object = UserCrud()

    def prefetch_email(self):
        ## probable err for no data
        self.emails=[elem[0] for elem in self.user_object.read(*['email'])]

    def read_result_formatter_paginator(self,*args,**kwargs):
        pass
    
    @staticmethod
    def pause(msg):
        print(msg)
        input('Enter any key to continue . . .')

    def infinite_loop(self):
        prompt='root@web# '
        #
        ## Creates Table if does not exist
        #
        self.user_object.create()
        self.prefetch_email()
        while True:
            self.show_Menu()
            user_input=input(prompt)
            if(user_input=='1'):
                uv = self.get_user_input()
                self.user_object.insert(**uv)
            elif(user_input=='2'):
                args=[]
                kwargs={}
                print('Enter fields to be displayed\nPress Enter to show all columns')
                while True:
                    inp=input(prompt)
                    if not inp:
                        break
                    args.append(inp)
                args=['*'] if len(args)==0 else args
                print('Enter filter fields to be selected seperated by space \nEnter to Quit ')
                while True:
                    inp=input(prompt)
                    if not inp:
                        break
                    field,value = inp.split(' ')
                    if field in self.user_object.user_values:
                        kwargs[field]=value
                    print('args: ',args)
                    print('kwargs: ',kwargs)
                resultSet=self.user_object.read(*args,**kwargs)
                for row in resultSet:
                    for ind,field in enumerate(row[1:]):
                        print(self.user_object.user_values[ind],'\t\t',field)
                self.pause('')

            elif(user_input=='3'):
                # Update User Info
                email = input('Enter email of the target row to be changed: ')
                res=self.user_object.read(*['*'],**{'email':email})
                if(email not in self.emails):
                    self.pause('No Matching email')
                    continue
                else:
                    print('Old Values\n')
                    for index,fields in enumerate(self.user_object.user_values):
                        print(fields,' : ',res[0][index+1])
                updating_values=self.get_user_input()
                self.user_object.update(email,**updating_values)
                self.pause('User Details updated')
                self.prefetch_email()

            elif(user_input=='4'):
                #
                ## Delete User Info
                #
                email=input('Enter the email address of the row to be deleted: ')
                if email not in self.emails:
                    self.pause('Email Does not Exist ')
                    continue
                self.user_object.delete(email)
                self.__class__.pause('Matching Records Deleted') #TODO: Add no. of Affected Rows
                self.prefetch_email()

            elif(user_input=='quit'):
                break
    
    def show_Menu(self):
        sys_cmd('clear')
        print("============================================================")
        print("Interactive Database Test\nOptions:\n1. Insert INTO Database")
        print("2. Read FROM Database\n3. Update User Info\n4. Delete User Info\n")

    def get_user_input(self):
        user_values={}
        for usv in self.user_object.user_values:
            user_values[usv]=input('Enter '+usv+'\t\t\t')
        return user_values

def main():
    ish=Interactive_Shell()
    ish.infinite_loop()


if __name__ == '__main__':
    main()