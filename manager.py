import time
from secretary import *


class Manager:
  def __init__(self):
    
    self.sara = Secretary()

  def work_a(self):
    self.sara.write_log("hello")
    time.sleep(5)
    self.sara.write_log("hey")
    

  def work_b(self):
    print(self.sara.get_log())

  def check_schedule(self):
    schedule = self.sara.get_schedule()
    print(schedule)

  def get_secretary(self):
    return self.sara
    

