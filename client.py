class Client:
  def __init__(self,name):
    self.name = name
    self.contact_point=None
  
  def set_contact_point(self,contact_point):
    self.contact_point = contact_point

  def make_appointment(self,when):
    if(self.contact_point):
      is_success = self.contact_point.request_appointment(when,self.name)

    print(self.name + " could book?:" + str(is_success))

    