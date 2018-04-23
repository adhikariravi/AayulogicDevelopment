#
## Python Library for self Project
## Create system-wide usable libraries
#

import re
from config.CrudModule import UserCrud

# TODO @asperoph || INTRODUCE BINNING TO COMPARE PERFORMANCE
 
class RadixSort:
    def __init__(self,word_list):

        #
        ## Manipulate Word List to remove non-word character
        ## Replaces all special_characters_and_spaces
        #
        self.word_list=word_list
        self.max_size=max([len(word) for word in word_list])
        self.buckets=self.get_buckets(37) 

        #
        ## During sorting, a new problem was detected. i.e 
        ## names can contain uppercase as well as lowercase characters.
        ## 
        ## Bucket Size is 26 alphabets + 10 numbers 
        #
        ## Total Buckets Needed = [a-z]+[#]
        # 
        self.buckets_directory=self.assign_numeric_values(
            self.get_numeric_characters()+
            self.get_alphabet_characters()) 
        #
        ## Simply Add Function to include Numeric character for binning
        #
        self.current_index=self.max_size

    @staticmethod
    def lsd_numeric(sort):
        pass

    def lsd_sort(self):
        # Maintain Length of all words
        self.word_list=self.maintain_size(self.word_list)
        # Sort in Iterative Method
        self.flat_list=self.word_list.copy()
        for index in range(1,self.max_size+1):
            for word in self.flat_list:
                self.add_to_bucket(word,index)
            self.flat_list=self.flatten()
        return(self.remove_dont_care_character(self.flat_list))

    def flatten(self):
        temp_list=list()
        for each_list in self.buckets:
            if not each_list:
                continue
            for each_word in each_list:
                temp_list.append(each_word)
        #
        ## Reset Buckets 
        #
        self.empty_buckets()
        return temp_list
    
    def empty_buckets(self):
        for each_bucket in self.buckets:
            while len(each_bucket)>0:
                each_bucket.pop()

    def add_to_bucket(self,word,index):
        self.buckets[self.get_dict_info(word[-index])].append(word)

    def get_dict_info(self,character):
        #
        ## Return invalid number so we know invalid character has been judged
        ## Not Handled || Breaks Code
        #
        index=self.buckets_directory.get(character,-9999)
        if(index==-9999):
            print(f'Invalid Index for {character}')
        return index

    @staticmethod
    def get_alphabet_characters():
        #
        ## Recieve 26 alphabets from 'a'=> 26
        #
        return [chr(i) for i in range(97,97+26)] 
    
    @staticmethod
    def get_numeric_characters():
        #
        ## Recieve 10 numeric character from '0'
        #
        return [chr(i) for i in range(ord('0'),ord('0')+10)]
    
    @staticmethod
    def maintain_size(old_word_list,single_case=True):

        ## Add functionality to accept both cases. Ignored due to high no. of buckets

        fixlen=list()
        max_size=max(len(word) for word in old_word_list)
        for word in old_word_list:
            add=['#' for _ in range(max_size-len(word))]
            word+=''.join(add)
            fixlen.append(word)
        return fixlen

    @staticmethod
    def remove_dont_care_character(word_list,dont_care_character='#'):
        #
        ## Use re to sub matching criteria from back
        ## for faster manipulation
        #
        removed_list=list()
        for each_word in word_list:
             removed_list.append(re.sub('[#]+$','',each_word))
        return removed_list

    @staticmethod
    def get_buckets(no_buckets):
        #
        ## Create multiple empty buckets / bins
        #
        return [list() for _ in range(no_buckets)]
    
    @staticmethod
    def assign_numeric_values(char_list,dont_care_character='#'):
        #
        ## Assigns numeric values in dictionary
        ## for recieved list starting from 1.
        ## 0 is used for dont_care_character
        #
        assigned_values={character:index+1 for index,character in enumerate(char_list)}
        assigned_values[dont_care_character]=0
        return assigned_values

class SearchMethods:

    @staticmethod
    def growth_function(current_item, search_item):
        pass

    @staticmethod
    def binary_search(unsorted_list,item):
        sorted_list=RadixSort(unsorted_list).lsd_sort()
        last=len(sorted_list)-1
        first=0
        while(first<=last):
            mid = int((first+last)//2)
            if(sorted_list[mid]==item):
                return mid
            else:
                if item<sorted_list[mid]:
                    last=mid-1
                else:
                    first=mid+1
        return False
