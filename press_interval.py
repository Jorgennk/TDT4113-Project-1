import keyboard
import simple_stopwatch


class press_interval:
    
    
    #Constructor, takes in the character you want to time on the keyboard
    #Normally this will be set to space for morse code on keyboard
    def __init__(self, keyboard_char):
        self.timer = simple_stopwatch.simple_stopwatch()
        self.time_list = []
         

        self.keyboard_char = keyboard_char

    def press_checker(self):
        timer_started = False
        continue_loop = True
        timer_started = False
                
        while continue_loop:
            press_check = False
            
            
            if keyboard.is_pressed(self.keyboard_char):
                #print(self.keyboard_char, " is pressed")
                if not timer_started:
                    self.timer.start()
                    timer_started = True
            
                press_check = True

            if timer_started and not press_check:
                continue_loop = False
        
        
        time_pressed = self.timer.stop()
        print("Time pressed: ", time_pressed)
        
        return time_pressed
        
        
        
    def pause_timer(self, time_list):
        self.timer.start()
        continue_pause_loop = True
        
        while continue_pause_loop:
            
            if keyboard.is_pressed("x"):
                self.timer.stop()
                return False
            
            if keyboard.is_pressed(self.keyboard_char):
                pause_time = self.timer.stop()
                time_list.append(pause_time)
                print("Paused: ", pause_time)
                continue_pause_loop = False

        return True
        
    #def pause_checker(self, time_list):
    #    self.timer.start()
    #    continue_pause_loop = True
    #    
    #    
    #    while continue_pause_loop:
    #        
    #        #if keyboard.is_pressed("x"):
    #        #    self.timer.stop()
    #        #    print("set to false")
    #        #    return False
    #        
    #        if keyboard.is_pressed(self.keyboard_char):
    #            #continue_loop = False
    #            pause_time = self.timer.stop()
    #            time_list.append(pause_time)
    #            print("Paused: ", pause_time)
    #            print("Set to true")
    #    
    #    return True
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    def pause_checker(self, time_list):
        self.timer.start()
        continue_loop = True
        pause_time = 0
        interupt = False
        
        while continue_loop:
            
            if keyboard.is_pressed(self.keyboard_char):
                interupt = True
                continue_loop = False

            if interupt:
                pause_time = self.timer.stop()
                self.time_list.append(pause_time)
                print("Time paused: ", pause_time)