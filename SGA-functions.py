from intervaltree import IntervalTree
from GE import GeneEncoder
from OF import *
import random
def init_of(o_func):
    sub_bits=15
    prec=2
    min_v=0
    max_v=0
    min_x=0
    min_y=0
    max_x=0
    max_y=0
    mut_p=0.06
    if (o_func !=10): 
        if (o_func ==1):
            #1 init_ackley():
            min_v=-(5.12)
            max_v=(5.12)
        elif (o_func ==2):
            #2 init_de_jongs_sphere():
            min_v=-(5.12)
            max_v=(5.12)
    
        elif (o_func ==3):
            #3 init_easom():
            min_v=-2*math.pi
            ax_v=2*math.pi

        elif(o_func==4):
            #4 init_griewank():
            min_v=-600
            max_v=600
        elif (o_func ==5):
            #5 init_himmelblau():
            min_v=-3.8
            max_v=3.6
        elif (o_func ==6):
            #6 init_rastrigin():
            min_v=-5.12
            max_v=5.12
        elif (o_func ==7):
            #7 init_rosenbrock_var():
            min_v=0
            max_v=2
        elif (o_func ==8):
            #8 init_rosenbrock_vec():
            min_v=-2.048
            max_v=2.048
        elif (o_func ==9):
            #9 init_schwefel():
            min_v=-65.536
            max_v=65.536    
        elif (o_func==11):
            #11 init_xin_she_yang():
            min_v=-2*mathi.pi
            max_v=2*math.pi    
        #12 init_zakharov():
        elif (o_func ==12):
            min_v=0
            max_v=1
    else:
        #10 init_six_hump_camel_back()
        min_y=-2
        max_y=2
        min_x=-3
        max_x=3

    return mut_p,sub_bits,prec,min_v,max_v,min_x,max_x,min_y,max_y
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

def select_mut_index(string1,size,max_v,min_v,sub_bits,prec):
    binary_g=GeneEncoder(min_v,max_v,sub_bits,prec)
    val=binary_g.binary_to_gray(string1)
    turn = (random.randint(0,size-1))
    print(turn,"turn")
    bit=""
    if val[turn]=="1":
        bit="0"
    else:
        bit="1"
    new_s=""
    if turn+1== size-1:
        new_s=val[0:size-1]+bit
    else:
        new_s=val[0:turn]+bit+val[turn+1:]
    
    final_r= binary_g.gray_to_binary(string1)
    return final_r
