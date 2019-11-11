import functools,random

#２値を比較して条件に合致したほうの値を返す（今回は大きいほう)
def get_bigger(a,b):
  if(a>b):
    return a
  else:
    return b

#ランダムな数値をリストに詰める
random_list =[]
for i in range(10):
  random_list.append(random.randint(0,100))

#リストの中で最も条件に合致する要素を返す
biggest = functools.reduce(get_bigger,random_list)

print('list:{}'.format(random_list))
print('biggest:{}'.format(biggest))
