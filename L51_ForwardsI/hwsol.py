r = .01
S0 = 24.
S1 = 20.

K0 = S0*(1.+r)**2.
K1 = S1*(1.+r)

f0 = (K1-K0)/(1.+r)
print(round(f0,4))

m1 = .2*K0
m2 = m1 - (K1 - K0)

re = (m2 - m1)/m1
print(round(100.*re,4))

e0 = 1.09
rD = .003
rF = -.006
                                                                            
k0 = (1.+rD)*e0/(1.+rF) 
print(round(k0,4))
