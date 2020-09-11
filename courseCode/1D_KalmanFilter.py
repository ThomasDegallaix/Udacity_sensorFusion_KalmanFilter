from math import *

#Simple 1-D Kalman Filter implementation

#Gaussian 1
# mu_1 = 10
# sigma2_1 = 8 #4

# #Gaussian 2
# mu_2 = 13 #12
# sigma2_2 = 2 #4

#Measurement update
def update(mean1, var1, mean2, var2):
    new_mean = (1/(var1 + var2))*(var2 * mean1 + var1 * mean2)
    new_var = 1/(1/var1 + 1/var2)
    return [new_mean, new_var]

#Motion update (mean2 and var2 correspond to the motion and its uncertainty)
def predict(mean1,var1,mean2,var2):
    new_mean = mean1 + mean2
    new_var = var1 + var2
    return [new_mean, new_var]

measurements = [5., 6., 7., 9., 10.]
motion = [1., 1., 2., 1., 1.]
measurement_sigma2 = 2.
motion_sigma2 = 2.
mu = 0.
sigma2 = 10000 # = Not confident about initial position #0.0000000000001 = really confident 

#The first estimate for position should become 5 because the inital uncertainty (10000) is so large that the estimate is dominated by the measurement
#The uncertainty should be sligthly better than 4 for the first estimate 
#The motion update creates uncertainty and the measurement update diminishes it

for n in range(len(measurements)):
    [mu, sigma2] = update(mu, sigma2, measurements[n], measurement_sigma2)
    #print("Update ", [mu, sigma2])
    [mu, sigma2] = predict(mu, sigma2, motion[n], motion_sigma2)
    #print("Predict ", [mu, sigma2])

print([mu, sigma2])