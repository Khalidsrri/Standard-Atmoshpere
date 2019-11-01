import math

R = 287
g = 9.81

# Standard atm
a0 = -6.5e-3
p0 = 101325
T0 = 288.15
rho0 = 1.225
h0 = 0

# Tropopause
h1 = 11
T1 = T0+a0*(h1-h0)*1e3
p1 = p0*(T1/T0)**(-g/(a0*R))
rho1 = rho0*(T1/T0)**((-g/(a0*R))-1)


# Stratopause
a2 = 1e-3
h2 = 20
T2 = T1
x = math.e**((-g*(h2-h1)*1e3)/(T1*R))
p2 = p1*x
rho2 = rho1*x

# Mezopause
a3 = 2.8e-3
h3 = 32
T3 = T2+a2*(h3-h2)*1e3
p3 = p2*(T3/T2)**(-g/(a2*R))
rho3 = rho2*(T3/T2)**((-g/(a2*R))-1)
while(1) :
    while(1) :
        h = input("what is the altitude ? (In Km) ")
        try :
            h = float(h)
            break
        except :
            print('Wrong entry ! try again')
        
    if(h < 11) :
        T = T0+a0*(h-h0)*1e3
        p = p0*(T/T0)**(-g/(a0*R))
        rho = rho0*(T/T0)**((-g/(a0*R))-1)
    elif (h < 20) :
        T = T1
        x = math.e**((-g*(h-h1)*1e3)/(T1*R))
        p = p1*x
        rho = rho1*x
    elif (h < 32) :
        T = T2+a2*(h-h2)*1e3
        p = p2*(T/T2)**(-g/(a2*R))
        rho = rho2*(T/T2)**((-g/(a2*R))-1)
    else :
        T = T3+a3*(h-h3)*1e3
        p = p3*(T/T3)**(-g/(a3*R))
        rho = rho3*(T/T3)**((-g/(a3*R))-1)


    print('p=', round(p, 4), '(Pa)',
     'rho=', round(rho, 4), '(Kg/m^3)',
      'T=', round(T, 4), '(K)')
    print()
