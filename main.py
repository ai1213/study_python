from manager import *
from client import *

bob = Manager()
adam = Client('adam')
adam.set_contact_point(bob.get_secretary())
adam.make_appointment('10:30')


charles = Client('charles')
charles.set_contact_point(bob.get_secretary())
charles.make_appointment('11:30')

dag = Client('dag')
dag.set_contact_point(bob.get_secretary())
dag.make_appointment('10:30')

bob.check_schedule()