class TestPrivate:
  def __init__(self):
    self.var1 = 'var1'
    self.__var2 = 'var2' #Private


  def method1(self):
    print('method1')

  def __method2(self):# private
    print('method2')

  def method3(self):
    print(self.var1)
    print(self.__var2)
    self.method1()
    self.__method2()


instance = TestPrivate()
print(instance.var1)
#print(instance.__var2)

instance.method1()
#instance.method2()

instance.method3()