def roulette(min_values):
    total_sum=0
    wieghts=[]
    
    for i in range(len(min_values)):
        total_sum=total_sum+min_values[i]
    
    for i in range(len(min_values)):
        temp=( (total_sum-min_values[i])/total_sum)/(len(min_values)-1)
        wieghts.append(temp)
    return wieght
  def weights_tree(min_values):
    total_sum=0
    weights=[]
    tree = IntervalTree()

    for i in range(len(min_values)):
        total_sum=total_sum+min_values[i]
    
    for i in range(len(min_values)):
        temp=( (total_sum-min_values[i])/total_sum)/(len(min_values)-1)
        weights.append(temp)

    start= 0
    end =0
    for i in range(len(min_values)):
        end = start+weights[i]

        tree[start:end]= i
        start= end 

    return tree
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
def obective_function(o_func,real_n,dim):
    min_values=[]
    if (o_func !=10):
        if (o_func ==1):
            #1 init_ackley():
            for i in range(len(real_n)):
                
                min_values.append(ackley(real_n[i],dim))

        elif (o_func ==2):
            #2 init_de_jongs_sphere():
            for i in range(len(real_n)):
                min_values.append(de_jongs_sphere(real_n[i],dim))  
        elif (o_func ==3):
            #3 init_easom():
            for i in range(len(real_n)):
                min_values.append(easom(real_n[i],dim))

        elif(o_func ==4):
            #4 init_griewank():
            for i in range(len(real_n)):
                min_values.append(griewank(real_n[i],dim))
        elif (o_func ==6):
            #6 init_rastrigin():
            for i in range(len(real_n)):
                min_values.append(rastrigin(real_n[i],dim))
        #elif (o_func !=7):
            #7 init_rosenbrock_var():
            #x,y - two real-valued variables
            #min at a,a^2 = 0
            #def rosenbrock_var(x,y):
            #a & b are parameters of the function
            #a = 1
            #b = 100
            #result = (a - x)**2 + b*(y-x**2)**2
            #return result
            
        elif (o_func ==8):
            #8 init_rosenbrock_vec():
            for i in range(len(real_n)):
                min_values.append(rosenbrock_vec(real_n[i],dim))
        elif (o_func ==9):
            #9 init_schwefel():
            for i in range(len(real_n)):
                min_values.append(schwefel(real_n[i],dim))
        elif (o_func ==11):
            #11 init_xin_she_yang():
            for i in range(len(real_n)):
                min_values.append(xin_she_yang(real_n[i],dim))   
        #12 init_zakharov():
        elif (o_func ==12):
            for i in range(len(real_n)):
                min_values.append(zakharov(real_n[i],dim))
    #elif (o_func !=5):
        #5 init_himmelblau():
        #x,y - two real-valued variables
        #mins at:
        #f(3.0,2.0)=0
        #f(-2.805118,3.131312)=0
        #f(-3.779310,-3.283186)=0
        #f(3.584428,-1.848126)=0
        #def himmelblau(x,y):
    #    result = (x**2 + y - 11)**2 + (x + y**2-7)**2
    #    return result
    #    continue
    #else:
        #10 init_six_hump_camel_back()
    
    #    continue

    return min_values
  
def vect_to_real(vect, min_v,max_v,bits,prec):

    geneE=GeneEncoder(min_v,max_v,bits,prec)
    real_num=[]
    for j in vect:
        temp_l=[]
        for x in j:
            temp_l.append([geneE.binary_to_real(x)])
        real_num.append(temp_l)
    return real_num

def main():
    #dim =8
    min_values=[]
    pool_s= int (input("Enter the Pool size:"))
    print("1 init_ackley()")
    print("2 init_de_jongs_sphere()")
    print("3 init_easom()")
    print("4 init_griewank()")
    print("5 init_himmelblau()")
    print("6 init_rastrigin()")
    print("7 init_rosenbrock_var()")
    print("8 init_rosenbrock_vec()")
    print("9 init_schwefel()")
    print("10 init_six_hump_camel_back()")
    print("11 init_xin_she_yang()")
    print("12 init_zakharov()")
    o_func= int(input("Enter the number of the objective function you want to use:"))
    dim=int(input("Enter the Obective Functions Dimensions:"))

    mut_p,sub_bits,prec,min_v,max_v,min_x,max_x,min_y,max_y = init_of(o_func)

    pool=initialize_strings(dim,sub_bits,8)
    print(pool)
    
    #no_change=0
    #while no_change!=3:
    vect=string_to_vector(pool,dim)
    real_n=vect_to_real(vect,min_v,max_v,sub_bits,prec)
    min_values=obective_function(o_func,real_n,dim)    
    # calling function to do interval tree to find 
    tree= weights_tree(min_values)    
    # crossover 
    for c in range(pool_s/2):
        index_s1= random.random()
        index_s2=random.random()
        a = list(tree.search(index_s1))[0]
        b= list(tree.search(index_s2))[0]
        string_1=pool[a[2]]
        string_2=pool[b[2]]
    
        pool[a[2]],pool[b[2]]=performCrossover(string_1,string_2, len(string_1))
    # mutation
    for i in range(pool_s):
        prob = random.random()
        if (prob <= mut_p):
            c = list(tree.search(i))[0]
            mut_string=pool[c[2]]
            pool[c[2]]=select_mut_index(mut_string,len(mut_string),max_v,min_v,sub_bits,prec)
    print(pool)
    return 
main()
