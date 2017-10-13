from math import sqrt, log2, log, factorial
import matplotlib.pyplot as plt


#sqrt(x)
def fun0(x):
    return sqrt(x)
#3^log2n
def fun1(x):
    return pow(3,log2(x))
 
#sqrt(log4n)
def fun2(x):
    return sqrt(log(x, 4))

#log2log2n
def fun3(x):
    return log2(log2(x))
#(log2n)^2
def fun4(x):
    return pow(log2(x),2)
#2^n
def fun5(x):
    return pow(2, x)
#4^n
def fun6(x):
    return pow(4, x)
#n!
def fun7(x):
    return factorial(x)
#log3n
def fun8(x):
    return log(x, 3)
#n^log2n
def fun9(x):
    return pow(x, log2(x))
#n/log5n
def fun10(x):
    return x/(log(x, 5))
#n^sqrt(n)
def fun11(x):
    return pow(x, sqrt(x))
#2^2^n
def fun12(x):
    return pow(2, pow(2, x))
#log2n!
def fun13(x):
    return log2(factorial(x))
#n^2
def fun14(x):
    return pow(x, 2)
#(log2n)^log2n
def fun15(x):
    return pow(log2(x), log2(x))
#7^(log2n)
def fun16(x):
    return pow(7, log2(x))
#2^3n
def fun17(x):
    return pow(2, 3*x)



funcs = [fun0, fun1, fun2, fun3, fun4, 
         fun5, fun6, fun7, fun8, fun9,
         fun10, fun11, fun12, fun13, fun14,
         fun15, fun16, fun17]

names = ["sqrt(n)", "3^log2n", "sqrt(log4n)", "log2log2n", "(log2n)^2",
         "2^n", "4^n", "n!", "log3n", "n^log2n", 
         "n/log5n", "n^sqrt(n)", "2^2^n", "log2(n!)", "n^2",
         "(log2n)^log2n", "7^(log2n)", "2^3n"]

all_func = (#12, #"2^2^n"
#            7, #n!
#            17, #2^3n
#            6, #4^n
#            5, #2^n
            #11, #n^sqrt(n)
            #9, #n^log2n
            #15, #(log2n)^log2n
#            16,  #7^(log2n)  
#            14, #n^2
#            1, #3^log2n
#            13, #log2n!+
#            10, #n/log5n
#            0, #sqrt(n) changed
#            4, #(log2n)^2
            #8, #log3n
            3, #log2log2n
            2 #sqrt(log4n)
            ) 


#12, 17, 7, 6, 9, 11, 5, 16
#2^2^n, 2^3n, n!, 4^n, n^log3n, n^sqrt(n), 2^n, 7^log2n


x_range = list(range(2, 10^7))

for i in all_func:
    y_range = [funcs[i](x) for x in x_range]
    plt.plot(x_range, y_range, label = names[i])
plt.legend(loc='lower left')
plt.show()
