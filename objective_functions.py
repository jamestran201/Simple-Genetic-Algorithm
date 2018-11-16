import math

#x - vector, -30 ≤ x[i] ≤ 30
#n - size of vector
#total - result of the function
#min at 00000...0000 = 0
def ackley(x,n):
    part1 = 0
    part2 = 0
    for i in range(n):
        val = x[i]
        part1+=val**2
        part2+= math.cos(math.pi*2*val)
    result = -20 * math.exp(-(1 / 5) * math.sqrt((1 / n) * part1)) - math.exp((1/n) * part2) + 20 + math.e
    return result

#x - vector of reals -(5.12) ≤ x[i] ≤ (5.12)
#n - size of the vector
#total - result of the function
#min at 000000...0 = 0
def de_jongs_sphere(x,n):
    total = 0
    for i in range(n):
        val = x[i]
        total += val**2
    return total

#x - vector of reals -(2pi) ≤ x[i] ≤ (2pi)
#n - size of the vector
#total - result of the function
#min at (pi,pi,pi,...,pi) = -1
def easom(x,n):
    part1 = 0
    part2 = 0
    for i in range (n):
        val = x[i]
        if i == 0:
            part1 += (math.cos(val))**2
        else:
            part1 *= (math.cos(val))**2
        part2 += (val - math.pi)**2
    result = (-(-1)**n) * part1 * math.exp(-part2)
    return result

#x - vector of reals −600 ≤ x[i] ≤ 600
#n - size of the vector
#total - result of the function
#min at 000000...0 = 0
def griewank(x,n):
    part1 = 0
    part2 = 0
    for i in range(1,n+1):
        val = x[i-1]
        part1 += val**2
        if i==0:
            part2 += math.cos(val/math.sqrt(i+1))
        else:
            part2 *= math.cos(val/math.sqrt(i+1))
    result = (1 / 4000) * part1 - part2 + 1
    return result

#x,y - two real-valued variables
#mins at:
#f(3.0,2.0)=0
#f(-2.805118,3.131312)=0
#f(-3.779310,-3.283186)=0
#f(3.584428,-1.848126)=0
def himmelblau(x,y):
    result = (x**2 + y - 11)**2 + (x + y**2-7)**2
    return result

#x - vector of reals -5.12 ≤ x[i] ≤ 5.12
#n - size of vector
#min at 111111...11 = 0
def rastrigin(x,n):
    partial=0
    for i in range(n):
        val = x[i]
        partial += val**2 - 10 * math.cos(2 * math.pi * val)
    result = 10 * n + partial
    return result

#x,y - two real-valued variables
#min at a,a^2 = 0
def rosenbrock_var(x,y):
    #a & b are parameters of the function
    a = 1
    b = 100
    result = (a - x)**2 + b*(y-x**2)**2
    return result

#x - vector of reals -2.048 ≤ x[i] ≤ 2.048
#n - size of vector
#min at 111111...11 = 0
def rosenbrock_vec(x,n):
    #a & b are parameters of the function
    a = 1
    b = 100
    total = 0
    for i in range(n-1):
        val = x[i]
        total += (a - val)**2 + b*(x[i+1]-val**2)**2
    return total

#x - vector of real numbers -65.536 ≤ x ≤ 65.536
#n - size of the vector
#min at 0000000 = 0 
def schwefel(x, n):
    total = 0
    for i in range(n):
        partial = 0
        for j in range(i):
            partial += x[j]
        total += partial**2

    return total

#x,y - real numbers −3 ≤ x ≤ 3 and −2 ≤ y ≤ 2
#min at (0.0898, −0.7126) and (−0.0898, 0.7126) =  −1.0316
def six_hump_camel_back(x,y):
    result = (4 - 2.1 * x**2 + (1/3) * x**4) * x**2 + x * y + 4 * (y**2 - 1) * y**2
    return result

# x - vector of real numbers -2pi ≤ x ≤ 2pi
#n - size of the vector
#min at 000000..000 = 0
def xin_she_yang(x,n):
    part1 = 0
    part2 = 0
    for i in range(n):
        val = x[i]
        part1 += abs(val)
        part2 += math.sin(val**2)
    result = (-part1) * math.exp(-part2)
    return result

# x - vector 
#n - size of the vector
#min at 000000..000 = 0
def zakharov(x,n):
    part1 = 0
    part2 = 0
    for i in range(n):
        val = x[i]
        part1 += val**2
        part2 += val*i
    result = part1 + ((1/2) * part2)**2 + ((1/2) * part2)**4
    return result
