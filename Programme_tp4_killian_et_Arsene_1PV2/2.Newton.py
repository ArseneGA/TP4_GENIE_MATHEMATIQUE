import math as m

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

def fder1 (x) :
    return 4*x**3+3
def fder2 (x) :
    return -3*m.sin(x)-1
def fder3(x):
    return m.exp(x)*(1+x)
def fder4(x):
    return m.exp(x)-1
def fder5 (x) :
    return 2/(m.cos(x))**2-1
def fder6 (x) :
    return -m.exp(x)+2*x
def fder7 (x) :
    return 3+4/x
def fder8 (x) :
    return 4*x**3-4*x+4
def fder9 (x) :
    return m.exp(x)-2*m.cos(x)
def fder10 (x) :
    return m.exp(x)*((2*x)/(x**2+4)+m.log(x**2+4))


def newton (f,fder,x0,e,Nitermax):
    xold= x0
    xnew = xold-(f(xold)/fder(xold))
    difference = xnew - xold
    xold = xnew
    n = 1
    while abs(difference)>e and n< Nitermax :
        xnew = xold-(f(xold)/fder(xold))
        difference = xnew-xold
        xold = xnew
        n =n+1
    return xnew,n

print("f1- : ",newton(f1,fder1,-1.5,1e-3,5e4))
print("f1+ : ",newton(f1,fder1,1.5,1e-3,5e4))
print("f2+ : ",newton (f2,fder2,0.5,1e-3,5e4))
print("f2- : ",newton (f2,fder2,-1.5,1e-3,5e4))
print("f2-- : ",newton (f2,fder2,-5,1e-3,5e4))
print("f3 : ",newton (f3,fder3,2,1e-3,5e4))
print("f4- : ",newton (f4,fder4,-9.5,1e-3,5e4))
print("f4+ : ",newton (f4,fder4,2.5,1e-3,5e4))
print("f5 : ",newton (f5,fder5,1.2,1e-3,5e4))
print("f6 : ",newton (f6,fder6,1.5,1e-3,5e4))
print("f7 : ",newton (f7,fder7,1.6,1e-3,5e4))
print("f8+ : ",newton (f8,fder8,2.5,1e-3,5e4))
print("f8- : ",newton (f8,fder8,-2.5,1e-3,5e4))
print("f9 : ",newton (f9,fder9,2.25,1e-3,5e4))
print("f10 : ",newton (f10,fder10,1.5,1e-3,5e4))
