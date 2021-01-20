

class interpreter:
    
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


    def set_sign_on_interval(self, input_time_interval):
        if input_time_interval < x:
            self.current_morse_char += "."
         
        elif input_time_interval < y:
            self.current_morse_char += "-"
         
        #Erase this part? @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
        elif input_time_interval < z:
            try:
                print("character deteced: ", self.morse_to_alphabet[self.current_morse_char])
                self.complete_morse_sentence += self.morse_to_alphabet[self.current_morse_char]    
            except:
                print("Error, invalid input. Unrecognizable morse")
            self.current_morse_char = ""
            
    
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
    
    def line_or_dot(self, time):
        if time < 0.5:
            return "."
        else:
            return "-"
        
    def continue_or_space(self, time):
        if time < 0.5:
            return ""
        else:
            return " "
            
    
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
        print(morse_char)
        return morse_char
                
                
    def letters_to_morse(self, sentence):
        morse_code = ""
    
        for letter in sentence:
            if letter == " ":
                morse_code += "| "
            else:
                morse_code += self.alphabet_to_morse[letter] + " "
                    

        return morse_code
        
        
    def morse_to_letters(self, morse):
        
        words = morse.split("|")
        complete_alpha_sentence = ""
        iterator = 0
        
        for word in words:
            char = word.split()
            print(char)
            for c in char:
                print(iterator)
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

