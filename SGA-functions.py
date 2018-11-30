from intervaltree import IntervalTree
from encoder import GeneEncoder
from objective_functions import *
import random
import math 
# stringOne and stringTwo are the strings that need to perform a crossover
# how many bits the strings have
# a random position is generated
# crossover is performed at the position
# returns the two new strings
def init_of(o_func):
    sub_bits=15
    prec=2
    min_v=0
    max_v=0
    min_x=0
    min_y=0
    max_x=0
    max_y=0
    mut_p=0.01
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
            max_v=3.8
        elif (o_func ==6):
            #6 init_rastrigin():
            min_v=-5.12
            max_v=5.12
        elif (o_func ==7):
            #7 init_rosenbrock_var():
            min_v=-2.048
            max_v=2.048
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
            min_v=-2*math.pi
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
def performCrossover(stringOne, stringTwo, length):
  posToCross = random.randint(0,length-1)

  temp=stringOne[posToCross:]
  stringOne = stringOne[:posToCross] + stringTwo[posToCross:]
  stringTwo = stringTwo[:posToCross] + temp

  return stringOne,stringTwo

def crossover_multivar(gene_1, gene_2, length):
    posToCross = random.randint(0,length-1)

    new_gene_1 = []
    new_gene_2 = []
    for subgene_1, subgene_2 in zip(gene_1, gene_2):
        temp = subgene_1[posToCross:]
        stringOne = subgene_1[:posToCross] + subgene_2[posToCross:]
        stringTwo = subgene_2[:posToCross] + temp

        new_gene_1.append(stringOne)
        new_gene_2.append(stringTwo)
        
    return new_gene_1, new_gene_2

# length - how many bits the strings will have
# n - how many strings to create
# this function randomly initalizes the bits of the initial generation
# returns the initial pool
def initialize_strings(dimensions_v,bits,n):
    #size = int(dimensions_v*(math.ceil(math.log(length_r,2))))
    size=dimensions_v*bits
    string_pool = []
    print(size)
    while len(string_pool) < n:
        new_string=''
        for j in range(size):
            new_string=new_string+str(random.randint(0,1))
    
        if(new_string not in string_pool):
            string_pool.append(new_string)
    return string_pool

def initialize_strings_no_concat(dimensions_v,bits,n):
    #size = int(dimensions_v*(math.ceil(math.log(length_r,2))))
    string_pool = []
    print("Number of variables: {}".format(dimensions_v))
    while len(string_pool) < n:
        new_gene = []
        for j in range(dimensions_v):
            new_string=''
            for i in range(bits):
                new_string=new_string+str(random.randint(0,1))
            new_gene.append(new_string)
    
        if(new_gene not in string_pool):
            string_pool.append(new_gene)
    return string_pool

def select_mut_index(string1,size,max_v,min_v,sub_bits,prec):
    binary_g=GeneEncoder(min_v,max_v,size,prec)
    val=binary_g.binary_to_gray(string1)
    turn = (random.randint(0,size-1))
    
    bit=""
    if val[turn]=="1":
        bit="0"
    else:
        bit="1"
    new_s=""
    if turn+1== size:
        new_s=val[0:size-1]+bit
    else:
        new_s=val[0:turn]+bit+val[turn+1:]
    final_r= binary_g.gray_to_binary(new_s)

    return final_r

def mutate_multi_var(gene, max_v, min_v, sub_bits, prec):
    binary_g = GeneEncoder(min_v, max_v, sub_bits, prec)
    subgene_index = random.randint(0, len(gene)-1)
    
    val = binary_g.binary_to_gray(gene[subgene_index])
    turn = (random.randint(0, sub_bits-1))
    bit = ""
    if val[turn] == "1":
        bit="0"
    else:
        bit="1"

    new_s = ""
    if turn+1 == sub_bits:
        new_s = val[0:sub_bits-1] + bit
    else:
        new_s = val[0:turn] + bit + val[turn+1:]

    gene[subgene_index] = binary_g.gray_to_binary(new_s)

    return gene

def weights_tree(min_values):
    total_sum=0
    weights=[]
    tree = IntervalTree()

    # for i in range(len(min_values)):
    #     total_sum=total_sum+min_values[i]
    
    # for i in range(len(min_values)):
    #     temp=( (total_sum-min_values[i])/total_sum)/(len(min_values)-1)
    #     weights.append(temp)

    shifted_values = []
    max_val = min(min_values)
    for val in min_values:
        shifted_values.append(val - max_val)

    for i in range(len(shifted_values)):
        total_sum = total_sum + math.exp(-1 * shifted_values[i])
    
    for i in range(len(shifted_values)):
        temp = math.exp(-1 * shifted_values[i]) / total_sum
        weights.append(temp)

    start= 0
    end =0
    for i in range(len(min_values)):
        if weights[i] - 0 > 0.0000000001:
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
    
    if (o_func ==1):
         #1 init_ackley():
        for i in range(len(real_n)):
            # print(real_n[i],"real_n[i]")
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
    elif (o_func ==5):
        #5 init_himmelblau():
        for i in range(len(real_n)):
            min_values.append(himmelblau(real_n[i][0],real_n[i][1]))
    elif (o_func ==6):
        #6 init_rastrigin():
        for i in range(len(real_n)):
            min_values.append(rastrigin(real_n[i],dim))
    elif (o_func ==7):
            #7 init_rosenbrock_var():
        for i in range(len(real_n)):
            min_values.append(rosenbrock_var(real_n[i][0],real_n[i][1]))
            
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
    
    else:
        #10 init_six_hump_camel_back()
        for i in range(len(real_n)):
            min_values.append(six_hump_camel_back(real_n[0],real_n[1]))
    

    return min_values
