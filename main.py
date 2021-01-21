'''
Must install keyboard (pip3 instlal keyboard)


'''

from time import sleep

from keyboard import press
import keyboard
import press_interval
import interpreter

inter = interpreter.interpreter()
test = press_interval.press_interval("a")
continue_loop = True
morse_message = "" #Don't really need this, declared it here for no underline in editor
continue_menu = True

while continue_menu:
    choice = input("0 for exit, 1 for morse input, 2 for text to morse: ")
    
    if choice == "0":
        continue_menu = False
        
    if choice == "1":
        print("Morse interpreter started")
        continue_loop = True
        time_list = []
        morse_message = ""
        
        while continue_loop:   
            continue_loop = True
            time_list.append(test.press_checker())
            continue_loop = test.pause_timer(time_list) #test.pause_checker(time_list)      
            print(time_list)

        morse_message += inter.translate_time_list(time_list)
        inter.morse_to_letters(morse_message)

        print("Detected \"x\", exiting...")
    elif choice == "2":
        user_answer = input("Write something you want in morse: ")
        in_morse = inter.letters_to_morse(user_answer)
        print("In morse code \"", user_answer,"\" is: ", in_morse )
    else:
        print("Input not recognized")