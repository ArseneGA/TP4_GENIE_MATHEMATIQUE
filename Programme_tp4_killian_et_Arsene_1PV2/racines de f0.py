import math as m
def f0(x) :
    return 2*x -(1 + m.sin(x))
def g0(x) :
    return (1 + m.sin(x))/2
def fder0 (x) :
    return 2 - m.cos(x)

def Point_fixe (g,x0,e,Nitermax):
    xold= x0
    xnew = g(xold)
    difference = xnew - xold
    xold = xnew
    n = 1
    while abs(difference)>e and n< Nitermax :
        xnew = g(xold)
        difference = xnew-xold
        xold = xnew
        n =n+1
    return xnew,n

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

def methode_dicotomie (f,a0,b0,e) :
    n = 0
    L_Dichotomie_An = []
    L_Dichotomie_Bn = []
    while b0 - a0 > e :
        m = (a0+b0)/2
        if f(a0)*f(m) <= 0 :
            b0 = m
        else :
            a0 = m
        n = n+1
        L_Dichotomie_An.append(a0)
        L_Dichotomie_Bn.append(b0)
    return m,n, 

def Secante(f,x0,x1,epsilon,Nitermax):
    n= 1
    xold = x0
    xoldold = x1
    xnew = xoldold - (xoldold-xold)*f(xoldold)/(f(xoldold)-f(xold))
    difference = xnew - xold
    xold = xnew
    while abs(difference)>epsilon and n< Nitermax :
        xnew = xoldold - (xoldold-xold)*f(xoldold)/(f(xoldold)-f(xold))
        difference = xnew-xold
        xold = xnew
        n =n+1
    return xnew,n
print("point fixe : ",Point_fixe (g0,0,1e-10,5e4))
print("newton : ",newton(f0,fder0,0,1e-10,5e4))
print("dichotomie : ",methode_dicotomie(f0,0,1,1e-10))
print("secante : ",Secante(f0,0,1,1e-10,5e4))

