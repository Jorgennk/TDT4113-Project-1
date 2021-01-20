'''
pynput required for this test: pip3 install pynput

'''

from keyboard import key_to_scan_codes
import keyboard
from pynput.keyboard import Key, Controller
import time

import interpreter
#import press_interval

class morse_test:
    
    def __init__(self):
        self.time_list = [1.0, 0.0, 0.3, 0.3, 0.0, 0.3, 0.0]
        self.inter = interpreter.interpreter()
        self.button = Controller()
        

    def run(self):
        #morse_words = self.inter.translate_list(self.time_list)        
        #print(morse_words)
        time.sleep(3)
        self.button.press("a")
        time.sleep(0.4)

        self.button.press("a")
        time.sleep(0)
        
        self.button.press("a")
        time.sleep(0.1)
        self.button.press("a")
        time.sleep(0.1)
        self.button.press("a")
        time.sleep(0.6)
        
        self.button.press("x")
        


a = morse_test()
a.run()

#class morse_test:
#    
#    def __init__(self):
#        interval = press_interval.press_interval()
#        inter = interpreter.interpreter()
#    
#    def run_test(self):
        