import math as m
def f0(x) :
    return 2*x -(1 + m.sin(x))
def f1(x) :
    return x**4+3*x-9
def f2(x) :
    return 3*m.cos(x)-x-2
def f3(x) :
    return x*m.exp(x)-7
def f4(x) :
    return m.exp(x)-x-10
def f5(x) :
    return 2*m.tan(x)-x-5
def f6(x) :
    return x**2+3-m.exp(x)
def f7(x) :
    return 3*x+4*m.log(x)-7
def f8(x) :
    return x**4-2*x**2+4*x-17
def f9(x) :
    return m.exp(x)-2*m.sin(x)-7
def f10(x) :
    return m.log(x**2+4)*m.exp(x)-10

def methode_dicotomie (f,a0,b0,e) :
    n = 0
    La = []
    Lb = []
    while b0 - a0 > e :
        m = (a0+b0)/2
        if f(a0)*f(m) <= 0 :
            b0 = m
        else :
            a0 = m
            n = n+1
        La.append(a0)
        Lb.append(b0)
    return m,n,La,Lb


print("f : ",methode_dicotomie(f0,0,1,1e-10))
"""
print("f1+ : ",methode_dicotomie(f1,1,1.5,1e-10))
print("f1- : ",methode_dicotomie(f1,-2,-1.5,1e-10))
print("f2+ : ",methode_dicotomie (f2,0.5,1,1e-10))
print("f2- : ",methode_dicotomie (f2,-1.5,-1,1e-10))
print("f2-- : ",methode_dicotomie (f2,-4,-3.5,1e-10))
print("f3 : ",methode_dicotomie (f3,1,2,1e-10))
"""

