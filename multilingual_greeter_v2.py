from typing import Dict

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {1 : 'English', 2: 'Spanish', 3: 'Portugeuse'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {1: 'What is your name?', 2: '¿Cómo te llamas?', 3: 'Qual é o seu nome?'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {1: 'Hello', 2: 'Hola', 3: 'Olá'
}

def print_language_options(lang_options: Dict[int, str]) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print("Please choose a language: ")
    for key in lang_options:
        print(str(key) + ': ' + lang_options[key])  # remove pass statement and implement me
#print_language_options(lang_dict)


def language_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    iterateStr = 'Please enter a language choice of '
    for key in lang_dict:
        iterateStr += str(key) + ' for ' + lang_dict[key] + ', '


    choice = input(iterateStr[:-2] + '\n')
    return int(choice)  # remove pass statement and implement me


def language_choice_is_valid(lang_options: Dict[int, str], lang_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    if lang_choice in lang_options.keys():
        return True
    else:
        return False


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    return name_prompt_options[lang_choice]  # remove pass statement and implement me


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """

    return input(name_prompt)
    


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
   
    #print(greetings_options[lang_choice] +' ' +  name + 'haha \n')
    print(greetings_options[lang_choice] + ' ' + name)

def admin_or_user():
    decision = input("Welcome to the multilingual greeter! Please select \n1: for admin mode \n2: for user mode\n3: to quit\n")
    return int(decision)


def admin_mode():
    decision = input("You are now in admin mode. Please select\n1: add support for existing languages\n2: update greetings\n3: update a name prompt\n4: main menu \nPlease note new languages need a new greeting and a new name prompt\n")
    return decision
def add_languages():
    languageToAdd = input("Please enter a language to add\n")
    lang_dict[len(lang_dict) + 1] = languageToAdd


def add_greetings():
    greetingToAdd = input("Please enter a greeting to add\n")
    greetings_dict[len(greetings_dict) + 1] = greetingToAdd

def add_hello():
    new_name_prompt = input('Please enter a new name question\n')
    name_prompt_dict[len(name_prompt_dict) + 1] = new_name_prompt


if __name__ == '__main__':
    while True:
        menuDec = admin_or_user()
        if menuDec == 3:
            print('Goodbye! :)')
            break
        elif menuDec == 1:
            while True:
                adminDec = admin_mode()
                print("adminDec: " + str(adminDec))
                if int(adminDec) == 4:
                    break
                elif int(adminDec) == 1:
                    a = add_languages()
                    print(lang_dict)
                elif int(adminDec) == 2:
                    b = add_greetings()
                    print(greetings_dict)
                elif int(adminDec) == 3:
                    c = add_hello()
                    print(name_prompt_dict)
                else:
                    print('This is not a valid input')
        else:
            print_language_options(lang_dict)
            chosen_lang = language_input()
            while language_choice_is_valid(lang_dict, chosen_lang) is False:
                print("Invalid selection. Try again.")
                chosen_lang = language_input()

            selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
            chosen_name = name_input(selected_prompt)
            greet(chosen_name, greetings_dict, chosen_lang)
