'''
Simple stopwatch class to take the time something takes, pretty self explanatory 

'''

import time

class simple_stopwatch:
    
    def __init__(self):
        self.start_time = 0
        self.end_time = 0
        pass

    def interval(self):
        new_interval = time.time()
        input("fjkeo: ")
        diff = time.time() - new_interval
        #print(diff)
        return diff
    
    #Start the timer    
    def start(self):
        self.start_time = time.time()
        
    #Stop the timer
    def stop(self):
        
        self.end_time = time.time()
        
        diff = round(self.end_time - self.start_time, 4)
        #print("Difference on interval: ", diff)
        
        return diff