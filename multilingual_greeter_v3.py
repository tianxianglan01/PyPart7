from typing import Dict
import random

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
class Greeter():
    

    def __init__(self):
        self.lang_dict = {1 : 'English', 2: 'Spanish', 3: 'Portugeuse'}
        self.name_prompt = {1: 'What is your name?', 2: '¿Cómo te llamas?', 3: 'Qual é o seu nome?'}
        self.greetings_dict = {1: ['Hello', 'Hey', 'Sup'], 2: ['Hola', 'Mucho Gusto', 'Gusto en verlo'], 3: ['Olá', 'Oi', 'E aí?']}

        self.language_Choice = None
        self.asking_for_name = None
        self.name = None
        self.greeting = None

        self.user_or_admin = None
        self.admin_choice = None
        #self.name_prompt = None

    def print_language_options(self):
        print("Please choose a language: ")
        for key in self.lang_dict:
            print(str(key) + ': ' + self.lang_dict[key])
    
    def language_input(self):
        iterateStr = 'Please enter a language choice of '
        for key in self.lang_dict:
            iterateStr += str(key) + ' for ' + self.lang_dict[key] + ', '

        self.language_Choice = input(iterateStr[:-2] + '\n')
        #print('language_Choice: ', self.language_Choice)
        print("You picked: "  + self.lang_dict[int(self.language_Choice)])
        return

    def language_choice_is_valid(self):
        if int(self.language_Choice) in self.lang_dict.keys():
            #print('Language is valid')
            return True
        else:
            #print('Language is not valid')
            return False

    def get_name_input(self):
        self.asking_for_name = self.name_prompt[int(self.language_Choice)]
        #print('self.name_prompt: ' + self.greeting_of_choice)
        return

    def name_input(self):
        self.name = input(self.asking_for_name + '\n')
        return 
    
    def greet(self):
        print(random.choice(self.greetings_dict[int(self.language_Choice)]) + ' ' + self.name)

    def admin_or_user(self):
        choice = int(input("Please select 1 for admin, 2 for user mode, 3 to quit\n"))
        self.user_or_admin = choice
        print('you picked: ' + str(self.user_or_admin))
        return choice
    
    def admin_choices(self):
        self.admin_choice = int(input("You are now in admin mode. Please select\n1: add a language\n2: update greetings\n3: update a name prompt\n4: add greeting to existing language\n5: main menu \nPlease note new languages need a new greeting and a new name prompt\n"))
        return self.admin_choice
    
    def add_lang(self):
        language = input("Please enter a language to add\n")
        self.lang_dict[len(self.lang_dict) + 1] = language
        print(self.lang_dict)
        return 
    
    def add_name_prompt(self):
        name_prompt = input("Please enter a name prompt to add\n")
        self.name_prompt[len(self.name_prompt) + 1] = name_prompt
        print(self.name_prompt)
        return 
    
    def add_greeting(self):
        greeting = input("Please enter a greeting to add\n")

        #if self.greetings_dic
        self.greetings_dict[len(self.greetings_dict) + 1] = [greeting]
        print(self.greetings_dict)
        return 
    def add_greeting__existing_greeting(self):
        lang_pick = input("Please enter the language # you'd like to update with a greeting\n")
        if int(lang_pick) not in self.greetings_dict.keys():
            print('Your language selection does not already exist.')
            self.add_greeting__existing_greeting()
        else:
            greeting = input("Please enter a greeting to add\n")
            self.greetings_dict[int(lang_pick)].append(greeting)
            print(self.greetings_dict)




#always use an intstance to test on your class methods
    
    
    
