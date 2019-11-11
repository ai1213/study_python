my_print = lambda x:print("my_print:{}".format(x))
my_print("hello")


funcs = {(lambda x,y:x+y),(lambda x,y:x-y),(lambda x,y:x*y),(lambda x,y:x**y)}

for fun in funcs:
  print(fun(5,10))

