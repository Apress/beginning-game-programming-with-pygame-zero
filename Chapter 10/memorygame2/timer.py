import math
import time

class Timer():
    
    def __init__(self, start_count):
        self.start_count = start_count
        self.start_time = time.time()
        
    # start count down, with optional parameter to replace the start_count value
    # -1 is used as a "magic number", this method should only be called with positive number
    # if it isn't given a number then -1 indicates no new time give
    def start_count_down(self, new_time = -1):
        if (new_time >= 0):
            self.start_count = new_time
        self.start_time = time.time()
        
    def get_time_remaining(self):
        current_time = self.start_count + self.start_time - time.time()
        if (current_time <= 0): 
            return 0
        return math.ceil(current_time)