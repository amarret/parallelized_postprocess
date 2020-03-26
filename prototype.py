
import time
import numpy as np
import multiprocessing
import sys

#==========================================
#wrapper for parallelized  calculation    
    
def wrapper_myfunction(args):
    
    return myfunction(*args)


#==========================================
def myfunction(x,y,z):
    
    time.sleep(1)
    
    return 3*x, y**2, z+1


#==========================================
#inputs
x = np.ones([10,100])
y = np.ones([10,100])
z = np.ones([10,100])
N = len(x)

multiplied_x = np.zeros([10,100])
squared_y = np.zeros([10,100])
added_z = np.zeros([10,100])


#==========================================
#Parallelized computation

nbrCores = 4


workers = multiprocessing.Pool(processes = nbrCores)

inputs = (np.array([x[i], y[i], z[i]]) for i in xrange(N))

results = workers.imap(wrapper_myfunction,inputs)

for i, data in enumerate(results, 0): 
    
    multiplied_x[i] = data[0]
    squared_y[i]    = data[1]
    added_z[i]      = data[2]
    
    sys.stderr.write('\rProgress : {0}/{1}'.format(i+1,N))
    
workers.close()
workers.join()














