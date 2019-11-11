#フレームワーク(手を加えない)
class Calc:
  #初期化でカスタマイズ用の関数定義を受け取り登録する
  def __init__(self,operation_list):
    self.operation_dict = {}
    for operation_tuple in operation_list:
      (operation,method) = operation_tuple
      self.operation_dict[operation] = method

  def run(self):
    while True:
      print('please input your calcuration')
      input_text = input()
      words = input_text.split()
      print(self.operation_dict)
      if words[0] == 'exit':
        return

      if len(words) < 3:
        print("len(words) < 3")
        continue

      if words[0] not in self.operation_dict:
        print("not in ")
        continue

      #カスタマイズされた関数を呼び出す
      print(words)
      fun = self.operation_dict[words[0]]
      print(type(fun))

      print(fun(int(words[1]), int(words[2])) )

def add(a,b):
  return a+b
def decrease(a,b):
  return a-b

calc = Calc([("plus",add),("decrease",decrease)])

calc.run()
