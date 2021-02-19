import time

class Timer:

    def __init__(self, expiration_time):
        self.expiration_time = expiration_time
        # sets the starting time
        self.start_time = round(time.time())

    def update(self):
        while True:
            time_now = round(time.time())
            # sets the delta between the current time and the starting time
            delta_time = time_now - self.start_time
            # if the delta is equal to the set expiration time the method returns True
            if delta_time == self.expiration_time:
                break
        return True