import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

gamma = 1.4

M = np.array(np.arange(1.05,10,0.2)) # Mach number range
batm = np.zeros(M.shape) # batm- beta for max theta initializing
tmax = np.zeros(M.shape) # tmax - theta max initializing

for i in range(0,M.size): #looping for every mach number
 betamin = np.arcsin(1/M[i]) # finind beta minimum
 beeta = np.array(np.arange(betamin,np.pi/2,np.pi/20000)) # storing values of beta for which theta would be calculated
 theeta = np.arctan((2 * ((M[i] * np.sin(beeta))**2 - 1) /
 (np.tan(beeta)*(M[i]**2 * (gamma+np.cos(2*beeta)) + 2)))) # using raltion of theta,beta and M
 tmax[i] = 180/np.pi * np.max(theeta) #theta max
 max_position = pd.Series(theeta).idxmax() # finding index at which theta is maximun in theeata array
 weak_soln = 180/np.pi * theeta [0:int(max_position)] # slicing theeta array into two part one weak solution
 strong_soln = 180/np.pi * theeta[int(max_position)+1:theeta.size] # another strong solution
 beta1 = 180/np.pi * beeta[0:int(max_position)] # slicing beeta array same as theeta
 batm[i] = 180/np.pi * beeta[beta1.size] # batm- beta at theta max
 beta2 = 180/np.pi * beeta[int(max_position)+1:theeta.size]# slice 2 beeta
 plt.plot(weak_soln,beta1,"b",linewidth = 0.3)
 plt.plot(strong_soln,beta2,"r--", linewidth = 0.3)#plotting theta beta graph for various mach number
 
plt.plot(tmax,batm,"c*-") # ploting a line that passes through every theta maximum
plt.title('θ-β-M plots')
plt.xlabel(' θ (in degree)')
plt.ylabel(' β (in degree)')
plt.xlim([0,45])
plt.ylim([0,90])
plt.grid(True)
plt.legend(['Weak Solution','Strong Solution'])
plt.show()