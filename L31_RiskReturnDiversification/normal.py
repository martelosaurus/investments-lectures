import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rc

rc('font',size=12)

@np.vectorize
def _pdf(x,mu,sigma):
	z = (x-mu)/sigma
	return np.exp(-.5*z**2.)/(np.sqrt(2*np.pi)*sigma)

class Normals:

	def __init__(self,mu,sigma,name):
		"""
		mu : tuple (of floats)
			Means
		sigma : tuple (of floats)
			Standard deviations
		name : str
			Filename (without extension)
		"""
		
		if len(mu) is not 2:
			raise Exception("too many/few means")
		else:
			self.mu = mu

		if len(sigma) is not 2:
			raise Exception("too many/few standard deviations")
		else:
			self.sigma = sigma

		self.name = name

	def plot(self,n_plt=100,lin_wid=3,num_sig=3.5):
		"""
		n_plt : int
			#of plotting knots
		lin_wid : float
			Linewidth
		num_sig : int
	`		#of sigmas on x-axis
		"""
		
		mu_max = max(self.mu)
		mu_min = min(self.mu)
		sigma_lim = max(self.sigma)
		mu_plt_min = mu_min-num_sig*sigma_lim
		mu_plt_max = mu_max+num_sig*sigma_lim
		mu_plt = np.linspace(mu_plt_min,mu_plt_max,n_plt)

		plt.plot(mu_plt,_pdf(mu_plt,mu_min,self.sigma[0]),linewidth=lin_wid)
		plt.plot(mu_plt,_pdf(mu_plt,mu_max,self.sigma[1]),linewidth=lin_wid)

		# yticks
		plt.yticks([],[])
		
		# xticks
		if mu_min is not mu_max:
			plt.xticks([mu_min,mu_max],[r'$\mu_{L}$',r'$\mu_{H}$'])
		else:
			plt.xticks([mu_min],[r'$\mu$'])

		# legend 
		if min(self.sigma) is not max(self.sigma):
			plt.legend([r'$\sigma_{L}$',r'$\sigma_{H}$'])

		# labels
		plt.xlabel('Returns')
		plt.ylabel('Frequency')

		# TODO somthing more robust than replace
		plt.grid()
		#plt.show()
		plt.savefig(self.name.replace(' ','_') + '.pdf')
		plt.close()

N = Normals((0.,2.),(1.,1.),'mean_shift').plot()
N = Normals((0.,0.),(1.,2.),'stdv_shift').plot()
N = Normals((0.,2.),(1.,2.),'mean_stdv_shift').plot()
