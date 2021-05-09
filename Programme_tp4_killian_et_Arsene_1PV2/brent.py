import math as m

def f0(x) :
    return 2*x -1 -m.sin(x)


def Brent(f, a, b, e):
       n = 0
       fa = f(a)
       fb = f(b)
       if fa*fb >= 0:
              print('non')
              return None
       if abs(fa) < abs(fb):
              c=a
              a=b
              b=c
              fc=fa
              fa=fb
              fb=fc

       c = a
       fc = fa
       mflag = True

       while f(b) != 0 and abs(b - a)>e:
              if fa != fc and fb != fc:
                     S = ((fb*fa)/((fc-fb)*(fc-fa))*c)+((fc*fa)/((fb-fc)*(fb-fa))*b)+((fc*fb)/((fa-fc)*(fa-fb))*a)
              else:
                     S = a-fa*(b-a)/(fb-fa)

                     
              if (S - a)*(S - b)<0:
                     S = (a+b)/2
              fS = f(S)
              c = b
              if fS * fb < 0:
                     a = b
                     fa = fb
              else:
                     fa = fa/2
              b = S
              fb = fS
              n = n + 1

       return 'résultat: ',b," et le nombre d'itérations: ",n

print(Brent(f0, -3, 2, 1e-10))
