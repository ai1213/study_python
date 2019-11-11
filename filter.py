
#-----------関数 + filter--------------
def is_even(x):
  return x % 2 == 0

filter_object = filter(is_even,range(10))

print(list(filter_object))

#-----------lambda + filter--------------
filter_object = filter(lambda x:x%2 == 0, range(10))

print(list(filter_object))
