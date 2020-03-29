import numpy as np
import matplotlib.pyplot as plt

# parameters------------------------------------------------------------------#
n = 100
h = 1./n
c0 = .1
y0 = .1
F0 = 1000
T0 = 20
f = 14

# grid------------------------------------------------------------------------#
yv = np.linspace(.0,.2,n)

# prc-------------------------------------------------------------------------#
def prc(y,c,F,T):
    return (c*F/y)*(1-(1/(1+y))**T)+F/(1+y)**T

# delprc----------------------------------------------------------------------#
def delprc(y,c,F,T):
    return prc(y,c,F,T)/prc(y0,c,F,T)-1

# duration--------------------------------------------------------------------#
def duration(y,c,F,T):
    return -((1+y)/y-((1+y)+T*(c*F-y))/(c*F*((1+y)**T-1)+y))/(1+y)

# convexity-------------------------------------------------------------------#
def convexity(y,c,F,T):
    return

# plotter---------------------------------------------------------------------#
def plotter(PY,leg): 
    for py in PY:
        plt.plot(yv-y0,py,linewidth=4)
    plt.grid()
    plt.xlabel('change in yield ($\Delta y$)',size=f)
    plt.ylabel('percent change in price ($\Delta P/P$)',size=f)
    plt.legend(leg,fontsize=f)
    plt.show()

# exercises-------------------------------------------------------------------#

# baseline
plotter([delprc(yv,c0,F0,T0)],['Bond'])

# Duration
plotter([delprc(yv,c0,F0,T0),-10*(yv-y0)],['Bond','Approximation with Duration'])

# duration
plotter([delprc(yv,c0,F0,T0),-10*(yv-y0),-10*(yv-y0)+30*(yv-y0)**2],['Bond','Approximation with Duration','Approximation with Duration and Convexity'])

# coupon
(plotter([delprc(yv,c0,F0,T0),delprc(yv,c0+.1,F0,T0),
    delprc(yv,c0-.1,F0,T0)],['Baseline','High Coupon','Low Coupon']))

# term
(plotter([delprc(yv,c0,F0,T0),delprc(yv,c0,F0,T0+10),
    delprc(yv,c0,F0,T0-10)],['Baseline','Long Term','Short Term']))
