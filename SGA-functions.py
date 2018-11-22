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
def initialize_strings(dimensions_v,bits,n):
  size=dimensions_v*bits
  string_pool = []

  while len(string_pool) < n:
    new_string=''
    for j in range(size):
      new_string=new_string+str(random.randint(0,1))
    
    if(new_string not in string_pool):
      string_pool.append(new_string)

  return string_pool

def select_mut_index(string1,size):
    turn = (random.randint(0,size-1))
    print(turn,"turn")
    bit=""
    if string1[turn]=="1":
        bit="0"
    else:
        bit="1"
    new_s=""
    if turn+1== size-1:
        new_s=string1[0:size-1]+bit
    else:
        new_s=string1[0:turn]+bit+string1[turn+1:]
    return new_s

def roulette(min_values):
    total_sum=0
    wieghts=[]
    
    for i in range(len(min_values)):
        total_sum=total_sum+min_values[i]
    
    for i in range(len(min_values)):
        temp=( (total_sum-min_values[i])/total_sum)/(len(min_values)-1)
        wieghts.append(temp)
    return wieghts
  
  def string_to_vector(pool,dim):
    vect=[]
    for i in pool:
        start=0
        temp= int(len(i)/dim)
        end= temp
        temp_l=[]
        for j in range (dim):
            temp_l.append(i[start:end])
            start=end
            end= end+temp   
        vect.append(temp_l)
    
    return vect     
def vect_to_real(vect, min_v,max_v,bits,prec):

    geneE=GeneEncoder(min_v,max_v,bits,prec)
    real_num=[]
    for j in vect:
        temp_l=[]
        for x in j:
            temp_l.append([geneE.binary_to_real(x)])
        real_num.append(temp_l)
    return real_num

dim=8
bits=15
min_v=-31
max_v=31
prec=2
pool=initialize_strings(dim,15,8)
print(pool)
vect=string_to_vector(pool,dim)
real_n=vect_to_real(vect,min_v,max_v,bits,prec)

for r in real_n:
    print(r)

