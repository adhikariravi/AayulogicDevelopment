# test library
import time
from re import sub as substitute
from config.CrudModule import UserCrud
from Caching import Caches
from Library import Radix_Sort
#
## Implement key wise searching on database results
#

class Data_Result_Searching:
    def __init__(self):
        self.userobj = UserCrud()
        self.shelving_dict=dict()
        # sorting_object=Radix_Sort(sorting_key_list)
    #
    ## We will take all the results from the User table
    ## And get the key to sort from with the `user`
    ## We will shelve the result using Caching Module
    ## And, work on the Sorting Methodology
    ## ADD: We will remove all characters and only include 
    ## Alphanumeric Character for sorting. Hence, having a fix of 36 buckets.
    
    #
    ## Define Function to remove all non-word characters
    ## to compare only numbers and alphabets
    #

    @staticmethod
    def remove_special(word):
        return substitute(r'\W+','',word)

    ## Function that removes special characters for all word in a list
    ## Replaced by a function that removes special for individual word

    # @staticmethod
    # def remove_special_characters(word_list_with_special_character):
    #     word_list_special_removed = list()
    #     for each_special_word in word_list_with_special_character:
    #         word_list_special_removed.append(substitute(r'\W+','',each_special_word))
    #     return word_list_special_removed
    
    def generate_all_results(self,sorting_key='email'):
        
        #
        ## Thread result Fetch and shelve 
        #
        
        ## Fetch all results in (id,name,email,......) form

        ## Slicing all results for first 1k rows

        # self.all_results=self.userobj.read()[:10000]
        self.all_results=self.userobj.read()
       
        ### Instead of fetching all results
        ### Only fetching email
        # start = time.process_time()
        # emails = self.userobj.fetch_email()
        # end = time.process_time()
        # self.total_time_to_fetch=end-start
        ## Sorting Key is the key to sort from | Hardcoded Email
        # sorting_key=self.get_sorting_key()

        # sorting_key='email'

        # The user values exclude id so we include it in get_dict_key
        # all_keys=self.remove_special_characters(list(shelving_dict.keys()))

        ## Iterating through all the result set tuple i.e. (id,name,email,..)
        
        for each_tuple in self.all_results:
        
            ## Fetch the sorting_key index from self.uservalues
            ## Remember tuples are (id,name,email,phone,...)
            ## User values are (name,email,phone)
            ## Add 1 to index if the table contains `id` field
            index_of_sorting_key = UserCrud.user_values.index(sorting_key)+1
            
            # get_dicx returns the special characters removed from the key(email)
            # i.e. ravi.adhikari@aayulogic.com=>raviadhikariaayulogiccom
            # Value is tuple set containing the email
            
            key, value = self.get_dicx(each_tuple[index_of_sorting_key]),each_tuple
            # Adding values to a dictionary for shelving
            self.shelving_dict[key]=value

        # Shelves given dictionary(arg1) to the given filename (arg2)

        # Caches.shelve_dictionary(shelving_dict,'webcache')
        
        # All Keys listed for Searching
        # Remember: emails are the special removed form.
        # Equivalent email must be fetched from the shelve cache

        self.all_keys=[key.lower() for key in self.shelving_dict.keys()]
        # print(all_keys)
        # input('All Keys Above')        
        # lsd_sort() sorts the given wordlist (to the class)
        
        ### all_keys is email list
        # special_removed_keys = [self.remove_special(email) for email in emails]
        self.radix_sort_obj = Radix_Sort(self.all_keys)
        # self.radix_sort_obj = Radix_Sort(all_keys)
        start = time.process_time()
        self.sorted_keys = self.radix_sort_obj.lsd_sort()
        end = time.process_time()
        self.total_time_to_sort = end-start

        #
        ## Unshelve Keys in order of sorted_keys
        #

        # all_dict = Caches.unshelve_dictionary('webcache')

        ## Return tuple (id,name,email,...) of each special removed sorting key
        ## Eg. raviadhikariaayulogic.com=>(1,'Ravi Adhikari','ravi.adhikari@aayulogic.com',...)

        # sorted_tuple = [all_dict.get(sorted_key,'NOT FOUND') for sorted_key in sorted_keys]
        # sorted_tuple = [self.shelving_dict.get(sorted_key,'NOT FOUND') for sorted_key in sorted_keys]
        # # print(sorted_keys)
        # # input()
        # print(self.shelving_dict.keys())
        # input()
        # return sorted_tuple
        # return sorted_keys

    def return_all_results(self,sorting_key='email'):
        self.generate_all_results(sorting_key)
        sorted_tuple = [self.shelving_dict.get(sorted_key,'NOT FOUND') for sorted_key in self.sorted_keys]
        # print(sorted_keys)
        # input()        
        return sorted_tuple

    def get_result_by_email(self,email):
        self.generate_all_results()
        sr_email=self.remove_special(email)
        return self.shelving_dict[self.remove_special(sr_email)]
    
    def get_dicx(self,sort_key):
        #
        ## Remove Non Word Characters 
        ## Including ' ','.','@',etc.
        #

        # super_key=''
        # usv=UserCrud.user_values
        # if sort_key in usv:
            # super_key+=self.remove_special(curr_tuple[usv.index(sort_key)+1])
        special_removed_key = self.remove_special(sort_key)
        return special_removed_key.lower()

    #
    ## Sorting Key Disabled to search only through emails
    # 
        
    # @staticmethod
    # def get_sorting_key():
    #     print("Enter Select Key\nValid Keys are\n",','.join(UserCrud.user_values))
    #     selected=input('>>> ')
    #     return selected