def vect_to_real(vect, min_v,max_v,sub_bits,prec):
    geneE=GeneEncoder(min_v,max_v,sub_bits,prec)
    real_num=[]
    for j in vect:
        temp_l=[]
        for x in j:
            temp_l.append(geneE.binary_to_real(x))
        real_num.append(temp_l)
    return real_num
def main():
    #dim =8
    max_iteration= 10000
    min_values=[]
    pool_s= int (input("Enter the Pool size: "))
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
    o_func= int(input("Enter the number of the objective function you want to use: "))

    if (o_func == 5) or (o_func == 7):
        # TODO: Determine what this should be after
        dim = 2
    else:
        dim=int(input("Enter the Obective Functions Dimensions: "))

    mut_p,sub_bits,prec,min_v,max_v,min_x,max_x,min_y,max_y = init_of(o_func)
    # pool=initialize_strings_no_concat(dim,sub_bits,pool_s)
    pool = initialize_strings(dim,sub_bits,pool_s)
    print(pool)
    print()
    
    best_obj_value = None
    best_gene = None
    threshold = 0.0001
    max_no_change = 100
    no_change=0
    iteration=0
    print("Max iteration: {}".format(max_iteration))
    while no_change < max_no_change and iteration < max_iteration:
        print("Iteration: {}, best_obj_value: {}".format(iteration, best_obj_value))
        new_pool=[]

        if (o_func==10 or o_func==5 or o_func==7 ):
            vect= string_to_vector(pool,2)
            real_n=vect_to_real(vect,min_v,max_v,(sub_bits*dim)//2,prec)
        else:
            vect=string_to_vector(pool,dim)
            real_n=vect_to_real(vect,min_v,max_v,sub_bits,prec)
        
        # real_n = vect_to_real(pool, min_v, max_v, sub_bits, prec)

        min_values=obective_function(o_func,real_n,dim)
        current_min_value = min(min_values)
        print("Iteration min value: {}".format(current_min_value))

        if best_obj_value is None:
            best_obj_value = current_min_value
            best_val_index = min_values.index(best_obj_value)
            best_gene = real_n[best_val_index]
        elif abs(best_obj_value - current_min_value) < threshold or current_min_value > best_obj_value:
            no_change += 1
        else:
            best_obj_value = current_min_value
            best_val_index = min_values.index(best_obj_value)
            best_gene = real_n[best_val_index]
            no_change = 0

        # calling function to do interval tree to find 
        tree= weights_tree(min_values)    

        index_of_temp_pool=[]
        for i in range(pool_s):
            index_s1= random.random()
            get_index=list(tree.search(index_s1))[0]
            index_of_temp_pool.append(get_index[2])

        # crossover 
        for c in range(pool_s//2):
            a= random.randint(0,len(index_of_temp_pool)-1)

            string_1=pool[index_of_temp_pool.pop(a)]
            b=random.randint(0,len(index_of_temp_pool)-1)
            string_2=pool[index_of_temp_pool.pop(b)]

            temp1,temp2=performCrossover(string_1,string_2, len(string_1))
            new_pool.append(temp1)
            new_pool.append(temp2)
        pool=new_pool

        # for c in range(pool_s // 2):
        #     a = random.randint(0,len(index_of_temp_pool)-1)
        #     gene_1 = pool[index_of_temp_pool.pop(a)]

        #     b = random.randint(0,len(index_of_temp_pool)-1)
        #     gene_2 = pool[index_of_temp_pool.pop(b)]

        #     temp1,temp2 = crossover_multivar(gene_1, gene_2, len(gene_1[0]))
        #     new_pool.append(temp1)
        #     new_pool.append(temp2)

        # pool=new_pool

        # mutation
        for i in range(pool_s):
            prob = random.random()
            if (prob <= mut_p ):
                temp=pool[i]
                pool[i]=select_mut_index(temp,(sub_bits*dim),max_v,min_v,sub_bits,prec)

        # for i in range(pool_s):
        #     prob = random.random()
        #     if (prob <= mut_p) :
        #         pool[i] = mutate_multi_var(pool[i], max_v, min_v, sub_bits, prec)

        iteration+=1 

        print()

    print("Best objective value found: {:.3f}".format(best_obj_value))
    print("Best input values found:")
    print(best_gene)
    print()
    print("The algorithm stopped after {} iterations".format(iteration))
    print("Reason for stopping: ", end = "")

    if iteration == max_iteration:
        print("maximum number of iteration reached")
    else:
        print("stopped early because the best objective value only changes slightly after {} iterations".format(max_no_change))

    return 

main()