import math as m
import matplotlib.pyplot as pp
import numpy as np

def f0(x) :
    return 2*x -(1 + m.sin(x))
def f1(x) :
    return x**4+3*x-9
def f2(x) :
    return 3*m.cos(x)-x-2
def f3(x) :
    return x*m.exp(x)-7


def g0(x) :
    return (1 + m.sin(x))/2
def g1_1(x) :
    return((9-3*x)**0.25)
def g1_2(x) :
    return-((9-3*x)**0.25)
def g2_1 (x):
    return(m.acos((x+2)/3))
def g2_2 (x):
    return(-(m.acos((x+2)/3)))
def g3 (x):
    return(m.log(7)-m.log(x))


def fder0 (x) :
    return 2 - m.cos(x)
def fder1 (x) :
    return 4*x**3+3
def fder2 (x) :
    return -3*m.sin(x)-1
def fder3(x):
    return m.exp(x)*(1+x)


####### Fonction résultat

def Point_fixe(g,x0,e,Nitermax):
    L_Pointfixe_n = []
    xold= x0
    xnew = g(xold)
    difference = xnew - xold
    xold = xnew
    n = 1
    L_Pointfixe_xn = []
    L_Pointfixe_en = []
    while abs(difference)>e and n< Nitermax :
        xnew = g(xold)
        difference = xnew-xold
        xold = xnew
        n =n+1
        L_Pointfixe_n.append(n)
        L_Pointfixe_xn.append(xold)
        L_Pointfixe_en.append(abs(difference))
    return L_Pointfixe_n, L_Pointfixe_xn, L_Pointfixe_en


def newton (f,fder,x0,e,Nitermax):
    xold= x0
    xnew = xold-(f(xold)/fder(xold))
    difference = xnew - xold
    xold = xnew
    n = 1
    L_Newton_n = []
    L_Newton_xn = []
    L_Newton_en = []
    while abs(difference)>e and n< Nitermax :
        xnew = xold-(f(xold)/fder(xold))
        difference = xnew-xold
        xold = xnew
        n =n+1
        L_Newton_n.append(n)
        L_Newton_xn.append(xold)
        L_Newton_en.append(abs(difference))
        
    return L_Newton_n,L_Newton_xn,L_Newton_en

def methode_dicotomie(f,a0,b0,e) :
    n = 0
    L_Dichotomie_n = []
    L_Dichotomie_xn = []
    L_Dichotomie_en = []
    while b0 - a0 > e :
        m = (a0+b0)/2
        if f(a0)*f(m) <= 0 :
            b0 = m   
        else :
            a0 = m
        n = n+1
        L_Dichotomie_n.append(n)
        L_Dichotomie_xn.append(m)
        L_Dichotomie_en.append(abs(b0-a0))
    return L_Dichotomie_n, L_Dichotomie_xn, L_Dichotomie_en

def Secante(f,x0,x1,epsilon,Nitermax):
    n= 1
    xold = x0
    xoldold = x1
    xnew = xoldold - (xoldold-xold)*f(xoldold)/(f(xoldold)-f(xold))
    difference = xnew - xold
    xold = xnew
    L_Secante_n = []
    L_Secante_xn = []
    L_Secante_en = []
    while abs(difference)>epsilon and n< Nitermax :
        xnew = xoldold - (xoldold-xold)*f(xoldold)/(f(xoldold)-f(xold))
        difference = xnew-xold
        xold = xnew
        n =n+1
        L_Secante_n.append(n)
        L_Secante_xn.append(xold)
        L_Secante_en.append(abs(difference))
    return L_Secante_n,L_Secante_xn,L_Secante_en

#####methode point fixe

pp.subplot(111)
#fo
L_Pointfixe_n, L_Pointfixe_xn, L_Pointfixe_en = Point_fixe(g0,0,1e-10,5e4)
pp.semilogy(L_Pointfixe_n,L_Pointfixe_en)
#f0
L_Newton_n,L_Newton_xn,L_Newton_en = newton (f0,fder0,0,1e-10,5e4)
pp.semilogy(L_Newton_n,L_Newton_en)
#f0
L_Dichotomie_n, L_Dichotomie_xn, L_Dichotomie_en = methode_dicotomie(f0,0,1,1e-10)
pp.semilogy(L_Dichotomie_n,L_Dichotomie_en)
#fo
L_Secante_n,L_Secante_xn,L_Secante_en =  Secante(f0,0,1,1e-10,5e4)
pp.semilogy(L_Secante_n,L_Secante_en)
pp.semilogy(L_Pointfixe_n,L_Pointfixe_en)
pp.xlabel("n",fontsize=10)
pp.ylabel("e_n",fontsize=10)
pp.title("evolution des erreurs de la fonction f0",fontsize=10)

