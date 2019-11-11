import time

class Secretary:
  def __init__(self):
    self.logfile='_log.txt'

  def write_log(self,text):
    log='{}:{}\n'.format(time.ctime(),text)
    f = open(self.logfile,'a')
    f.write(log)
    f.close()
    
  def get_log(self):
    f = open(self.logfile,'r')
    log = f.read()
    f.close()
    return log




class Manager:
  def __init__(self):
    self.tom = Engineer()
    self.sara = Secretary()

  def work_a(self):
    self.sara.write_log("hello")
    time.sleep(5)
    self.sara.write_log("hey")
    

  def work_b(self):
    print(self.sara.get_log())
    

class Engineer:
  def add(self,a,b):
    return a+b
  
  def multiply(self,a,b):
    return a * b

bob = Manager()
bob.work_a()
bob.work_b()



