from intervaltree import IntervalTree
from encoder import *
from objective_functions import *
from new_of import *
from output import *
from datetime import datetime
import random
import math 

def init_of(o_func):
    """
    Given the type of objective function, return:
        - the number of bits used to encode each variable in the function
        - the minimum and maximum of the range of values

    For objective functions 13 to 30, the number of bits used for encoding
    will be 1 since the variables can only take -1 or 1 as value
    
    Parameters
    ----------
    o_func : int
        the type of objective function
    
    Returns
    -------
    mut_p : float
        mutation probability
    sub_bits : int
        number of bits used to encode each variable
    prec : int
        number of decimal points to keep for real values
    min_v : float
        the minimum in the range of possible values
    max_v : float
        the maximum in the range of values
    min_y : float
        the minimum in the range of possible values for the second variable in a 2D objective function
    max_y : float
        the maximum in the range of possible values for the second variable in a 2D objective function
    """

    sub_bits=15
    prec=2
    min_v=0
    max_v=0
    min_x=0
    min_y=0
    max_x=0
    max_y=0
    mut_p=0.001
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
        max_v=2*math.pi

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
    elif (o_func == 10):
        #10 init_six_hump_camel_back()
        min_y=-2
        max_y=2
        min_x=-3
        max_x=3
    elif (o_func==11):
        #11 init_xin_she_yang():
        min_v=-2*math.pi
        max_v=2*math.pi    
    #12 init_zakharov():
    elif (o_func ==12):
        min_v=0
        max_v=1
    elif (o_func >= 13) and (o_func <= 30):
        sub_bits = 1

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

def select_mut_index(string1,size,max_v,min_v,sub_bits,prec,discrete_mode):
    """
    Randomly flip a bit in the given binary string

    Parameters
    ----------
    string1 : str
        a binary string
    size : int
        the length of the binary string
    max_v : float
        the maximum value in the range of values
    min_v : float
        the minimum value in the range of values
    sub_bits : int
        number of bits used for encoding
    prec : int
        number of digits after decimal point to keep
    discrete_mode : boolean
        whether the possible values can only be integers (this is True for OF's 13 to 30)
    
    Returns
    -------
    the original string with a bit flipped in a random position
    """

    if not discrete_mode:
        binary_g=GeneEncoder(min_v,max_v,size,prec)
        val=binary_g.binary_to_gray(string1)
    else:
        val = string1

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
    
    if not discrete_mode:
        final_r= binary_g.gray_to_binary(new_s)
    else:
        final_r = new_s

    return final_r

def weights_tree(min_values, use_softmax = False):
    """
    Given the fitness values, calculate the probabilities of reproduction for each gene
    and return the IntervalTree that contains all of the probability intervals

    Parameters
    ----------
    min_values : list
        The list of fitness values
    use_softmax : boolean (default is False)
        Whether to use the softmax function to assign survival probabilities

    Returns
    -------
    An IntervalTree that contains all of the probability intervals
    """

    total_sum=0
    weights=[]
    tree = IntervalTree()

    if (not use_softmax):
        for i in range(len(min_values)):
            total_sum=total_sum+min_values[i]
        
        for i in range(len(min_values)):
            temp=( (total_sum-min_values[i])/total_sum)/(len(min_values)-1)
            weights.append(temp)
    else:
        shifted_values = []
        min_val = min(min_values)
        for val in min_values:
            shifted_values.append(val - min_val)

        for i in range(len(shifted_values)):
            total_sum = total_sum + math.exp(-1 * shifted_values[i])
        
        for i in range(len(shifted_values)):
            temp = math.exp(-1 * shifted_values[i]) / total_sum
            weights.append(temp)

    start = 0
    end = 0
    for i in range(len(min_values)):
        if weights[i] - 0 > 0.0000000001:
            end = start+weights[i]

            tree[start:end]= i
            start= end 

    return tree

def string_to_vector(pool,dim):
    """
    Given a list of binary string, split each string into a list of substrings,
    where each substring is the binary encoding of a variable in the OF

    Parameters
    ----------
    pool : list
        the list of all genes in the gene pool
    dim : int
        the dimension of the OF
    
    Returns
    -------
    A 2D list where each sub-list contains the binary encoding of a variable in the OF
    """

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

def objective_function(o_func,real_n,dim):
    """
    Calculate the fitness values using the given objective function

    Parameters
    ----------
    o_func : int
        the type of objective function to use
    real_n : list
        the values of each variable as real numbers
    dim : int
        the dimension of the function
    
    Returns
    -------
    A list of the fitness values
    """

    func_ptr = [ackley, de_jongs_sphere, easom, griewank, himmelblau, rastrigin, rosenbrock_var, rosenbrock_vec,
                schwefel, six_hump_camel_back, xin_she_yang, zakharov, f10, f11, f12, f13, f14, f15, f16, f17,
                f18, f19, f20, f21, f22, f23, f24, f25, f26, f27]
    min_values=[]
    chosen_func = func_ptr[o_func - 1]

    if (o_func >= 13) and (o_func <= 30):
        # Custom functions in new_of
        for i in range(len(real_n)):
            min_values.append(chosen_func(real_n[i]))
    elif o_func in [5, 7, 10]:
        # Himmelblau, Rosenbrock single and multi-variable
        for i in range(len(real_n)):
            min_values.append(chosen_func(real_n[i][0],real_n[i][1]))
    else:
        # The rest of the objective functions
        for i in range(len(real_n)):
            min_values.append(chosen_func(real_n[i],dim))
    
    return min_values

