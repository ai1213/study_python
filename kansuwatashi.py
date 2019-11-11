#関数を呼び出す関数(高階関数)
def fun1(fun,text):
  fun(text)

def fun2(text):
  print('fun2:' + text)

#高階関数に関数を渡して利用
fun1(fun2,'hello')

