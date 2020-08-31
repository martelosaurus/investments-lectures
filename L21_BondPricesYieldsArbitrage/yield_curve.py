"""
Yield curve

Currently performs a cubic approximation on the reported yields
"""
import numpy_financial as npf

def y11_fun(y01,y02):
	y01 = y01/100.
	y02 = y02/100.
	y11 = 2.*((1.+y02/2.)**2./(1.+y01/2.)-1.)
	return round(100.*y11,4)

def prc(yld,trm):
	return round(100./(1.+yld/200.)**trm,4)

def z2_fun(y1,y2):
        _pv = 1.-.5*y2/(1.+.5*y1)
        _fv = .5*y2+1.
        return 2.*npf.rate(2,0.,-_pv,_fv)


Y = [1.,3.,4.,4.5]
T = list(range(1,5))

P1 = [prc(*z) for z in zip(Y,T)]
W1 = [1,1,1,11]

