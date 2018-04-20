#
## Python Library for self Project
## Create system-wide usable libraries
#

import re
# TODO @asperoph || INTRODUCE BINNING TO COMPARE PERFORMANCE
 
class Radix_Sort:
    def __init__(self,word_list):
        self.word_list=word_list
        self.max_size=max([len(word) for word in word_list])
        self.buckets=self.get_buckets(27) 
        #
        ## Total Buckets Needed = [a-z]+[#]
        # 
        self.buckets_directory=self.assign_numeric_values(
            self.get_alphabet_characters()) 
        #
        ## Simply Add Function to include Numeric character for binning
        #
        self.current_index=self.max_size

    def lsd_sort(self):
        # Maintain Length of all words
        self.word_list=self.maintain_size(self.word_list)
        # Sort in Iterative Method
        self.flat_list=self.word_list.copy()
        for index in range(1,self.max_size+1):
            for word in self.flat_list:
                self.add_to_bucket(word,index)
            self.flat_list=self.flatten()
        # TODO @asperoph || Remove Dont Care Character
        # print(self.flat_list)
        return(self.remove_dont_care_character(self.flat_list))

    def flatten(self):
        temp_list=[]
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
        return self.buckets_directory.get(character,-9999)

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
        fixlen=[]
        max_size=max(len(word) for word in old_word_list)
        for word in old_word_list:
            add=['#' for _ in range(max_size-len(word))]
            word+=''.join(add)
            fixlen.append(word.lower() if single_case else word)
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
        return [[] for _ in range(no_buckets)]
    
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