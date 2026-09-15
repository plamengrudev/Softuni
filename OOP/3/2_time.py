class Time:
    max_hours=23
    max_minutes=59
    max_seconds=59

    def __init__(self,hours: int, minutes: int, seconds: int):
        self.hours=hours
        self.minutes=minutes
        self.seconds=seconds

    def set_time(self,hours: int, minutes: int, seconds: int):
        if self.hours <= Time.max_hours and self.minutes<=Time.max_minutes and self.hours<=Time.max_seconds:
            self.hours=hours
            self.minutes=minutes
            self.seconds=seconds
    
    def get_time(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'
    
    def next_second(self):
        self.seconds+=1
        if self.seconds>Time.max_seconds:
            new_min=self.seconds//60
            self.seconds%=60
            self.minutes+=new_min
        if self.minutes>Time.max_minutes:
            new_hour=self.minutes//60
            self.minutes%=60
            self.hours+=new_hour
        if self.hours>Time.max_hours:
            self.hours%=24
        return self.get_time()


time = Time(23, 59, 59)
print(time.next_second())