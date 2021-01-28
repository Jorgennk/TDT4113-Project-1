'''
This is the interpreter, it takes either morse or alphabetical inout and outputs the other option. 



'''

class interpreter:
    
    #constructor, initiates morse alphabets with other variables that will be needed
    def __init__(self):
        self.current_morse_char = ""
        self.complete_morse_sentence  = ""
        self.continue_interpreting = True
        
        self.morse_to_alphabet = {
            ".-"   : "a",
            "-..." : "b",
            "-.-." : "c",
            "-.."  : "d",
            "."    : "e",
            "..-." : "f",
            "--."  : "g",
            "...." : "h",
            ".."   : "i",
            ".---" : "j", 
            "-.-"  : "k",
            ".-.." : "l",
            "--"   : "m",
            "-."   : "n",
            "---"  : "o",
            ".--." : "p",
            "--.-" : "q",
            ".-."  : "r",
            "..."  : "s",
            "-"    : "t",
            "..-"  : "u",
            "...-" : "v",
            ".--"  : "w",
            "-..-" : "x",
            "-.--" : "y",
            "--.." : "z",        
        }
        
        self.alphabet_to_morse= {
            "a" : ".-",  
            "b" : "-...",
            "c" : "-.-.",
            "d" : "-..",
            "e" : ".",   
            "f" : "..-.",
            "g" : "--.", 
            "h" : "....",
            "i" : "..",  
            "j" : ".---",
            "k" : "-.-", 
            "l" : ".-..",
            "m" : "--",  
            "n" : "-.",  
            "o" : "---", 
            "p" : ".--.",
            "q" : "--.-",
            "r" : ".-.", 
            "s" : "...", 
            "t" : "-",   
            "u" : "..-", 
            "v" : "...-",
            "w" : ".--", 
            "x" : "-..-",
            "y" : "-.--",
            "z" : "--.."
        }
   
    
    #Continues the loop until a limit where no response is detected      
    def continous_interpreter(self, input_time_interval):
        continue_loop = True
        
        while continue_loop:
            
            #set time limit for exit interpreter to 5 seconds
            if input_time_interval < 5:
                self.set_sign_on_interval(input_time_interval)
            else:
                continue_loop = False
                
        return self.complete_morse_sentence
    
    #Decide whether it is a line or a dot based on how long you hold the inout signal
    def line_or_dot(self, time):
        if time < 0.5:
            return "."
        else:
            return "-"
        
    #This is for word partitioning, decide if it is a new word or not
    def continue_or_space(self, time):
        if time < 0.5:
            return ""
        else:
            return " "
            
    
    #This takes in a list of time intervals where x%2 == 0 is the length of the button press
    #while the x%1 == 1 is the length of the pause between button presses
    def translate_time_list(self, time_list):
        morse_char = ""
        iterator = 0
        
        for time in time_list:
            #Press time
            if iterator%2 == 0:
                morse_char += self.line_or_dot(time)
            #pause time
            else:
                    morse_char += self.continue_or_space(time)
            iterator += 1
        #print(morse_char)
        return morse_char
                
    
    #This function translates alphabetical signs and outputs it in morse code            
    def letters_to_morse(self, sentence):
        morse_code = ""
    
        for letter in sentence:
            if letter == " ":
                morse_code += "| "
            else:
                morse_code += self.alphabet_to_morse[letter] + " "
                    

        return morse_code
        
    
    #Translates morse code to alphabetical letters
    def morse_to_letters(self, morse):
        
        words = morse.split("|")
        complete_alpha_sentence = ""
        iterator = 0
        
        for word in words:
            char = word.split()
            print(char)
            for c in char:
                #print(iterator)
                try:
                    print(self.morse_to_alphabet[c])
                    complete_alpha_sentence += self.morse_to_alphabet[c]
                except:
                    print("no match for that letter")
                iterator += 1
        
        print("complete: ", complete_alpha_sentence)
                
                        
            
            
#a = interpreter()
#a.translate_time_list([1.0, 0.4, 0.3, 0.4, 0.3, 0.0, 0.3, 0.0, 0.3, 0.4, 1.0])
#a.letters_to_morse("test test")

