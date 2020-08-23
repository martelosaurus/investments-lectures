def y11_fun(y01,y02):
	y01 = y01/100.
	y02 = y02/100.
	y11 = 12.*((1.+y02/6.)/(1.+y01/12.)-1.)
	return round(100.*y11,4)

def prc(yld,trm):
	return round(100./(1.+trm*yld/100.),4)

Y = [1.72,1.47,1.38]
T = list(range(1,4))

P1 = [prc(*z) for z in zip(Y,T)]
W1 = [1,1,11]

P2 = [prc(*z) for z in zip(Y,T)]
W2 = [.5,.5,10.5]





