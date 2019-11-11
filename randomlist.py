import random


def get_random_list1(length):
  random_list = []
  for i in range(length):
    random_list.append(random.randint(0,100))
  return random_list


# mapを使った関数
def get_random_list2(length):
  return list(map(lambda x:random.randint(0,100), range(length)))

print(get_random_list1(10))
print(get_random_list2(10))
