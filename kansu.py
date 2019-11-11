def test():
  return 1


print('call test:{}'.format(test()))

print('time test: {}'.format(type(test)))

test2 = test

print('call test2:{}'.format(test2()))
print('type test2:{}'.format(type(test2)))
