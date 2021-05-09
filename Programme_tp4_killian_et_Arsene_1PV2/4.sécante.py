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
def Secante(f,x0,x1,epsilon,Nitermax):
    n= 1
    xold = x0
    xoldold = x1
    xnew = xoldold - (xoldold-xold)*f(xoldold)/(f(xoldold)-f(xold))
    difference = xnew - xold
    xold = xnew
    L_Secante_n = [1]
    L_Secante_xn = [x0, x1, xold]
    L_Secante_en = [abs(difference)]
    while abs(difference)>epsilon and n< Nitermax :
        xnew = xoldold - (xoldold-xold)*f(xoldold)/(f(xoldold)-f(xold))
        difference = xnew-xold
        xold = xnew
        n =n+1
        L_Secante_n.append(n)
        L_Secante_xn.append(xold)
        L_Secante_en.append(abs(difference))
    return 'Suite des x(n):  ',L_Secante_xn, 'Suite des ittérations:  ',L_Secante_n,'Suite des e(n):  ',L_Secante_en



##def Secante(f,x0,x1,epsilon,Nitermax):
##    n= 0
##
##    while True and n< Nitermax :
##        x = x1 - (x1-x0)*f(x1)/(f(x1)-f(x0))
##        n = n+1
##        if abs(x-x1) <= epsilon :
##            return x,n

print("f1+ : ",Secante(f1,1,1.5,1e-3,5e4))
'''
print("f1- : ",Secante(f1,-2,-1.5,1e-3,5e4))
print("f2+ : ",Secante (f2,0.5,1,1e-3,5e4))
print("f2- : ",Secante (f2,-1.5,-1,1e-3,5e4))
print("f2-- : ",Secante (f2,-4,-3.5,1e-3,5e4))
print("f3 : ",Secante (f3,1,2,1e-3,5e4))
print("f4- : ",Secante (f4,-10,-9.5,1e-3,5e4))
print("f4+ : ",Secante (f4,2.5,2.6,1e-3,5e4))
print("f5 : ",Secante (f5,1.2,1.3,1e-3,5e4))
print("f6 : ",Secante (f6,1.5,1.9,1e-3,5e4))
print("f7 : ",Secante (f7,1.6,1.7,1e-3,5e4))
print("f8+ : ",Secante (f8,2,2.5,1e-3,5e4))
print("f8- : ",Secante (f8,-2.51,-2.5,1e-3,5e4))
print("f9 : ",Secante (f9,2.1,2.25,1e-3,5e4))
print("f10 : ",Secante(f10,1.5,1.7,1e-3,5e4))
'''