def vect_to_real(vect, min_v,max_v,sub_bits,prec):
    """
    Given a 2D list where each sublist contains binary encodings of the variables
    for each gene, convert the binary enconding into real values

    Parameters
    ----------
    vect : 2D-list
        the 2D-list of binary encodings
    min_v : float
        the minimum value in the range of values
    max_v : float
        the maximum value in the range of values
    sub_bits : int
        number of bits used for the encoding
    prec : int
        number of decimal points to keep
    
    Returns
    -------
    A 2D list where each sub-list contains the real values corresponding to each
    binary string
    """

    geneE=GeneEncoder(min_v,max_v,sub_bits,prec)
    real_num=[]
    for j in vect:
        temp_l=[]
        for x in j:
            temp_l.append(geneE.binary_to_real(x))
        real_num.append(temp_l)
    return real_num
    
def main():
    discrete_mode = False
    max_iteration= 10000
    min_values=[]
    pool_s= int (input("Enter the Pool size: "))
    names = ["init_ackley()", "init_de_jongs_sphere()", "init_easom()", "init_griewank()", "init_himmelblau()",
            "init_rastrigin()", "init_rosenbrock_var()", "init_rosenbrock_vec()",
            "init_schwefel()", "init_six_hump_camel_back()", "init_xin_she_yang()", "init_zakharov()",
            "init f10()", "init f11()", "init f12()", "init f13()", "init f14()", "init f15()",
            "init f16()", "init f17()", "init f18()", "init f19()", "init f20()", "init f21()",
            "init f22()", "init f23()", "init f24()", "init f25()", "init f26()", "init f27()"]
    for i in range(len(names)):
        print("{} {}".format(i+1, names[i]))

    o_func= int(input("Enter the number of the objective function you want to use: "))

    if (o_func == 5) or (o_func == 7) or (o_func == 10):
        dim = 2
    elif (o_func >= 13) and (o_func <= 30):
        discrete_mode = True
        dim = int( names[o_func - 1].lstrip("init f").rstrip("()") )
    else:
        dim=int(input("Enter the Objective Functions Dimensions: "))

    use_softmax = bool(input("Use softmax function to calculate survival probability (False by default): "))
    
    mut_p,sub_bits,prec,min_v,max_v,min_x,max_x,min_y,max_y = init_of(o_func)

    pool = initialize_strings(dim,sub_bits,pool_s)
    print(pool)
    print()
    
    best_obj_value = None
    best_gene = None
    avg_obj_value_per_gen = []
    min_obj_value_per_gen = []
    threshold = 0.0001
    max_no_change = 100
    no_change=0
    iteration=0
    print("Max iteration: {}".format(max_iteration))
    while no_change < max_no_change and iteration < max_iteration:
        print("Iteration: {}, best_obj_value: {}".format(iteration, best_obj_value))
        new_pool=[]

        real_n = []
        if discrete_mode:
            for i in range(pool_s):
                real_n.append(binary_to_bipolar(pool[i]))
        else:
            if (o_func==10 or o_func==5 or o_func==7):
                vect = string_to_vector(pool,2)
                real_n = vect_to_real(vect,min_v,max_v,(sub_bits*dim)//2,prec)
            else:
                vect = string_to_vector(pool,dim)
                real_n = vect_to_real(vect,min_v,max_v,sub_bits,prec)
        
        min_values=objective_function(o_func,real_n,dim)
        current_min_value = min(min_values)
        min_obj_value_per_gen.append(current_min_value)
        avg_obj_value_per_gen.append(sum(min_values) / pool_s)

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
        tree= weights_tree(min_values, use_softmax)    

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

        # mutation
        for i in range(pool_s):
            prob = random.random()
            if (prob <= mut_p ):
                temp=pool[i]
                pool[i]=select_mut_index(temp,(sub_bits*dim),max_v,min_v,sub_bits,prec, discrete_mode)

        iteration+=1 

        print()

    print("Best objective value found: {:.3f}".format(best_obj_value))
    print("Best input values found:")
    print(best_gene)
    print()
    print("The algorithm stopped after {} iterations".format(iteration))
    print("Reason for stopping: ", end = "")

    stop_reason = ""
    if iteration == max_iteration:
        stop_reason = "maximum number of iteration reached"
    else:
        stop_reason = "stopped early because the best objective value only changes slightly after {} iterations".format(max_no_change)
    print(stop_reason)

    current_time = datetime.now()
    plot_line_graph([i for i in range(iteration)], avg_obj_value_per_gen, "Generation", "Average fitness value",\
                    "Average fitness value per generation", current_time)
    
    plot_line_graph([i for i in range(iteration)], [math.log10(i + 0.0001) for i in avg_obj_value_per_gen], "Generation", "log(Average fitness value)",\
                    "log(Average fitness value) per generation", current_time)
    
    plot_line_graph([i for i in range(iteration)], min_obj_value_per_gen, "Generation", "Minimum fitness value",\
                    "Minimum fitness value per generation", current_time)
    
    plot_line_graph([i for i in range(iteration)], [math.log10(i + 0.0001) for i in min_obj_value_per_gen], "Generation", "log(Minimum fitness value)",\
                    "log(Minimum fitness value) per generation", current_time)

    result_dict = {
        "obj_func" : o_func,
        "obj_dimen" : dim,
        "pool_size" : pool_s,
        "mutate_prob" : mut_p,
        "max_iter" : max_iteration,
        "best_obj_value" : best_obj_value,
        "best_gene": best_gene,
        "stop_iter" : iteration,
        "stop_reason" : stop_reason
    }
    save_result_to_file(result_dict, current_time)

    return 

main()