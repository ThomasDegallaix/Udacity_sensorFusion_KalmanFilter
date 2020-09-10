from math import *

#Simple 1-D Kalman Filter implementation

#Gaussian 1
mu_1 = 10
sigma2_1 = 8 #4

#Gaussian 2
mu_2 = 13 #12
sigma2_2 = 2 #4

#Measurement update
def update(mean1, var1, mean2, var2):
    new_mean = (1/(var1 + var2))*(var2 * mean1 + var1 * mean2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

#Motion update (man2 and var2 correspond to the motion and its uncertainty)
def predict(mean1,var1,mean2,var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]


print(update(mu_1,sigma2_1,mu_2,sigma2_2))
print(predict(mu_1,sigma2_1,mu_2,sigma2_2))