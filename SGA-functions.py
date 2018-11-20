import random

# stringOne and stringTwo are the strings that need to perform a crossover
# how many bits the strings have
# a random position is generated
# crossover is performed at the position
# returns the two new strings
def performCrossover(stringOne, stringTwo, length):
  posToCross = random.randint(0,length-1)

  temp=stringOne[posToCross:]
  stringOne = stringOne[:posToCross] + stringTwo[posToCross:]
  stringTwo = stringTwo[:posToCross] + temp

  return stringOne,stringTwo


# length - how many bits the strings will have
# n - how many strings to create
# this function randomly initalizes the bits of the initial generation
# returns the initial pool
def initialize_strings(length, n):

  string_pool = []

  while len(string_pool) < n:
    new_string=''
    for j in range(length):
      new_string=new_string+str(random.randint(0,1))
    
    if(new_string not in string_pool):
      string_pool.append(new_string)

  return string_pool
