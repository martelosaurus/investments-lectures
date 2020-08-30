def lev(S0=1,S1=1.,D1=0.,n=1,r=0.,E0=1.):
	A0 = S0*n
	L0 = A0-E0
	L1 = (1.+r/12.)*L0
	A1 = (S1+D1)*n
	E1 = A1-L1
	R1 = (E1-E0)/E0
	_locals =  locals()
	for key in _locals.keys():
		_locals[key] = round(_locals[key],2)
	return _locals

AAPL = lev(
	S0 = 135.36,
	S1 = 125.02,
	D1 = 0.,
	n = 100,
	r = .09569,
	E0 = 10000.
)

MSFT = lev(
	S0 = 135.36,
	S1 = 125.02,
	D1 = 0.,
	n = 100,
	r = .09569,
	E0 = 10000.
)


