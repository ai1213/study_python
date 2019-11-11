map_object = map(lambda x: x**2 , range(10))
print(list(map_object))

text_list = ['ab','cd','ef']
map_object = map(lambda x:x.upper(),text_list)

print(list(map_object))