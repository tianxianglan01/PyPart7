from multilingual_greeter_v3 import Greeter

newGreeting = Greeter()

#print(newGreeting.admin_or_user())
#break up main while loop into another class?

while True:
    print('')
    a_or_u = newGreeting.admin_or_user()
    #print(a_or_u)
    if a_or_u == 3:
        break
    elif a_or_u == 2: #user mode
            newGreeting.print_language_options() #prints language options

            newGreeting.language_input() #picks which language with an int

            while newGreeting.language_choice_is_valid() == False:
                print("Invalid selection. Try again.") #makes sure one of the choices is valid
                newGreeting.language_input()
            newGreeting.get_name_input() #assigns a greeting based on language choice

            newGreeting.name_input() #passes name

            newGreeting.greet()


    elif a_or_u == 1: #admin mode
        a_choice = newGreeting.admin_choices()
        while True:
            if a_choice == 1:
                newGreeting.add_lang()
                
            elif a_choice == 2:
                newGreeting.add_greeting()
                
            elif a_choice == 3:
                newGreeting.add_name_prompt()
                
            elif a_choice == 4:
                newGreeting.add_greeting__existing_greeting()
            elif a_choice == 5:
                break
            else:
                print("Invalid selection. Try again.")
            a_choice = newGreeting.admin_choices()
    else:
        print('Invalid Selection, please try again')


