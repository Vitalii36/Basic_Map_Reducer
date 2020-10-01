import string
from map_reducer import map_reduce

def remove_punctuation(s):
  return s.translate([str.maketrans(',',' '), string.punctuation])

def mapper(input_key,input_value):
  return [(word,1) for word in
          remove_punctuation(input_value.lower()).split()]

def reducer(intermediate_key,intermediate_value_list):
  return (intermediate_key,sum(intermediate_value_list))

filenames = ["text/a.txt","text/b.txt","text/c.txt"]
i = {}

for filename in filenames:
  f = open(filename)
  i[filename] = f.read()
  f.close()

print(map_reduce(i,mapper,reducer))