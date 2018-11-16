import objective_functions as of
import math

#ackley(x,n)
x1 = [1,1,0,1,1,1,1,1]
x2 = [0,0,0,0,0,0,0,0]
n = len(x1)
print("The result of Ackley's function on {} is {}".format(x1,of.ackley(x1,n)))
print("The result of Ackley's function on {} is {} and is minimal".format(x2,of.ackley(x2,n)))

#de_jong(x,n)
x1 = [1,1,0,1,1,1,1,1]
x2 = [0,0,0,0,0,0,0,0]
n = len(x1)
print("The result of De Jong's sphere on {} is {}".format(x1,of.de_jongs_sphere(x1,n)))
print("The result of De Jong's sphere on {} is {} and is minimal".format(x2,of.de_jongs_sphere(x2,n)))

#easom(x,n)
x1 = [1,1,0,1,1,1,1,1]
x2 = [math.pi,math.pi,math.pi,math.pi,math.pi,math.pi,math.pi,math.pi]
n = len(x1)
print("The result of Easom's function on {} is {}".format(x1,of.easom(x1,n)))
print("The result of Easom's function on {} is {} and is minimal".format(x2,of.easom(x2,n)))

#griewank(x,n)
x1 = [1,1,0,1,1,1,1,1]
x2 = [0,0,0,0,0,0,0,0]
n = len(x1)
print("The result of Griewank function on {} is {}".format(x1,of.griewank(x1,n)))
print("The result of Griewank function on {} is {} and is minimal".format(x2,of.griewank(x2,n)))

#himmelblau(x,y)
x1 = 1
y1 = 2
x2 = 3
y2 = 2

print("The result of Himmelblau's function on x= {} and y= {} is {}".format(x1,y2,of.himmelblau(x1,y1)))
print("The result of Himmelblau's function on x= {} and y= {} is {} and is minimal".format(x2,y2,of.himmelblau(x2,y2)))

#rastrigin(x,n)
x1 = [1,1,0,1,1,1,1,1]
x2 = [0,0,0,0,0,0,0,0]
n = len(x1)
print("The result of Rastrigin's function on {} is {}".format(x1,of.rastrigin(x1,n)))
print("The result of Rastrigin's function on {} is {} and is minimal".format(x2,of.rastrigin(x2,n)))

#rosenbrock_var(x,y)
x1 = 4
y1 = 2
x2 = 1
y2 = 1
print("The result of Rosenbrock's function on x= {} and y= {} is {}".format(x1,y1,of.rosenbrock_var(x1,y1)))
print("The result of Rosenbrock's function on x= {} and y= {} is {} and is minimal".format(x2,y2,of.rosenbrock_var(x2,y2)))

#rosenbrock_vec(x,y)
x1 = [1,1,0,1,1,1,1,1]
x2 = [1,1,1,1,1,1,1,1]
n = len(x1)
print("The result of Rosenbrock's function on {} is {}".format(x1,of.rosenbrock_vec(x1,n)))
print("The result of Rosenbrock's function on {} is {} and is minimal".format(x2,of.rosenbrock_vec(x2,n)))

#schwefel(x, n)
x1 = [1,1,0,1,1,1,1,1]
x2 = [0,0,0,0,0,0,0,0]
n = len(x1)
print("The result of Schwefel's Function on {} is {}".format(x1,of.schwefel(x1, n)))
print("The result of Schwefel's Function on {} is {} and is minimal".format(x2,of.schwefel(x2, n)))

#six_hump_camel_back(x,y)
x1 = 1
y1 = 1
x2 = 0.0898
y2 = -0.7126

print("The result of Six-Hump Camel Back Function on x= {} and y= {} is {}".format(x1,y1,of.six_hump_camel_back(x1,y1)))
print("The result of Six-Hump Camel Back Function on x= {} and y= {} is {} and is minimal".format(x2,y2,of.six_hump_camel_back(x2,y2)))

#xin_she_yang(x,n)
x1 = [1,1,0,1,1,1,1,1]
x2 = [0,0,0,0,0,0,0,0]
n = len(x1)
print("The result of Xin-She Yang's function on {} is {}".format(x1,of.xin_she_yang(x1,n)))
print("The result of Xin-She Yang's function on {} is {} and is minimal".format(x2,of.xin_she_yang(x2,n)))

#zakharov(x,n)
x1 = [1,1,0,1,1,1,1,1]
x2 = [0,0,0,0,0,0,0,0]
n = len(x1)
print("The result of Zakharov's function on {} is {}".format(x1,of.zakharov(x1,n)))
print("The result of Zakharov's function on {} is {} and is minimal".format(x2,of.zakharov(x2,n)))