"""
pp.subplot(321)

#f1-
L_Pointfixe_n, L_Pointfixe_xn, L_Pointfixe_en = Point_fixe(g1_1,1.5,1e-10,5e4)
pp.semilogy(L_Pointfixe_n,L_Pointfixe_en)

#f1-
L_Newton_n,L_Newton_xn,L_Newton_en = newton (f1,fder1,-1.5,1e-10,5e4)
pp.semilogy(L_Newton_n,L_Newton_en)

#f1-
L_Dichotomie_n, L_Dichotomie_xn, L_Dichotomie_en = methode_dicotomie(f1,-2,-1.5,1e-10)
pp.semilogy(L_Dichotomie_n,L_Dichotomie_en)

#f1-
L_Secante_n,L_Secante_xn,L_Secante_en =  Secante(f1,-2,-1.5,1e-10,5e4)
pp.semilogy(L_Secante_n,L_Secante_en)

pp.xlabel("n",fontsize=10)
pp.ylabel("e_n",fontsize=10)
pp.title("f1-",fontsize=10)


pp.subplot(322)

#f1+
L_Pointfixe_n, L_Pointfixe_xn, L_Pointfixe_en = Point_fixe(g1_2,-1.5,1e-10,5e4)
pp.semilogy(L_Pointfixe_n,L_Pointfixe_en)

#f1+
L_Newton_n,L_Newton_xn,L_Newton_en = newton (f1,fder1,1.5,1e-10,5e4)
pp.semilogy(L_Newton_n,L_Newton_en)

#f1+
L_Dichotomie_n, L_Dichotomie_xn, L_Dichotomie_en = methode_dicotomie(f1,1,1.5,1e-10)
pp.semilogy(L_Dichotomie_n,L_Dichotomie_en)

#f1+
L_Secante_n,L_Secante_xn,L_Secante_en =  Secante(f1,1,1.5,1e-10,5e4)
pp.semilogy(L_Secante_n,L_Secante_en)

pp.xlabel("n",fontsize=10)
pp.ylabel("e_n",fontsize=10)
pp.title("f1+",fontsize=10)

pp.subplot(323)

#f2+
L_Pointfixe_n, L_Pointfixe_xn, L_Pointfixe_en = Point_fixe(g2_1,0.5,1e-10,5e4)
pp.semilogy(L_Pointfixe_n,L_Pointfixe_en)

#f2+
L_Newton_n,L_Newton_xn,L_Newton_en = newton (f2,fder2,0.5,1e-10,5e4)
pp.semilogy(L_Newton_n,L_Newton_en)

#f2+
L_Dichotomie_n, L_Dichotomie_xn, L_Dichotomie_en = methode_dicotomie(f2,0.5,1,1e-10)
pp.semilogy(L_Dichotomie_n,L_Dichotomie_en)

#f2+
L_Secante_n,L_Secante_xn,L_Secante_en =  Secante(f2,0.5,1,1e-10,5e4)
pp.semilogy(L_Secante_n,L_Secante_en)

pp.xlabel("n",fontsize=10)
pp.ylabel("e_n",fontsize=10)
pp.title("f2+",fontsize=10)

pp.subplot(324)

#f2-
L_Pointfixe_n, L_Pointfixe_xn, L_Pointfixe_en = Point_fixe(g2_2,-1.5,1e-10,5e4)
pp.semilogy(L_Pointfixe_n,L_Pointfixe_en)

#f2-
L_Newton_n,L_Newton_xn,L_Newton_en = newton (f2,fder2,-1.5,1e-10,5e4)
pp.semilogy(L_Newton_n,L_Newton_en)

#f2-
L_Dichotomie_n, L_Dichotomie_xn, L_Dichotomie_en = methode_dicotomie(f2,-1.5,-1,1e-10)
pp.semilogy(L_Dichotomie_n,L_Dichotomie_en)

#f2-
L_Secante_n,L_Secante_xn,L_Secante_en =  Secante(f2,-1.5,-1,1e-10,5e4)
pp.semilogy(L_Secante_n,L_Secante_en)

pp.xlabel("n",fontsize=10)
pp.ylabel("e_n",fontsize=10)
pp.title("f2-",fontsize=10)

pp.subplot(325)
#f2--
L_Newton_n,L_Newton_xn,L_Newton_en = newton (f2,fder2,-5,1e-10,5e4)
pp.semilogy(L_Newton_n,L_Newton_en)
#f2--
L_Dichotomie_n, L_Dichotomie_xn, L_Dichotomie_en = methode_dicotomie(f2,-4,-3.5,1e-10)
pp.semilogy(L_Dichotomie_n,L_Dichotomie_en)
#f2--
L_Secante_n,L_Secante_xn,L_Secante_en =  Secante(f2,-4,-3.5,1e-10,5e4)
pp.semilogy(L_Secante_n,L_Secante_en)
pp.xlabel("n",fontsize=10)
pp.ylabel("e_n",fontsize=10)
pp.title("f2--",fontsize=10)

pp.subplot(326)
#f3
L_Pointfixe_n, L_Pointfixe_xn, L_Pointfixe_en = Point_fixe(g3,1.5,1e-10,5e4)
pp.semilogy(L_Pointfixe_n,L_Pointfixe_en)

#f3
L_Newton_n,L_Newton_xn,L_Newton_en = newton (f3,fder3,2,1e-10,5e4)
pp.semilogy(L_Newton_n,L_Newton_en)

#f3
L_Dichotomie_n, L_Dichotomie_xn, L_Dichotomie_en = methode_dicotomie(f3,1,2,1e-10)
pp.semilogy(L_Dichotomie_n,L_Dichotomie_en)
#f3
L_Secante_n,L_Secante_xn,L_Secante_en =  Secante(f3,1,2,1e-10,5e4)
pp.semilogy(L_Secante_n,L_Secante_en)

pp.xlabel("n",fontsize=10)
pp.ylabel("e_n",fontsize=10)
pp.title("f3",fontsize=10)

"""

pp.show()







