import math
ma = .05
mb = .05
sa = .20
sb = .20
sra = round(ma/sa,2)
srb = round(mb/sb,2)

def f(x,corr):
	xa = x
	xb = 1.-x
	mp = xa*ma+xb*mb
	var_p = (xa*sa)**2.+(xb*sb)**2.+2.*xa*xb*sa*sb*corr
	print(round(var_p,6))
	sp = math.sqrt(var_p)
	print(round(100.*sp,4))
	return [sra,srb,round(mp/sp,4)]
