#秘書クラス
import time

class Secretary:
  def __init__(self):
    self.logfile='_log.txt'
    self.appointment = {}

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

  #アポイントメントリクエスト
  def request_appointment(self,when,who):
    #その時間に予定があればfalse
    if(when in self.appointment):
      return False
    else:
      #なければアポを入れる
      self.appointment[when] = who
      return True

  def get_schedule(self):
    return str(self.appointment)


