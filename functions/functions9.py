def even_Generator(limit):
   for i in  range(2,limit+1):
      yield i
print(even_Generator(10))