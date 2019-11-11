import getch

KEY_CTL_C = 3

class Hero:
  def run(self):
    
    while(True):
      key = ord(getch.getch())
      if(key == KEY_CTL_C):
        print('bye!')
        break;

      print('key input:' + str(key))

hero = Hero()
hero.run()
    
