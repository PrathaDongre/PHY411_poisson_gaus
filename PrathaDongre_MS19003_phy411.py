from matplotlib import pyplot as plt
import numpy as np
import math
import scipy.special as sps
import random

#Question 3 part (b)

def gaussian(x, mu):
    #taking sigma as sqrt(mean) to make sense in comparison to poisson
    #y =  (1/sig*math.sqrt(2*math.pi))* np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))
    y = (1/math.sqrt(2*math.pi*mu))* np.exp(-np.power(x - mu, 2.) / (2 * np.power(math.sqrt(mu), 2.)))
    return y

'''x_values = np.linspace(-3, 3, 120)
for mu, sig in [(-1, 1), (0, 2), (2, 3)]:
    plt.plot(x_values, gaussian(x_values, mu, sig))
'''
def poisson(k_array, lmd):
    y = np.power(lmd, k_array)* np.exp(-lmd) / sps.factorial(k_array)
    return y

k_array = np.linspace(0,50,50)
x_array = np.linspace(0,50, 300)

for lmda in [2,5,10,15,20,25]:
    plt.plot(k_array, poisson(k_array, lmda), linestyle='none', marker='.')

    plt.plot(x_array, gaussian(x_array, lmda))

plt.show()

def deviation(k_array, lmda):
    pois_array = poisson(k_array, lmda)
    gaus_array = gaussian(k_array, lmda)
    diff = np.subtract(pois_array,gaus_array)
    plt.plot(k_array, diff)


for lmda in [2,5,10,15,20,25]:
    deviation(k_array, lmda)
    plt.legend([2,5,10,15,20,25])
plt.show()

def poisson_int(k_int, lmd):
    y = (lmd** k_int)* math.exp(-lmd) / np.math.factorial(k_int)
    return y

def gaussian_int(x_int, mu):

    y = (1/math.sqrt(2*math.pi*mu))* math.exp(-(x - mu** 2.) / (2 * (math.sqrt(mu)** 2.)))
    return y


for lmda in [2,5,10,15,20,25]:
    #generates as many samples from data as we want
    x_samples = np.random.choice(x_array)
    k_samples = np.random.choice(k_array)

    plt.plot(k_samples, poisson(k_samples, lmda), linestyle='none', marker='.')
    
    #plotting sampled data:
